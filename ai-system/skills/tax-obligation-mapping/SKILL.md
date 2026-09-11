---
name: tax-obligation-mapping
category: finance
description: "Determine what the venture owes, where, and when."
output: "tax-obligations.md"
used_by:
  - tax-and-compliance-finance
---

# Tax Obligation Mapping

`finance` · produces `tax-obligations.md` · used by `tax-and-compliance-finance`

Determine what the venture owes, where, and when.

## Procedure
1. Identify every jurisdiction where a nexus exists, including digital-service rules.
2. Map obligation types: income, indirect, payroll, and filing-only.
3. Record registration requirements and thresholds.
4. Build the deadline calendar with the lead time each filing needs.
5. Flag every item requiring a qualified tax adviser.

## Output contract
`tax-obligations.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Nexus assessed per jurisdiction
- Adviser-grade items flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
