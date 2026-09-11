---
name: break-even-analysis
category: finance
description: "Find the volume or price at which the business stops losing money."
output: "break-even.md"
used_by:
  - council-economics-skeptic
---

# Break Even Analysis

`finance` · produces `break-even.md` · used by `council-economics-skeptic`

Find the volume or price at which the business stops losing money.

## Procedure
1. Separate fixed from variable costs rigorously.
2. Compute contribution margin per unit.
3. Divide fixed costs by contribution margin to get break-even volume.
4. Show how break-even moves with price, cost, and fixed-base changes.
5. State the time to reach break-even at the current growth rate.

## Output contract
`break-even.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Fixed and variable separated rigorously
- Time to break-even stated at current growth
- The output states its confidence grade and names the evidence behind every load-bearing claim.
