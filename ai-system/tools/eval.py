"""Run the evaluation cases against any model.

This harness imports no provider SDK. You supply a callable; it supplies the contract, the context
assembly, and the scoring structure. That is deliberate — an eval suite coupled to one vendor
measures that vendor, not the organisation.

    python3 ai-system/tools/eval.py --dry-run                 # no model needed; CI runs this
    python3 ai-system/tools/eval.py --list
    python3 ai-system/tools/eval.py --runner mymodule:call
    python3 ai-system/tools/eval.py --runner mymodule:call --exclude-holdout

Your runner:

    def call(prompt: str, model: str) -> str: ...

Scoring is not automated. The harness assembles, runs, and records; a human or a judge model scores
against evals/rubric.yaml. Automating the score with the same model that produced the output is how
an eval suite quietly starts measuring nothing.
"""
from __future__ import annotations

import argparse
import importlib
import json
import pathlib
import sys
import time

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from loader import Organisation, BudgetExceeded, tok  # noqa: E402

CASES = ROOT / "evals" / "cases"
RUBRIC = ROOT / "evals" / "rubric.yaml"


def load_cases(exclude_holdout: bool = False) -> list[dict]:
    cases = [yaml.safe_load(p.read_text()) for p in sorted(CASES.glob("*.yaml"))]
    if exclude_holdout:
        cases = [c for c in cases if not c.get("holdout")]
    return cases


def resolve_runner(spec: str):
    if ":" not in spec:
        raise SystemExit("--runner must look like module:function, e.g. mymodule:call")
    module_name, func_name = spec.split(":", 1)
    try:
        module = importlib.import_module(module_name)
    except ImportError as exc:
        raise SystemExit(f"could not import '{module_name}': {exc}")
    fn = getattr(module, func_name, None)
    if not callable(fn):
        raise SystemExit(f"'{module_name}.{func_name}' is not callable")
    return fn


def validate(org: Organisation, cases: list[dict]) -> list[str]:
    """Everything checkable without a model. This is what CI runs."""
    problems = []
    rubric = yaml.safe_load(RUBRIC.read_text())

    if not rubric.get("dimensions"):
        problems.append("rubric has no dimensions")
    for name, dim in rubric.get("dimensions", {}).items():
        if not dim.get("what"):
            problems.append(f"rubric dimension '{name}' does not say what it measures")
        levels = dim.get("levels", {})
        if set(levels) != {0, 1, 2, 3}:
            problems.append(f"rubric dimension '{name}' must anchor levels 0-3, has {sorted(levels)}")
        for level, anchor in levels.items():
            if not anchor or len(str(anchor)) < 20:
                problems.append(f"rubric '{name}' level {level} is not anchored concretely")

    seen = set()
    for case in cases:
        cid = case.get("id")
        if not cid:
            problems.append("a case has no id")
            continue
        if cid in seen:
            problems.append(f"duplicate case id '{cid}'")
        seen.add(cid)
        for field in ("agent", "task", "tests", "must"):
            if not case.get(field):
                problems.append(f"{cid}: missing '{field}'")
        if case.get("agent") not in org.agents:
            problems.append(f"{cid}: unknown agent '{case.get('agent')}'")
            continue
        if not case.get("must_not"):
            problems.append(f"{cid}: no 'must_not' — a case that cannot fail teaches nothing")
        try:
            org.assemble(case["agent"], case["task"])
        except BudgetExceeded as exc:
            problems.append(f"{cid}: context does not fit the agent's budget — {exc}")
        except SystemExit as exc:
            problems.append(f"{cid}: could not assemble — {exc}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runner", help="module:function that takes (prompt, model) and returns text")
    ap.add_argument("--profile", help="model profile to resolve task classes through")
    ap.add_argument("--dry-run", action="store_true", help="validate the suite without a model")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--exclude-holdout", action="store_true",
                    help="use while tuning; holdout cases must stay unseen")
    ap.add_argument("--case", action="append", help="run only these case ids")
    ap.add_argument("--out", help="write results JSON here")
    args = ap.parse_args()

    org = Organisation(profile=args.profile)
    cases = load_cases(args.exclude_holdout)
    if args.case:
        cases = [c for c in cases if c["id"] in set(args.case)]
        if not cases:
            raise SystemExit("no cases matched --case")

    if args.list:
        print(f"{len(cases)} cases (profile: {org.profile_name})")
        for c in cases:
            agent = org.agents.get(c["agent"], {})
            mark = "holdout" if c.get("holdout") else "tuning "
            print(f"  [{mark}] {c['id']:<32} {c['agent']:<32} "
                  f"{agent.get('task_class', '?'):<11} {c['tests'][:50]}")
        return 0

    if args.dry_run or not args.runner:
        problems = validate(org, load_cases())
        if problems:
            print("SUITE INVALID:")
            for p in problems:
                print(f"  - {p}")
            return 1
        total = len(load_cases())
        holdout = sum(1 for c in load_cases() if c.get("holdout"))
        print(f"suite valid: {total} cases ({holdout} holdout, {total - holdout} tuning), "
              f"rubric anchored across 4 dimensions")
        print(f"every case assembles within its agent's budget under profile '{org.profile_name}'")
        if not args.runner:
            print("\nNo --runner supplied, so nothing was executed. "
                  "Supply one to actually measure a model.")
        return 0

    runner = resolve_runner(args.runner)
    results = []
    print(f"running {len(cases)} cases against runner '{args.runner}' "
          f"(profile: {org.profile_name})\n")
    for case in cases:
        assembled = org.assemble(case["agent"], case["task"])
        started = time.time()
        try:
            output = runner(assembled["text"], assembled["model"])
            error = None
        except Exception as exc:  # a runner failure is a result, not a crash
            output, error = "", f"{type(exc).__name__}: {exc}"
        elapsed = time.time() - started
        results.append({
            "case": case["id"], "agent": case["agent"], "holdout": bool(case.get("holdout")),
            "model": assembled["model"], "prompt_tokens": assembled["total_tokens"],
            "output_tokens": tok(output), "seconds": round(elapsed, 2),
            "error": error, "output": output,
            "must": case["must"], "must_not": case.get("must_not", []),
            "scores": {k: None for k in yaml.safe_load(RUBRIC.read_text())["dimensions"]},
        })
        status = "ERROR" if error else f"{tok(output):>5} tok"
        print(f"  {case['id']:<34} {status}  {elapsed:>5.1f}s")

    out = pathlib.Path(args.out) if args.out else ROOT / "evals" / "last-run.json"
    out.write_text(json.dumps({"profile": org.profile_name, "results": results},
                              indent=2, sort_keys=True))
    errors = sum(1 for r in results if r["error"])
    print(f"\nresults written to {out}")
    print(f"{len(results)} cases run, {errors} runner errors")
    print("Scores are unset. Score against evals/rubric.yaml — a model scoring its own output "
          "measures agreement, not quality.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
