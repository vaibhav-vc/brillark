---
name: convertible-conversion-modeling
category: finance
description: "Model what convertible instruments turn into under real terms."
output: "conversion-model.md"
used_by:
  - cap-table-steward
---

# Convertible Conversion Modeling

`finance` · produces `conversion-model.md` · used by `cap-table-steward`

Model what convertible instruments turn into under real terms.

## Procedure
1. List each instrument with its cap, discount, interest, and maturity.
2. Model conversion at the priced round under each instrument's mechanics.
3. Apply the more favourable of cap or discount per instrument, as the terms specify.
4. Show the resulting ownership and the effect on the new investor's stake.
5. Test edge cases: low valuations, high valuations, and a non-qualifying round.

## Output contract
`conversion-model.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Each instrument's mechanics applied individually
- Edge-case valuations tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
