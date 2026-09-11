---
name: value-quantification
category: market
description: "Put a number on the value delivered and show the arithmetic."
output: "value-quantification.md"
used_by:
  - value-proposition-designer
---

# Value Quantification

`market` · produces `value-quantification.md` · used by `value-proposition-designer`

Put a number on the value delivered and show the arithmetic.

## Procedure
1. Identify the customer's measurable outcome: time, cost, revenue, or risk.
2. Establish the baseline from the customer's current state.
3. Compute the improvement with conservative assumptions.
4. Show the arithmetic so the customer can check it with their own numbers.
5. Compare the value against the price to show the ratio.

## Output contract
`value-quantification.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Arithmetic shown and checkable
- Conservative assumptions used
- The output states its confidence grade and names the evidence behind every load-bearing claim.
