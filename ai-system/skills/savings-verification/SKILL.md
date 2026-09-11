---
name: savings-verification
category: finance
description: "Prove a claimed saving actually appeared in the accounts."
output: "savings-verification.md"
used_by:
  - cost-optimization-analyst
---

# Savings Verification

`finance` · produces `savings-verification.md` · used by `cost-optimization-analyst`

Prove a claimed saving actually appeared in the accounts.

## Procedure
1. Record the claimed saving with its baseline and expected timing.
2. Check the next period's actuals for the specific line.
3. Adjust for volume changes that would have moved the cost anyway.
4. Mark the saving realised, partial, or not realised.
5. Report the realisation rate so future claims can be discounted appropriately.

## Output contract
`savings-verification.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Verified against actuals, not forecasts
- Volume effects adjusted out
- The output states its confidence grade and names the evidence behind every load-bearing claim.
