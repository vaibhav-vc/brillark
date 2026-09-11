---
name: cohort-retention-analysis
category: finance
description: "Understand how customers actually behave over time rather than in aggregate."
output: "cohort-analysis.md"
used_by:
  - revenue-forecaster
  - unit-economics-architect
---

# Cohort Retention Analysis

`finance` · produces `cohort-analysis.md` · used by `revenue-forecaster`, `unit-economics-architect`

Understand how customers actually behave over time rather than in aggregate.

## Procedure
1. Group customers by acquisition period and track each cohort separately.
2. Plot retention by period since acquisition, not by calendar date.
3. Identify where the curve flattens — that plateau is the real long-term retention.
4. Compare cohorts to detect whether product changes improved retention.
5. Report the sample size per cohort; small cohorts produce confident-looking noise.

## Output contract
`cohort-analysis.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Curve plateau identified
- Sample sizes reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.
