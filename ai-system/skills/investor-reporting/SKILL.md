---
name: investor-reporting
category: finance
description: "Write an investor update that is accurate, consistent, and worth reading."
output: "investor-update.md"
used_by:
  - cfo-agent
  - investor-reporting-agent
---

# Investor Reporting

`finance` · produces `investor-update.md` · used by `cfo-agent`, `investor-reporting-agent`

Write an investor update that is accurate, consistent, and worth reading.

## Procedure
1. Report the same metric set as last period, with the same definitions.
2. Lead with the numbers table, then the narrative.
3. State bad news plainly and early, with the action being taken.
4. Make asks specific: a name, an introduction, or a decision.
5. Reconcile every figure before sending.

## Output contract
`investor-update.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Metric definitions unchanged from prior period
- Asks are specific and actionable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
