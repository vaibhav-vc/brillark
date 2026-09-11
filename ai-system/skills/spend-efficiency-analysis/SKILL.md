---
name: spend-efficiency-analysis
category: finance
description: "Rank spend by what it produces, and cut the worst."
output: "spend-efficiency.md"
used_by:
  - burn-runway-analyst
  - cost-optimization-analyst
---

# Spend Efficiency Analysis

`finance` · produces `spend-efficiency.md` · used by `burn-runway-analyst`, `cost-optimization-analyst`

Rank spend by what it produces, and cut the worst.

## Procedure
1. Attribute output to spend at the category level.
2. Compute output per unit of cash for each category.
3. Rank and identify the bottom quartile.
4. Distinguish investments with delayed returns from genuine waste.
5. Recommend cuts with the expected output loss stated honestly.

## Output contract
`spend-efficiency.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Delayed-return spend distinguished from waste
- Expected output loss stated for each cut
- The output states its confidence grade and names the evidence behind every load-bearing claim.
