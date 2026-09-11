"""Measure what it costs to put this organisation into a model's context.

The claim the tiered design makes is that a request can be routed and executed without ever
loading the whole library. This script measures that claim instead of asserting it.

Token counts are ESTIMATES using 4 characters per token. They are not a tokeniser. Use them for
comparing strategies against each other, which is what they are for — not for billing.

    python3 ai-system/tests/measure_context_cost.py
"""
from __future__ import annotations

import json
import pathlib
import statistics

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHARS_PER_TOKEN = 4


def tok(text: str) -> int:
    return len(text) // CHARS_PER_TOKEN


def file_tok(path: pathlib.Path) -> int:
    return tok(path.read_text(encoding="utf-8"))


def main() -> int:
    registry = yaml.safe_load((ROOT / "agents" / "registry.yaml").read_text())["agents"]
    skills = yaml.safe_load((ROOT / "skills" / "registry.yaml").read_text())["skills"]
    budget = yaml.safe_load((ROOT / "runtime" / "context-budget.yaml").read_text())

    agent_files = [ROOT / a["path"] for a in registry]
    skill_files = [ROOT / s["path"] for s in skills]

    naive = sum(file_tok(p) for p in agent_files) + sum(file_tok(p) for p in skill_files)

    domains_idx = file_tok(ROOT / "agents" / "index" / "_domains.tsv")
    agent_shards = {p.stem: file_tok(p) for p in (ROOT / "agents" / "index").glob("*.tsv")
                    if not p.stem.startswith("_")}
    skill_shards = {p.stem: file_tok(p) for p in (ROOT / "skills" / "index").glob("*.tsv")
                    if not p.stem.startswith("_")}
    biggest_shard = max(skill_shards.values())
    median_shard = int(statistics.median(skill_shards.values()))
    cards = domains_idx + int(statistics.median(agent_shards.values()))

    agent_tok = {a["id"]: file_tok(ROOT / a["path"]) for a in registry}
    skill_tok = {s["name"]: file_tok(ROOT / s["path"]) for s in skills}
    median_agent = int(statistics.median(agent_tok.values()))
    median_skill = int(statistics.median(skill_tok.values()))

    # Two real paths.
    #   Routed: pick a domain, pick an agent, run it with the skills it already declares.
    #           The skill index is not needed — the charter names its own toolkit.
    #   Composed: the task does not match one agent's toolkit, so skills are discovered too.
    routed, composed = [], []
    for a in registry:
        cats = {sk["category"] for sk in skills if sk["name"] in a["skills"]}
        ap = sum(len((ROOT / "skills" / "antipatterns" / f"{c}.md").read_text()) // 4 for c in cats)
        t2 = agent_tok[a["id"]] + sum(skill_tok.get(s, 0) for s in a["skills"]) + ap
        base = domains_idx + agent_shards[a["domain"]] + t2
        routed.append(base)
        composed.append(base + median_shard)
    per_agent_run = routed
    median_run = int(statistics.median(routed))
    worst_run = max(routed)
    median_composed = int(statistics.median(composed))

    base_prompts = sum(file_tok(p) for p in (ROOT / "prompts" / "system").glob("*.md"))

    print("=" * 72)
    print("Context cost of the ai-system organisation (estimated, 4 chars/token)")
    print("=" * 72)
    print(f"  agents:                      {len(registry):>8}")
    print(f"  skills:                      {len(skills):>8}")
    print(f"  median agent charter:        {median_agent:>8} tok")
    print(f"  median SKILL.md:             {median_skill:>8} tok")
    print()
    print("Strategy A — load everything (a STRAWMAN: no sane runtime does this):")
    print(f"  all charters + all skills:   {naive:>8} tok")
    print()
    print("Strategy A' — the honest baseline: one good general-purpose system prompt")
    print(f"  a well-written 5k prompt:    {5000:>8} tok")
    print()
    print("Strategy B — three-tier progressive disclosure (what this system specifies):")
    print(f"  tier 1  domain index:        {domains_idx:>8} tok")
    print(f"  tier 1  one agent shard:     {int(statistics.median(agent_shards.values())):>8} tok "
          f"(median; largest is {max(agent_shards.values())})")
    print(f"  tier 2  one charter:         {median_agent:>8} tok")
    print(f"  tier 2  skills + antipatterns:"
          f"{median_run - domains_idx - int(statistics.median(agent_shards.values())) - median_agent:>7} tok")
    print(f"  ---------------------------------------")
    print(f"  ROUTED  median run:          {median_run:>8} tok   <- the common path")
    print(f"  ROUTED  worst case:          {worst_run:>8} tok")
    print()
    print(f"  plus one skill shard:        {median_shard:>8} tok (median; largest {biggest_shard})")
    print(f"  COMPOSED median run:         {median_composed:>8} tok   <- when skills must be discovered")
    print()
    print(f"  vs. strategy A (strawman):   {naive / median_run:>7.1f}x cheaper")
    print(f"  vs. strategy A' (realistic): {5000 / median_run:>7.2f}x — i.e. COMPARABLE cost")
    print()
    print("  The honest claim is NOT '80x cheaper'. Against a single well-written system prompt")
    print("  this costs about the same. What tiering buys is that 138 specialised agents stay")
    print("  affordable at the cost of one generalist — capability per token, not raw savings.")
    print()
    print(f"  shared system prompts:       {base_prompts:>8} tok (cacheable prefix, loaded once)")
    print()

    limit = budget["per_agent_tier"]["specialist"]["context"]
    over = [a["id"] for a, t in zip(registry, per_agent_run) if t > limit]
    print(f"Budget check — specialist context limit is {limit} tok:")
    if over:
        print(f"  {len(over)} agent(s) exceed it at tier 1+2 before any task context:")
        for name in over[:10]:
            print(f"    - {name}")
    else:
        print("  no agent exceeds its budget on tier 1 + tier 2 load. "
              "The remainder is available for task context.")
    print()
    print("Note: these are estimates for comparing strategies, not a tokeniser and not a bill.")
    return 1 if over else 0


if __name__ == "__main__":
    raise SystemExit(main())
