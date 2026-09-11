---
name: cac-ltv-modeling
category: finance
description: "Compute what a customer costs to acquire and what they are worth, honestly."
output: "cac-ltv.md"
used_by:
  - unit-economics-architect
---

# CAC LTV Modeling

`finance` · produces `cac-ltv.md` · used by `unit-economics-architect`

Compute what a customer costs to acquire and what they are worth, honestly.

## Procedure
1. Compute CAC from total acquisition spend divided by customers actually acquired, including salaries.
2. Build LTV from observed cohort retention, not from an assumed churn rate.
3. Cap the LTV horizon conservatively when retention data is thin.
4. Report the ratio and the payback period separately; the ratio alone hides cash timing.
5. Segment by channel — blended numbers conceal both the best and worst channels.

## Output contract
`cac-ltv.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- CAC includes fully loaded spend
- LTV derived from observed cohorts
- The output states its confidence grade and names the evidence behind every load-bearing claim.
