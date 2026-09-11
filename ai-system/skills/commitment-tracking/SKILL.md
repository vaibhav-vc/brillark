---
name: commitment-tracking
category: finance
description: "Track money already promised but not yet paid."
output: "commitments.md"
used_by:
  - burn-runway-analyst
---

# Commitment Tracking

`finance` · produces `commitments.md` · used by `burn-runway-analyst`

Track money already promised but not yet paid.

## Procedure
1. Inventory every signed contract, its term, and its notice period.
2. Record renewal and cancellation dates with the lead time needed to act.
3. Include contingent commitments and their trigger conditions.
4. Include these in runway calculations, not just paid invoices.
5. Alert before each notice-period deadline so renewals are a choice.

## Output contract
`commitments.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Notice periods tracked with lead time
- Commitments included in runway
- The output states its confidence grade and names the evidence behind every load-bearing claim.
