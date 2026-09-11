---
name: schedule-optimisation
category: orchestration
description: "Improve the schedule without pretending work takes less time than it does."
output: "schedule.md"
used_by:
  - dependency-scheduler
---

# Schedule Optimisation

`orchestration` · produces `schedule.md` · used by `dependency-scheduler`

Improve the schedule without pretending work takes less time than it does.

## Procedure
1. Attack the critical path first; optimising slack changes nothing.
2. Look for tasks that can start on partial inputs rather than complete ones.
3. Rebalance load away from over-committed agents.
4. Add buffer where variance is historically high, not uniformly.
5. Publish the revised schedule with what changed and why.

## Output contract
`schedule.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Only critical-path changes claimed as gains
- Buffers placed by measured variance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
