---
name: budget-allocation
category: orchestration
description: "Give every task an explicit ceiling on time, tokens, and spend."
output: "budget-allocation.md"
used_by:
  - dependency-scheduler
---

# Budget Allocation

`orchestration` · produces `budget-allocation.md` · used by `dependency-scheduler`

Give every task an explicit ceiling on time, tokens, and spend.

## Procedure
1. Derive the total budget from the stage gate's allowance.
2. Allocate proportionally to expected value, not to requester insistence.
3. Set a hard ceiling per task and the action to take when it is hit.
4. Reserve a contingency pool held by the head, not distributed in advance.
5. Track consumption and report overruns before they compound.

## Output contract
`budget-allocation.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Every task has a hard ceiling
- Contingency held centrally, not pre-spent
- The output states its confidence grade and names the evidence behind every load-bearing claim.
