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

    # A realistic single run: discovery, then one charter, then that agent's declared skills.
    per_agent_run = []
    for a in registry:
        t1 = domains_idx + agent_shards[a["domain"]] + median_shard
        t2 = agent_tok[a["id"]] + sum(skill_tok.get(s, 0) for s in a["skills"])
        per_agent_run.append(t1 + t2)
    median_run = int(statistics.median(per_agent_run))
    worst_run = max(per_agent_run)

    base_prompts = sum(file_tok(p) for p in (ROOT / "prompts" / "system").glob("*.md"))

    print("=" * 72)
    print("Context cost of the ai-system organisation (estimated, 4 chars/token)")
    print("=" * 72)
    print(f"  agents:                      {len(registry):>8}")
    print(f"  skills:                      {len(skills):>8}")
    print(f"  median agent charter:        {median_agent:>8} tok")
    print(f"  median SKILL.md:             {median_skill:>8} tok")
    print()
    print("Strategy A — load everything (what a naive runtime would do):")
    print(f"  all charters + all skills:   {naive:>8} tok")
    print()
    print("Strategy B — three-tier progressive disclosure (what this system specifies):")
    print(f"  tier 1  domain index:        {domains_idx:>8} tok")
    print(f"  tier 1  one agent shard:     {int(statistics.median(agent_shards.values())):>8} tok "
          f"(median; largest is {max(agent_shards.values())})")
    print(f"  tier 1  one skill shard:     {median_shard:>8} tok (median; largest is {biggest_shard})")
    print(f"  tier 2  one charter:         {median_agent:>8} tok")
    print(f"  tier 2  that agent's skills: {median_run - cards - median_shard - median_agent:>8} tok")
    print(f"  ---------------------------------------")
    print(f"  median single-agent run:     {median_run:>8} tok")
    print(f"  worst-case single-agent run: {worst_run:>8} tok")
    print()
    print(f"  reduction vs. strategy A:    {100 * (1 - median_run / naive):>7.1f}%")
    print(f"  ratio:                       {naive / median_run:>7.1f}x cheaper per run")
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
