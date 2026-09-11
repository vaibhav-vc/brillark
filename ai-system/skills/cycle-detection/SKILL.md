---
name: cycle-detection
category: orchestration
description: "Find circular dependencies before they deadlock execution."
output: "cycle-report.md"
used_by:
  - dependency-scheduler
---

# Cycle Detection

`orchestration` · produces `cycle-report.md` · used by `dependency-scheduler`

Find circular dependencies before they deadlock execution.

## Procedure
1. Traverse the graph depth-first, tracking the active path.
2. Report every cycle with the full loop, not just the closing edge.
3. Classify each cycle: genuine mutual need, or accidental over-specification.
4. Propose a break: split a task, stub an interface, or stage the work.
5. Re-run detection after the fix to confirm the graph is acyclic.

## Output contract
`cycle-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Full loops reported, not single edges
- Re-verified acyclic after the break
- The output states its confidence grade and names the evidence behind every load-bearing claim.
