---
name: option-pool-planning
category: finance
description: "Size the option pool against the actual hiring plan."
output: "option-pool-plan.md"
used_by:
  - cap-table-steward
---

# Option Pool Planning

`finance` · produces `option-pool-plan.md` · used by `cap-table-steward`

Size the option pool against the actual hiring plan.

## Procedure
1. Build the hiring plan by role and level for the funding period.
2. Assign target equity per role from benchmarks.
3. Sum to the required pool and add a buffer for refreshes and replacements.
4. Model the dilution cost of the pool.
5. Avoid oversizing — unallocated pool is dilution taken early for no reason.

## Output contract
`option-pool-plan.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Pool derived from the actual hiring plan
- Dilution cost of the pool stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
