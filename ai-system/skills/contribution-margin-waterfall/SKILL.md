---
name: contribution-margin-waterfall
category: finance
description: "Show exactly where revenue per unit is consumed before it becomes margin."
output: "margin-waterfall.md"
used_by:
  - unit-economics-architect
---

# Contribution Margin Waterfall

`finance` · produces `margin-waterfall.md` · used by `unit-economics-architect`

Show exactly where revenue per unit is consumed before it becomes margin.

## Procedure
1. Start from gross revenue per unit.
2. Subtract each cost category in order of size, largest first.
3. Label every step with its source and whether it is fixed or variable.
4. Show the residual contribution margin in both currency and percentage.
5. Highlight the two steps whose improvement would matter most.

## Output contract
`margin-waterfall.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Steps ordered by size with sources
- Fixed vs variable labelled per step
- The output states its confidence grade and names the evidence behind every load-bearing claim.
