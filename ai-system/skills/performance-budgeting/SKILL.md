---
name: performance-budgeting
category: engineering
description: "Set limits on the performance of critical journeys."
output: "performance-budgets.md"
used_by:
  - performance-engineer
---

# Performance Budgeting

`engineering` · produces `performance-budgets.md` · used by `performance-engineer`

Set limits on the performance of critical journeys.

## Procedure
1. Define budgets on user-perceived journeys, not component benchmarks.
2. Set them from user expectation and competitive comparison.
3. Measure the current position honestly, at the tail not the mean.
4. Attribute the budget across the components involved.
5. Review when the journey or the platform changes.

## Output contract
`performance-budgets.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Budgets set on user journeys
- Measured at the tail, not the mean
- The output states its confidence grade and names the evidence behind every load-bearing claim.
