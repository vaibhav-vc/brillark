---
name: critical-path-analysis
category: orchestration
description: "Identify the chain of work that actually determines the finish date."
output: "critical-path.md"
used_by:
  - dependency-scheduler
---

# Critical Path Analysis

`orchestration` · produces `critical-path.md` · used by `dependency-scheduler`

Identify the chain of work that actually determines the finish date.

## Procedure
1. Estimate duration for each task from historical throughput, not optimism.
2. Compute earliest and latest start for every node.
3. Identify the zero-slack chain and mark it as the critical path.
4. Name the single binding constraint on that path.
5. Re-compute whenever a task on the path slips.

## Output contract
`critical-path.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Estimates drawn from actual throughput
- Binding constraint named explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
