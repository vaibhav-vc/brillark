---
name: revenue-forecasting
category: finance
description: "Predict revenue with a stated range and a driver behind every number."
output: "revenue-forecast.md"
used_by:
  - revenue-forecaster
---

# Revenue Forecasting

**Category:** `finance` · **Output artifact:** `revenue-forecast.md`

## What this skill does
Predict revenue with a stated range and a driver behind every number.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `revenue-forecaster`.

## Procedure
1. Forecast bottom-up from funnel volumes and conversion rates.
2. Separate new, expansion, and churned revenue.
3. Use cohort retention rather than blended churn.
4. Produce base, downside, and upside with the assumptions defining each end.
5. Score last period's forecast against actuals and correct the method.

## Output contract
Write `revenue-forecast.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** revenue-forecasting
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- New, expansion, and churn separated
- Prior forecast accuracy scored
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
