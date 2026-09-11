---
name: price-testing
category: finance
description: "Change price in a way that produces evidence rather than damage."
output: "price-test.md"
used_by:
  - pricing-strategist
---

# Price Testing

`finance` · produces `price-test.md` · used by `pricing-strategist`

Change price in a way that produces evidence rather than damage.

## Procedure
1. Define the hypothesis and the metric that decides it.
2. Test on new customers first to avoid damaging existing relationships.
3. Run long enough to see the retention effect, not just conversion.
4. Measure revenue per visitor, not conversion rate alone.
5. Decide on the pre-agreed criterion and record the outcome either way.

## Output contract
`price-test.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Retention effect measured, not just conversion
- Decision made on the pre-agreed criterion
- The output states its confidence grade and names the evidence behind every load-bearing claim.
