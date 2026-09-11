---
name: tax-handling-review
category: finance
description: "Check that the system applies the tax logic correctly in practice."
output: "tax-review.md"
used_by:
  - billing-systems-designer
---

# Tax Handling Review

`finance` · produces `tax-review.md` · used by `billing-systems-designer`

Check that the system applies the tax logic correctly in practice.

## Procedure
1. Sample transactions across jurisdictions and customer types.
2. Recompute the expected treatment independently.
3. Investigate every mismatch, including the ones in our favour.
4. Check that evidence for zero-rating or exemption is actually captured.
5. Report gaps with the specific correction needed.

## Output contract
`tax-review.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Sample spans jurisdictions and customer types
- Exemption evidence verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
