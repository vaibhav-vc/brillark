---
name: forecast-accuracy-review
category: finance
description: "Score past forecasts so the method improves rather than the story."
output: "forecast-accuracy.md"
used_by:
  - revenue-forecaster
---

# Forecast Accuracy Review

`finance` · produces `forecast-accuracy.md` · used by `revenue-forecaster`

Score past forecasts so the method improves rather than the story.

## Procedure
1. Compare each past forecast against the actual outcome.
2. Compute error magnitude and direction — persistent optimism is a method defect.
3. Identify which drivers were mis-forecast, not just the total.
4. Adjust the method, and record the adjustment.
5. Publish the accuracy trend alongside every new forecast.

## Output contract
`forecast-accuracy.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Bias direction identified
- Method adjusted and recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
