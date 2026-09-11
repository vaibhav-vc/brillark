---
name: survival-analysis
category: finance
description: "State the minimum performance required to avoid failure."
output: "survival-requirements.md"
used_by:
  - scenario-stress-tester
---

# Survival Analysis

`finance` · produces `survival-requirements.md` · used by `scenario-stress-tester`

State the minimum performance required to avoid failure.

## Procedure
1. Define failure concretely: cash exhausted, covenant breached, or commitment missed.
2. Work backwards to the minimum revenue, retention, and cost levels that avoid it.
3. Compare the minimum against current performance and the trend.
4. State the margin of safety in months, not percentages.
5. Define the trigger point at which contingency plans activate.

## Output contract
`survival-requirements.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Failure defined concretely
- Margin of safety stated in time
- The output states its confidence grade and names the evidence behind every load-bearing claim.
