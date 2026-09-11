---
name: cap-table-reconciliation
category: finance
description: "Make the cap table match the signed documents exactly."
output: "cap-table-reconciliation.md"
used_by:
  - cap-table-steward
  - corporate-secretary-agent
---

# Cap Table Reconciliation

`finance` · produces `cap-table-reconciliation.md` · used by `cap-table-steward`, `corporate-secretary-agent`

Make the cap table match the signed documents exactly.

## Procedure
1. List every equity instrument and locate its signed document.
2. Verify share counts, dates, prices, and vesting terms against the document.
3. Reconcile option grants against board approvals.
4. Resolve every discrepancy before the table is used for any decision.
5. Record the reconciliation date and the version certified.

## Output contract
`cap-table-reconciliation.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Every line matched to a signed document
- Discrepancies resolved before use
- The output states its confidence grade and names the evidence behind every load-bearing claim.
