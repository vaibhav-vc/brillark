---
name: switching-analysis
category: market
description: "Understand what it costs a customer to change, and who bears that cost."
output: "switching-analysis.md"
used_by:
  - jtbd-analyst
---

# Switching Analysis

`market` · produces `switching-analysis.md` · used by `jtbd-analyst`

Understand what it costs a customer to change, and who bears that cost.

## Procedure
1. List the switching costs: data migration, retraining, contract, and political risk.
2. Identify who inside the customer bears each cost.
3. Estimate the value gain required to outweigh them.
4. Design a specific reduction for the largest switching cost.
5. Verify against real switching stories rather than assumption.

## Output contract
`switching-analysis.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Switching costs quantified
- Reduction designed for the largest cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.
