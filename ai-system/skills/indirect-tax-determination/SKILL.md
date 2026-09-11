---
name: indirect-tax-determination
category: finance
description: "Decide the VAT, GST, or sales tax treatment per product and market."
output: "indirect-tax-logic.md"
used_by:
  - tax-and-compliance-finance
---

# Indirect Tax Determination

`finance` · produces `indirect-tax-logic.md` · used by `tax-and-compliance-finance`

Decide the VAT, GST, or sales tax treatment per product and market.

## Procedure
1. Classify the product for tax purposes in each market.
2. Determine the place of supply rules that apply.
3. Establish whether the customer's status changes the treatment.
4. Define the evidence needed to support the treatment.
5. Document the logic so the billing system can implement it deterministically.

## Output contract
`indirect-tax-logic.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Place of supply determined per market
- Evidence requirements documented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
