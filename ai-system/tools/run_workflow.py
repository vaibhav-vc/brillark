"""Drive a workflow, enforcing the contract at every step.

The definitions described an orchestrator and nothing implemented one. This does: for each step it
resolves the agent, assembles its context through the loader, records what the step actually cost,
and refuses to advance until the step's artifact exists. It does not call a model — you or your
runtime does that — but it will not let a step be marked done on an artifact that is not there.

    python3 ai-system/tools/run_workflow.py start  --venture acme --workflow 01-business-model-design
    python3 ai-system/tools/run_workflow.py next   --venture acme          # what to do now
    python3 ai-system/tools/run_workflow.py done   --venture acme --step size --tokens 9000
    python3 ai-system/tools/run_workflow.py status --venture acme
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKSPACE = ROOT.parent / "workspace"
sys.path.insert(0, str(ROOT / "tools"))
from loader import Organisation, tok  # noqa: E402


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def run_path(venture: str) -> pathlib.Path:
    return WORKSPACE / venture / "run.json"


def load_run(venture: str) -> dict:
    path = run_path(venture)
    if not path.exists():
        raise SystemExit(f"no run in progress for '{venture}'. Start one with: run_workflow.py start")
    return json.loads(path.read_text())


def save_run(venture: str, run: dict) -> None:
    run_path(venture).write_text(json.dumps(run, indent=2, sort_keys=True))


GRADES = ["guessed", "estimated", "benchmarked", "sourced", "measured"]


def parse_evidence_grades(body: str) -> list[tuple[str, str, bool]]:
    """Pull (claim, grade, load_bearing) out of the artifact's Evidence table.

    A row is load-bearing unless it is explicitly marked otherwise. Conservative on purpose:
    treating an unmarked claim as load-bearing errs toward demanding more evidence, not less.
    """
    rows = []
    section = body.split("## Evidence", 1)
    if len(section) < 2:
        return rows
    for line in section[1].split("##", 1)[0].splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() in ("claim", "---") or set(cells[0]) <= {"-", " "}:
            continue
        grade = cells[-1].lower().strip("*` ")
        if grade not in GRADES:
            continue
        load_bearing = "not load-bearing" not in line.lower()
        rows.append((cells[0], grade, load_bearing))
    return rows


def parse_blocks(body: str) -> dict | None:
    """An artifact may declare that later steps must not proceed on it.

    Without this the orchestrator advances regardless of what a step actually found — which is
    exactly what it did before this existed.
    """
    match = re.search(r"```blocks\n(.*?)```", body, re.S)
    if not match:
        return None
    try:
        declared = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None
    if not isinstance(declared, dict) or not declared.get("blocks"):
        return None
    return declared


def artifact_path(venture: str, org: Organisation, step: dict) -> pathlib.Path:
    """Where the step's output belongs: workspace/<venture>/<category>/<produces>."""
    categories = [org.skills[s]["category"] for s in step["skills"] if s in org.skills]
    category = max(set(categories), key=categories.count) if categories else "artifacts"
    return WORKSPACE / venture / category / step["produces"]


def start(venture: str, workflow: str, org: Organisation) -> int:
    wf = yaml.safe_load((ROOT / "workflows" / f"{workflow}.yaml").read_text())
    if not (WORKSPACE / venture).exists():
        raise SystemExit(f"no workspace for '{venture}'. Run: bash ai-system/bootstrap/init.sh {venture}")
    run = {
        "venture": venture, "workflow": workflow, "name": wf["name"], "owner": wf["owner"],
        "started_at": now(), "exit_criteria": wf["exit_criteria"],
        "steps": [{"id": s["id"], "agent": s["agent"], "skills": s["skills"],
                   "does": s["does"], "produces": s["produces"], "done_when": s["done_when"],
                   "status": "pending"} for s in wf["steps"]],
    }
    save_run(venture, run)
    print(f"started {wf['name']} for {venture} — {len(run['steps'])} steps, owner {wf['owner']}")
    print("next: python3 ai-system/tools/run_workflow.py next --venture " + venture)
    return 0


def next_step(venture: str, org: Organisation, write_context: bool) -> int:
    run = load_run(venture)
    blocks = run.get("blocks", {})
    pending = [s for s in run["steps"] if s["status"] != "done"]
    for s in pending:
        if s["id"] in blocks:
            b = blocks[s["id"]]
            print(f"BLOCKED  {s['id']} — declared by {b['declared_by']}")
            print(f"  reason: {b['reason']}")
            print(f"  resolve via: {', '.join(b.get('resolved_by', [])) or 'unspecified'}\n")
    pending = [s for s in pending if s["id"] not in blocks]
    if not pending and run.get("blocks"):
        print("Every remaining step is blocked. Resolve a block before continuing.")
        return 1
    if not pending:
        print("all steps done. Check the exit criteria:")
        for c in run["exit_criteria"]:
            print(f"  [ ] {c}")
        return 0
    step = pending[0]
    agent = org.agents[step["agent"]]
    assembled = org.assemble(step["agent"], task=step["does"])
    target = artifact_path(venture, org, step)

    print(f"STEP {step['id']}  ({run['steps'].index(step) + 1}/{len(run['steps'])})")
    print(f"  agent        {step['agent']}  [{agent['tier']}, {agent['task_class']}]")
    print(f"  model        {assembled['model']}  (profile {assembled['profile']}, NOT validated)")
    print(f"  skills       {', '.join(step['skills'])}")
    print(f"  does         {step['does']}")
    print(f"  produces     {target.relative_to(WORKSPACE)}")
    print(f"  done when    {step['done_when']}")
    print(f"  context      {assembled['total_tokens']} tok "
          f"(budget {assembled['context_budget']}, headroom {assembled['headroom']})")
    print(f"  returns      <= {assembled['return_budget']} tok")
    if write_context:
        ctx = WORKSPACE / venture / "context" / f"{step['id']}.txt"
        ctx.parent.mkdir(parents=True, exist_ok=True)
        ctx.write_text(assembled["text"])
        print(f"  context written to {ctx.relative_to(WORKSPACE)}")
    return 0


def done(venture: str, step_id: str, org: Organisation, tokens: int | None) -> int:
    run = load_run(venture)
    step = next((s for s in run["steps"] if s["id"] == step_id), None)
    if step is None:
        raise SystemExit(f"no step '{step_id}' in this run")
    target = artifact_path(venture, org, step)
    if not target.exists():
        print(f"REFUSED — {step_id} produces {target.relative_to(WORKSPACE)}, which does not exist.")
        print("A step is done when its artifact exists, not when it feels finished.")
        return 1
    body = target.read_text()
    if len(body) < 200:
        print(f"REFUSED — {target.name} is {len(body)} characters. That is not an artifact.")
        return 1

    problems = []
    for required in ("## Summary", "## Evidence", "## Open questions", "## Next action"):
        if required not in body:
            problems.append(f"missing '{required}' (see skills/OUTPUT_CONTRACT.md)")

    declared = re.search(r"\*\*Confidence:\*\*\s*([a-z]+)", body)
    if not declared:
        problems.append("missing a confidence grade")
    else:
        stated = declared.group(1).lower()
        if stated not in GRADES:
            problems.append(f"confidence '{stated}' is not one of {GRADES}")
        else:
            evidence = parse_evidence_grades(body)
            load_bearing = [(c, g) for c, g, lb in evidence if lb]
            if not evidence:
                problems.append("the Evidence table has no graded rows")
            elif load_bearing:
                weakest_claim, weakest = min(load_bearing, key=lambda cg: GRADES.index(cg[1]))
                if GRADES.index(stated) > GRADES.index(weakest):
                    problems.append(
                        f"confidence '{stated}' overstates the evidence: a load-bearing claim is "
                        f"graded '{weakest}'. OUTPUT_CONTRACT.md rule 5 — confidence is the weakest "
                        f"grade among the claims the conclusion rests on, not the author's mood.\n"
                        f"      weakest load-bearing claim: {weakest_claim[:70]}")
    if problems:
        print(f"REFUSED — {target.name} does not meet the output contract:")
        for p in problems:
            print(f"  - {p}")
        return 1

    blocked_by = run.get("blocks", {})
    if step_id in blocked_by:
        block = blocked_by[step_id]
        print(f"REFUSED — {step_id} is blocked by {block['declared_by']}:")
        print(f"  reason: {block['reason']}")
        print(f"  resolve via: {', '.join(block.get('resolved_by', [])) or 'unspecified'}")
        print("\nClear it deliberately once resolved:")
        print(f"  run_workflow.py unblock --venture {venture} --step {step_id} --evidence '<what changed>'")
        return 1

    step["status"] = "done"
    step["completed_at"] = now()
    step["artifact"] = str(target.relative_to(WORKSPACE))
    step["artifact_tokens"] = tok(body)
    step["run_tokens"] = tokens
    declared_blocks = parse_blocks(body)
    if declared_blocks:
        run.setdefault("blocks", {})
        for blocked in declared_blocks["blocks"]:
            run["blocks"][blocked] = {
                "declared_by": step_id,
                "reason": declared_blocks.get("reason", "unstated"),
                "resolved_by": declared_blocks.get("resolved_by", []),
                "declared_at": now(),
            }
        print(f"  this step BLOCKS: {', '.join(declared_blocks['blocks'])}")
        print(f"  reason: {declared_blocks.get('reason', 'unstated')}")
    save_run(venture, run)

    ledger = WORKSPACE / venture / "telemetry" / "token-ledger" / f"{run['workflow']}-{step_id}.json"
    ledger.parent.mkdir(parents=True, exist_ok=True)
    assembled = org.assemble(step["agent"], task=step["does"])
    ledger.write_text(json.dumps({
        "run_id": f"{run['workflow']}-{step_id}", "agent": step["agent"],
        "task_id": step_id, "model": assembled["model"],
        "tokens": {"system": assembled["cacheable_prefix_tokens"],
                   "context": assembled["variable_tokens"], "retrieved": 0,
                   "output": tok(body),
                   "total": (tokens if tokens else assembled["total_tokens"] + tok(body))},
        "completed": True, "attempts": 1, "escalated": False,
        "budget_exceeded": assembled["headroom"] < 0,
    }, indent=2, sort_keys=True))

    remaining = sum(1 for s in run["steps"] if s["status"] != "done")
    print(f"{step_id} done — {step['artifact']} ({step['artifact_tokens']} tok)")
    print(f"{remaining} step(s) remaining")
    return 0


def unblock(venture: str, step_id: str, evidence: str) -> int:
    run = load_run(venture)
    blocks = run.get("blocks", {})
    if step_id not in blocks:
        print(f"{step_id} is not blocked")
        return 0
    if not evidence:
        raise SystemExit("unblock needs --evidence stating what actually changed")
    cleared = blocks.pop(step_id)
    run.setdefault("cleared_blocks", []).append(
        {**cleared, "step": step_id, "cleared_at": now(), "evidence": evidence})
    save_run(venture, run)
    print(f"{step_id} unblocked. Recorded: {evidence}")
    return 0


def status(venture: str) -> int:
    run = load_run(venture)
    done_n = sum(1 for s in run["steps"] if s["status"] == "done")
    print(f"{run['name']} — {venture}  [{done_n}/{len(run['steps'])} steps]")
    blocks = run.get("blocks", {})
    for s in run["steps"]:
        mark = "x" if s["status"] == "done" else "!" if s["id"] in blocks else " "
        extra = f"  {s.get('artifact', '')}" if s["status"] == "done" else ""
        if s["id"] in blocks:
            extra = f"  BLOCKED by {blocks[s['id']]['declared_by']}: {blocks[s['id']]['reason'][:50]}"
        print(f"  [{mark}] {s['id']:<12} {s['agent']:<32}{extra}")
    if done_n == len(run["steps"]):
        print("\nexit criteria — these are attested, not auto-checked:")
        for c in run["exit_criteria"]:
            print(f"  [ ] {c}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["start", "next", "done", "status", "unblock"])
    ap.add_argument("--venture", required=True)
    ap.add_argument("--workflow")
    ap.add_argument("--step")
    ap.add_argument("--tokens", type=int)
    ap.add_argument("--write-context", action="store_true")
    ap.add_argument("--evidence")
    args = ap.parse_args()
    org = Organisation()

    if args.command == "start":
        if not args.workflow:
            raise SystemExit("start needs --workflow")
        return start(args.venture, args.workflow, org)
    if args.command == "next":
        return next_step(args.venture, org, args.write_context)
    if args.command == "unblock":
        if not args.step:
            raise SystemExit("unblock needs --step")
        return unblock(args.venture, args.step, args.evidence or "")
    if args.command == "done":
        if not args.step:
            raise SystemExit("done needs --step")
        return done(args.venture, args.step, org, args.tokens)
    return status(args.venture)


if __name__ == "__main__":
    raise SystemExit(main())
