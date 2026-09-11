"""Benchmark the organisation's context cost, and fail when it regresses.

Unlike measure_context_cost.py, which reports, this asserts. It computes a fixed set of metrics,
compares them against a committed baseline, and exits non-zero when any metric has got worse by
more than its tolerance. Run it in CI so the library cannot quietly become expensive.

    python3 ai-system/tests/benchmark.py                 # run and compare to baseline
    python3 ai-system/tests/benchmark.py --repeat 20     # confirm the measurement is stable
    python3 ai-system/tests/benchmark.py --json          # machine-readable output
    python3 ai-system/tests/benchmark.py --update-baseline   # accept the current numbers

Token counts are estimates at 4 characters per token. They are a consistent yardstick for
comparing revisions of this repository against each other, which is what a regression gate needs.
They are not a tokeniser and not a bill.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import statistics
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASELINE = pathlib.Path(__file__).resolve().parent / "benchmark-baseline.json"
CHARS_PER_TOKEN = 4

# metric -> (direction, tolerance). "lower" means smaller is better.
# Tolerance is fractional: 0.05 allows a 5% regression before failing.
METRICS = {
    "routed_run_median": ("lower", 0.05),
    "routed_run_p90": ("lower", 0.05),
    "routed_run_max": ("lower", 0.05),
    "composed_run_median": ("lower", 0.05),
    "tier1_routing_max": ("lower", 0.05),
    "workflow_cost_median": ("informational", None),
    "workflow_cost_max": ("informational", None),
    "workflow_step_cost_max": ("lower", 0.05),
    "workflow_steps_max": ("informational", None),
    "median_charter": ("lower", 0.05),
    "median_skill": ("lower", 0.05),
    "naive_total": ("informational", None),
    "agents": ("informational", None),
    "skills": ("informational", None),
    "budget_violations": ("exact", 0),
    "orphan_skills": ("exact", 0),
}


def tok(text: str) -> int:
    return len(text) // CHARS_PER_TOKEN


def ftok(path: pathlib.Path) -> int:
    return tok(path.read_text(encoding="utf-8"))


def percentile(values, pct):
    ordered = sorted(values)
    idx = min(int(round((pct / 100) * (len(ordered) - 1))), len(ordered) - 1)
    return ordered[idx]


def collect() -> dict:
    registry = yaml.safe_load((ROOT / "agents" / "registry.yaml").read_text())["agents"]
    skills = yaml.safe_load((ROOT / "skills" / "registry.yaml").read_text())["skills"]
    skill_cat = {s["name"]: s["category"] for s in skills}

    agent_tok = {a["id"]: ftok(ROOT / a["path"]) for a in registry}
    skill_tok = {s["name"]: ftok(ROOT / s["path"]) for s in skills}
    by_id = {a["id"]: a for a in registry}

    domains_idx = ftok(ROOT / "agents" / "index" / "_domains.tsv")
    agent_shards = {p.stem: ftok(p) for p in (ROOT / "agents" / "index").glob("*.tsv")
                    if not p.stem.startswith("_")}
    skill_shards = {p.stem: ftok(p) for p in (ROOT / "skills" / "index").glob("*.tsv")
                    if not p.stem.startswith("_")}
    antipattern = {p.stem: ftok(p) for p in (ROOT / "skills" / "antipatterns").glob("*.md")}

    def activation(agent) -> int:
        """Tier 2: the charter, its declared skills, and those skills' category anti-patterns."""
        cats = {skill_cat[s] for s in agent["skills"] if s in skill_cat}
        return (agent_tok[agent["id"]]
                + sum(skill_tok.get(s, 0) for s in agent["skills"])
                + sum(antipattern.get(c, 0) for c in cats))

    routed, composed = {}, {}
    for a in registry:
        base = domains_idx + agent_shards[a["domain"]] + activation(a)
        routed[a["id"]] = base
        composed[a["id"]] = base + statistics.median(skill_shards.values())

    # Worst tier-1 routing: domain index + the largest domain shard + the largest skill shard.
    tier1_max = domains_idx + max(agent_shards.values()) + max(skill_shards.values())

    # End-to-end workflow cost: every step pays tier 1 + tier 2 for its agent. Charters and skills
    # repeated across steps are counted once, since a session caches them.
    workflow_cost, workflow_step_cost, workflow_steps = {}, {}, {}
    for path in sorted((ROOT / "workflows").glob("*.yaml")):
        wf = yaml.safe_load(path.read_text())
        seen_agents, seen_skills, seen_cats, domains = set(), set(), set(), set()
        for step in wf["steps"]:
            seen_agents.add(step["agent"])
            domains.add(by_id[step["agent"]]["domain"])
            for s in step["skills"]:
                seen_skills.add(s)
                if s in skill_cat:
                    seen_cats.add(skill_cat[s])
        cost = (domains_idx
                + sum(agent_shards[d] for d in domains)
                + sum(agent_tok[a] for a in seen_agents)
                + sum(skill_tok.get(s, 0) for s in seen_skills)
                + sum(antipattern.get(c, 0) for c in seen_cats))
        workflow_cost[path.stem] = cost
        workflow_steps[path.stem] = len(wf["steps"])
        # What one step of this workflow actually loads — this is the number that must fit a budget.
        # Total workflow cost scales with length and is informational; step cost is the real gate.
        workflow_step_cost[path.stem] = max(
            domains_idx + agent_shards[by_id[st["agent"]]["domain"]]
            + agent_tok[st["agent"]]
            + sum(skill_tok.get(sk, 0) for sk in st["skills"])
            + sum(antipattern.get(skill_cat[sk], 0)
                  for sk in {s2 for s2 in st["skills"] if s2 in skill_cat})
            for st in wf["steps"])

    limits = {"director": 25000, "head": 25000, "executive": 20000,
              "council": 20000, "specialist": 15000}
    violations = [a["id"] for a in registry
                  if routed[a["id"]] > min(a["context_budget_tokens"], limits[a["tier"]])]

    referenced = {s for a in registry for s in a["skills"]}
    orphans = sorted({s["name"] for s in skills} - referenced)

    naive = sum(agent_tok.values()) + sum(skill_tok.values())

    return {
        "metrics": {
            "routed_run_median": int(statistics.median(routed.values())),
            "routed_run_p90": int(percentile(list(routed.values()), 90)),
            "routed_run_max": max(routed.values()),
            "composed_run_median": int(statistics.median(composed.values())),
            "tier1_routing_max": tier1_max,
            "workflow_cost_median": int(statistics.median(workflow_cost.values())),
            "workflow_cost_max": max(workflow_cost.values()),
            "workflow_step_cost_max": max(workflow_step_cost.values()),
            "workflow_steps_max": max(workflow_steps.values()),
            "median_charter": int(statistics.median(agent_tok.values())),
            "median_skill": int(statistics.median(skill_tok.values())),
            "naive_total": naive,
            "agents": len(registry),
            "skills": len(skills),
            "budget_violations": len(violations),
            "orphan_skills": len(orphans),
        },
        "detail": {
            "violations": violations,
            "orphans": orphans[:20],
            "workflow_cost": workflow_cost,
            "workflow_step_cost": workflow_step_cost,
            "most_expensive_agents": sorted(routed.items(), key=lambda kv: -kv[1])[:5],
            "ratio_vs_naive": round(naive / statistics.median(routed.values()), 1),
        },
    }


def compare(current: dict, baseline: dict) -> list[str]:
    failures = []
    for name, (direction, tolerance) in METRICS.items():
        now = current[name]
        was = baseline.get(name)
        if was is None or direction == "informational":
            continue
        if direction == "exact":
            if now != tolerance:
                failures.append(f"{name}: {now}, must be {tolerance}")
        elif direction == "lower":
            ceiling = was * (1 + tolerance)
            if now > ceiling:
                failures.append(
                    f"{name}: {now} tok, baseline {was} tok "
                    f"(+{100 * (now / was - 1):.1f}%, tolerance {100 * tolerance:.0f}%)")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeat", type=int, default=1,
                    help="run N times and report spread; the measurement should be deterministic")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--update-baseline", action="store_true")
    args = ap.parse_args()

    runs = [collect() for _ in range(args.repeat)]
    result = runs[-1]
    metrics, detail = result["metrics"], result["detail"]

    if args.repeat > 1:
        unstable = [k for k in metrics
                    if len({r["metrics"][k] for r in runs}) > 1]
        if unstable:
            print(f"NON-DETERMINISTIC across {args.repeat} runs: {unstable}")
            return 1
        print(f"stable across {args.repeat} runs: all {len(metrics)} metrics identical")

    if args.update_baseline:
        BASELINE.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n")
        print(f"baseline written to {BASELINE.relative_to(ROOT.parent)}")
        return 0

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    print("=" * 74)
    print("ai-system context benchmark (estimated tokens, 4 chars/token)")
    print("=" * 74)
    width = max(len(k) for k in metrics)
    baseline = json.loads(BASELINE.read_text()) if BASELINE.exists() else {}
    for name, value in metrics.items():
        was = baseline.get(name)
        if was in (None, 0) or METRICS[name][0] == "exact":
            delta = ""
        else:
            pct = 100 * (value / was - 1)
            delta = f"   baseline {was:>7}  {pct:+6.1f}%"
        print(f"  {name:<{width}}  {value:>9}{delta}")

    print()
    print(f"  ratio vs. loading everything: {detail['ratio_vs_naive']}x cheaper per routed run")
    print()
    print("  most expensive agents to activate:")
    for name, cost in detail["most_expensive_agents"]:
        print(f"    {cost:>6} tok  {name}")
    print()
    print("  most expensive workflows (whole run, charters and skills counted once —")
    print("  informational: this scales with workflow length, not with per-step cost):")
    for name, cost in sorted(detail["workflow_cost"].items(), key=lambda kv: -kv[1])[:5]:
        print(f"    {cost:>6} tok  {name}")
    print()
    print("  heaviest single step in any workflow (this is what must fit a budget):")
    for name, cost in sorted(detail["workflow_step_cost"].items(), key=lambda kv: -kv[1])[:5]:
        print(f"    {cost:>6} tok  {name}")

    if detail["violations"]:
        print(f"\n  BUDGET VIOLATIONS: {detail['violations']}")
    if detail["orphans"]:
        print(f"\n  ORPHAN SKILLS (in the library, referenced by no agent): {detail['orphans']}")

    if not baseline:
        print("\nNo baseline committed. Run with --update-baseline to create one.")
        return 0

    failures = compare(metrics, baseline)
    print()
    if failures:
        print("REGRESSION:")
        for f in failures:
            print(f"  - {f}")
        print("\nEither fix the regression, or accept it deliberately with --update-baseline")
        print("and say why in the commit message.")
        return 1
    print("PASS — no metric regressed beyond its tolerance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
