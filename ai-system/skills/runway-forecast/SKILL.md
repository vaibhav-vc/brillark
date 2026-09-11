---
name: runway-forecast
category: finance
description: "Determine the date the venture runs out of money."
output: "runway.md"
used_by:
  - burn-runway-analyst
  - finance-head
---

# Runway Forecast

`finance` · produces `runway.md` · used by `burn-runway-analyst`, `finance-head`

Determine the date the venture runs out of money.

## Procedure
1. Start from the current cash balance, confirmed against the bank, not the ledger.
2. Project net burn month by month from the hiring plan and committed contracts.
3. Include committed but uninvoiced obligations.
4. Produce the runway date under base and downside cases.
5. Set threshold alerts at 12, 9, and 6 months with pre-agreed actions.

## Output contract
`runway.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Cash balance confirmed at source
- Committed obligations included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
