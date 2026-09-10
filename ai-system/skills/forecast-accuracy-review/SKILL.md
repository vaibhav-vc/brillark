---
name: forecast-accuracy-review
category: finance
description: "Score past forecasts so the method improves rather than the story."
output: "forecast-accuracy.md"
used_by:
  - revenue-forecaster
---

# Forecast Accuracy Review

**Category:** `finance` · **Output artifact:** `forecast-accuracy.md`

## What this skill does
Score past forecasts so the method improves rather than the story.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `revenue-forecaster`.

## Procedure
1. Compare each past forecast against the actual outcome.
2. Compute error magnitude and direction — persistent optimism is a method defect.
3. Identify which drivers were mis-forecast, not just the total.
4. Adjust the method, and record the adjustment.
5. Publish the accuracy trend alongside every new forecast.

## Output contract
Write `forecast-accuracy.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** forecast-accuracy-review
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
- Bias direction identified
- Method adjusted and recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
