---
name: waterfall-analysis
category: finance
description: "Show who gets what in an exit, in what order."
output: "waterfall.md"
used_by:
  - cap-table-steward
---

# Waterfall Analysis

`finance` · produces `waterfall.md` · used by `cap-table-steward`

Show who gets what in an exit, in what order.

## Procedure
1. List every security with its liquidation preference and participation rights.
2. Model the distribution stack in seniority order.
3. Compute proceeds by exit value across a realistic range.
4. Identify the value at which common shareholders receive nothing.
5. Highlight where preference stacking creates a misaligned incentive.

## Output contract
`waterfall.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Distribution modelled across a value range
- Common-zero point identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
