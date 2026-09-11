---
name: value-metric-selection
category: finance
description: "Choose the thing the price scales with."
output: "value-metric.md"
used_by:
  - pricing-strategist
---

# Value Metric Selection

`finance` · produces `value-metric.md` · used by `pricing-strategist`

Choose the thing the price scales with.

## Procedure
1. List candidate metrics that correlate with customer value received.
2. Test each for predictability, transparency, and ease of measurement.
3. Check that it grows as the customer succeeds, not as they struggle.
4. Verify the customer can forecast their own bill.
5. Confirm it is measurable in the product before committing.

## Output contract
`value-metric.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Metric grows with customer success
- Customer can forecast their bill
- The output states its confidence grade and names the evidence behind every load-bearing claim.
