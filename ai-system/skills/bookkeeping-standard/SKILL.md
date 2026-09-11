---
name: bookkeeping-standard
category: finance
description: "Define how transactions are recorded so the books stay auditable."
output: "bookkeeping-standard.md"
used_by:
  - tax-and-compliance-finance
---

# Bookkeeping Standard

`finance` · produces `bookkeeping-standard.md` · used by `tax-and-compliance-finance`

Define how transactions are recorded so the books stay auditable.

## Procedure
1. Define the chart of accounts and what belongs in each.
2. Set the rules for revenue, prepayments, and accruals.
3. Define the documentation required per transaction type.
4. Set the close calendar and its checklist.
5. Define who may post, who reviews, and how corrections are recorded.

## Output contract
`bookkeeping-standard.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Documentation requirement defined per type
- Correction process explicit
- The output states its confidence grade and names the evidence behind every load-bearing claim.
