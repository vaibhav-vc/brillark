---
name: burn-categorisation
category: finance
description: "Show where the money is actually going."
output: "burn-report.md"
used_by:
  - burn-runway-analyst
---

# Burn Categorisation

`finance` · produces `burn-report.md` · used by `burn-runway-analyst`

Show where the money is actually going.

## Procedure
1. Split gross burn from net burn; revenue can mask a spending problem.
2. Categorise spend so the top three categories are always visible.
3. Separate one-off from recurring commitments.
4. Compare each category against the prior period and explain movements.
5. Rank categories by output produced per unit of cash.

## Output contract
`burn-report.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Gross and net reported separately
- One-off separated from recurring
- The output states its confidence grade and names the evidence behind every load-bearing claim.
