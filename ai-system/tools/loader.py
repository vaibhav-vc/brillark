"""Reference loader for the ai-system organisation.

The definitions in this repository are portable, but portable is not the same as usable. This is
the executable contract: it assembles an agent's context in the correct order, enforces the budgets,
resolves the model tier through the active profile, and validates what comes back.

Copy it, port it, or call it. If your runtime disagrees with this file, your runtime is wrong —
`tests/test_conformance.py` checks this implementation against the written contract.

    python3 ai-system/tools/loader.py domains
    python3 ai-system/tools/loader.py agents --domain hardware
    python3 ai-system/tools/loader.py assemble --agent pcb-layout-designer --task "Route the sensor board"
    python3 ai-system/tools/loader.py assemble --agent director --task "..." --out /tmp/ctx.txt
    python3 ai-system/tools/loader.py validate-return --file return.json

No third-party dependencies beyond PyYAML.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHARS_PER_TOKEN = 4

# The cacheable prefix, in order. Everything here is stable for a session; anything variable
# placed inside it destroys cache reuse for all of it.
STABLE_PREFIX = [
    "prompts/system/00-base-agent.md",
    "prompts/system/05-token-discipline.md",
    "skills/OUTPUT_CONTRACT.md",
]
TIER_PROMPT = {
    "director": "prompts/system/01-director.md",
    "head": "prompts/system/02-domain-head.md",
    "council": "prompts/system/03-council-critic.md",
    "specialist": "prompts/system/04-specialist.md",
}
IMPROVEMENT_PROMPT = "prompts/system/06-self-modification.md"


def tok(text: str) -> int:
    """Estimate tokens. Deliberately crude and deliberately consistent: this is a budget yardstick,
    not a tokeniser. Swap it for your provider's counter if you need billing accuracy."""
    return len(text) // CHARS_PER_TOKEN


class BudgetExceeded(RuntimeError):
    pass


class Organisation:
    def __init__(self, root: pathlib.Path = ROOT, profile: str | None = None):
        self.root = root
        self.agents = {a["id"]: a for a in
                       yaml.safe_load((root / "agents" / "registry.yaml").read_text())["agents"]}
        self.skills = {s["name"]: s for s in
                       yaml.safe_load((root / "skills" / "registry.yaml").read_text())["skills"]}
        self.budget = yaml.safe_load((root / "runtime" / "context-budget.yaml").read_text())
        self.profiles = yaml.safe_load((root / "runtime" / "model-profiles.yaml").read_text())
        self.profile_name = profile or self.profiles["active_profile"]
        if self.profile_name not in self.profiles["profiles"]:
            raise SystemExit(f"unknown profile '{self.profile_name}'; "
                             f"available: {', '.join(self.profiles['profiles'])}")
        self.profile = self.profiles["profiles"][self.profile_name]

    # ---- model resolution ------------------------------------------------------------------
    def resolve_model(self, task_class: str) -> str:
        """task_class -> concrete model, through the active profile. A null tier is a hard error:
        silently falling back to a stronger model hides a misconfiguration and inflates cost."""
        model = self.profile.get(task_class)
        if model is None:
            raise SystemExit(
                f"profile '{self.profile_name}' has no model for task_class '{task_class}'.\n"
                f"Set it in runtime/model-profiles.yaml — this is not defaulted on purpose.")
        if isinstance(model, str) and model.startswith("${") and model.endswith("}"):
            env = model[2:-1]
            resolved = os.environ.get(env)
            if not resolved:
                raise SystemExit(f"profile '{self.profile_name}' needs environment variable {env}")
            return resolved
        return model

    def escalated_model(self, task_class: str) -> str:
        """Escalation moves up a tier, never to a named model."""
        ladder = ["mechanical", "analytical", "judgement"]
        idx = min(ladder.index(task_class) + 1, len(ladder) - 1)
        return self.resolve_model(ladder[idx])

    # ---- tier 1: discovery -----------------------------------------------------------------
    def domains(self) -> list[dict]:
        rows = self._tsv(self.root / "agents" / "index" / "_domains.tsv")
        return [{"domain": r[0], "head": r[1], "agents": int(r[2]), "cards": r[3], "owns": r[4]}
                for r in rows]

    def agents_in(self, domain: str) -> list[dict]:
        path = self.root / "agents" / "index" / f"{domain}.tsv"
        if not path.exists():
            raise SystemExit(f"no such domain '{domain}'; try: loader.py domains")
        return [{"id": r[0], "tier": r[1], "model_tier": r[2], "capability": r[3]}
                for r in self._tsv(path)]

    def tier1_cost(self, domain: str) -> int:
        return (tok((self.root / "agents" / "index" / "_domains.tsv").read_text())
                + tok((self.root / "agents" / "index" / f"{domain}.tsv").read_text()))

    # ---- tier 2: activation ----------------------------------------------------------------
    def assemble(self, agent_id: str, task: str = "", context_package: dict | None = None,
                 enforce: bool = True) -> dict:
        """Build the full context for one agent run, in cache order, within budget."""
        agent = self.agents.get(agent_id)
        if agent is None:
            raise SystemExit(f"no such agent '{agent_id}'; try: loader.py agents --domain <d>")

        parts: list[tuple[str, str]] = []

        # Stable prefix — never reorder, never interleave anything variable.
        for rel in STABLE_PREFIX:
            parts.append((rel, (self.root / rel).read_text()))
        tier_prompt = TIER_PROMPT.get(agent["tier"])
        if tier_prompt:
            parts.append((tier_prompt, (self.root / tier_prompt).read_text()))
        if agent["domain"] == "improvement":
            parts.append((IMPROVEMENT_PROMPT, (self.root / IMPROVEMENT_PROMPT).read_text()))

        # Tier 1 discovery for this domain, then the charter.
        parts.append((f"agents/index/{agent['domain']}.tsv",
                      (self.root / "agents" / "index" / f"{agent['domain']}.tsv").read_text()))
        parts.append((agent["path"], (self.root / agent["path"]).read_text()))

        # The agent's declared skills, and those skills' category anti-patterns. The skill INDEX is
        # deliberately not loaded: the charter already names its toolkit.
        categories = []
        for name in agent["skills"]:
            skill = self.skills.get(name)
            if skill is None:
                raise SystemExit(f"{agent_id} declares unknown skill '{name}'")
            parts.append((skill["path"], (self.root / skill["path"]).read_text()))
            if skill["category"] not in categories:
                categories.append(skill["category"])
        for category in categories:
            rel = f"skills/antipatterns/{category}.md"
            parts.append((rel, (self.root / rel).read_text()))

        prefix_tokens = sum(tok(body) for _, body in parts)

        # Variable content last.
        variable: list[tuple[str, str]] = []
        if context_package is not None:
            variable.append(("context-package", json.dumps(context_package, indent=2)))
        if task:
            variable.append(("task", task))

        total = prefix_tokens + sum(tok(body) for _, body in variable)
        limit = agent["context_budget_tokens"]
        if enforce and total > limit:
            raise BudgetExceeded(
                f"{agent_id}: {total} tokens exceeds its {limit} budget by {total - limit}.\n"
                f"Compact the context package, then escalate to {agent['reports_to']} if still over.\n"
                f"Repeated exceedance is a bloat defect for token-efficiency-analyst, not a reason "
                f"to raise the limit.")

        return {
            "agent": agent_id,
            "tier": agent["tier"],
            "domain": agent["domain"],
            "task_class": agent["task_class"],
            "model": self.resolve_model(agent["task_class"]),
            "escalates_to": self.escalated_model(agent["task_class"]),
            "profile": self.profile_name,
            "cacheable_prefix_tokens": prefix_tokens,
            "variable_tokens": total - prefix_tokens,
            "total_tokens": total,
            "context_budget": limit,
            "headroom": limit - total,
            "return_budget": agent["return_budget_tokens"],
            "parts": [{"source": src, "tokens": tok(body)} for src, body in parts + variable],
            "text": "\n\n".join(body for _, body in parts + variable),
        }

    # ---- return validation -----------------------------------------------------------------
    def validate_return(self, payload: dict) -> list[str]:
        """Check an agent's return against the contract. Returns a list of problems; empty is good."""
        schema = json.loads((self.root / "knowledge-schema" /
                             "agent-return.schema.json").read_text())
        problems = []
        for field in schema["required"]:
            if field not in payload:
                problems.append(f"missing required field '{field}'")
        agent = self.agents.get(payload.get("agent"))
        if agent is None:
            problems.append(f"unknown agent '{payload.get('agent')}'")
        else:
            summary_tokens = tok(payload.get("summary", ""))
            if summary_tokens > agent["return_budget_tokens"]:
                problems.append(
                    f"summary is {summary_tokens} tokens, over the "
                    f"{agent['return_budget_tokens']} return budget — summarise and point at the "
                    f"artifact instead")
        grade = payload.get("confidence")
        grades = schema["properties"]["confidence"]["enum"]
        if grade not in grades:
            problems.append(f"confidence '{grade}' is not one of {grades}")
        for key in ("artifacts",):
            for item in payload.get(key, []):
                if "\n" in str(item) or len(str(item)) > 300:
                    problems.append(f"{key} must contain paths, not contents")
        return problems

    @staticmethod
    def _tsv(path: pathlib.Path) -> list[list[str]]:
        return [line.split("\t") for line in path.read_text().splitlines()
                if line and not line.startswith("#")]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", help="model profile to resolve tiers through")
    sub = ap.add_subparsers(dest="command", required=True)

    sub.add_parser("domains", help="tier-1: list domains and what each owns")
    p_agents = sub.add_parser("agents", help="tier-1: list the agents in one domain")
    p_agents.add_argument("--domain", required=True)
    p_asm = sub.add_parser("assemble", help="tier-2: build one agent's full context")
    p_asm.add_argument("--agent", required=True)
    p_asm.add_argument("--task", default="")
    p_asm.add_argument("--context", help="path to a context-package JSON file")
    p_asm.add_argument("--out", help="write the assembled context here")
    p_asm.add_argument("--no-enforce", action="store_true", help="report over-budget instead of failing")
    p_val = sub.add_parser("validate-return", help="check an agent return against the contract")
    p_val.add_argument("--file", required=True)
    args = ap.parse_args()

    org = Organisation(profile=args.profile)

    if args.command == "domains":
        print(f"profile: {org.profile_name}")
        print(f"{'domain':<14} {'head':<22} {'n':>3}  owns")
        for d in org.domains():
            print(f"{d['domain']:<14} {d['head']:<22} {d['agents']:>3}  {d['owns'][:70]}")
        return 0

    if args.command == "agents":
        rows = org.agents_in(args.domain)
        print(f"{args.domain}: {len(rows)} agents "
              f"(tier-1 discovery cost {org.tier1_cost(args.domain)} tok)")
        for a in rows:
            print(f"  {a['id']:<32} {a['tier']:<11} {a['capability'][:60]}")
        return 0

    if args.command == "assemble":
        ctx = json.loads(pathlib.Path(args.context).read_text()) if args.context else None
        try:
            result = org.assemble(args.agent, args.task, ctx, enforce=not args.no_enforce)
        except BudgetExceeded as exc:
            print(f"BUDGET EXCEEDED\n{exc}", file=sys.stderr)
            return 1
        print(f"agent            {result['agent']}  ({result['tier']}, {result['domain']})")
        print(f"task_class       {result['task_class']}")
        print(f"model            {result['model']}   [profile: {result['profile']}]")
        print(f"escalates to     {result['escalates_to']}")
        print(f"cacheable prefix {result['cacheable_prefix_tokens']:>7} tok")
        print(f"variable         {result['variable_tokens']:>7} tok")
        print(f"total            {result['total_tokens']:>7} tok  "
              f"(budget {result['context_budget']}, headroom {result['headroom']})")
        print(f"return budget    {result['return_budget']:>7} tok")
        print("\ncomposition:")
        for part in result["parts"]:
            print(f"  {part['tokens']:>6} tok  {part['source']}")
        if args.out:
            pathlib.Path(args.out).write_text(result["text"])
            print(f"\nassembled context written to {args.out}")
        return 0

    if args.command == "validate-return":
        payload = json.loads(pathlib.Path(args.file).read_text())
        problems = org.validate_return(payload)
        if problems:
            print("INVALID RETURN:")
            for p in problems:
                print(f"  - {p}")
            return 1
        print("valid return")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
