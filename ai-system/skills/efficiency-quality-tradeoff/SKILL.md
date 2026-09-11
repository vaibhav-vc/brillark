---
name: efficiency-quality-tradeoff
category: efficiency
description: "Decide whether a saving is worth it."
output: "tradeoff-record.md"
used_by:
  - token-efficiency-analyst
---

# Efficiency Quality Tradeoff

`efficiency` · produces `tradeoff-record.md` · used by `token-efficiency-analyst`

Decide whether a saving is worth it.

## Procedure
1. Measure the saving per completed task, not per call.
2. Measure quality on the golden cases before and after.
3. Reject any saving that moves quality below the rubric floor.
4. Account for the cost of extra retries the change causes.
5. Record the trade-off and the decision.

## Output contract
`tradeoff-record.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Retry cost accounted for
- Rubric floor never crossed for savings
- The output states its confidence grade and names the evidence behind every load-bearing claim.
