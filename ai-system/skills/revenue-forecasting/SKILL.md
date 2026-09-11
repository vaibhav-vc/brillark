---
name: revenue-forecasting
category: finance
description: "Predict revenue with a stated range and a driver behind every number."
output: "revenue-forecast.md"
used_by:
  - revenue-forecaster
---

# Revenue Forecasting

`finance` · produces `revenue-forecast.md` · used by `revenue-forecaster`

Predict revenue with a stated range and a driver behind every number.

## Procedure
1. Forecast bottom-up from funnel volumes and conversion rates.
2. Separate new, expansion, and churned revenue.
3. Use cohort retention rather than blended churn.
4. Produce base, downside, and upside with the assumptions defining each end.
5. Score last period's forecast against actuals and correct the method.

## Output contract
`revenue-forecast.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- New, expansion, and churn separated
- Prior forecast accuracy scored
- The output states its confidence grade and names the evidence behind every load-bearing claim.
