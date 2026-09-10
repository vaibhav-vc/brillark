---
name: funnel-modeling
category: finance
description: "Model the path from first contact to paying customer with real conversion rates."
output: "funnel-model.md"
used_by:
  - revenue-forecaster
---

# Funnel Modeling

**Category:** `finance` · **Output artifact:** `funnel-model.md`

## What this skill does
Model the path from first contact to paying customer with real conversion rates.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `revenue-forecaster`.

## Procedure
1. Define each funnel stage by an observable event.
2. Measure conversion and time between stages from actual data.
3. Identify the stage with the largest drop and the largest delay.
4. Model how volume at the top translates to revenue at the bottom.
5. Flag stages where the sample is too small for the rate to be trusted.

## Output contract
Write `funnel-model.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** funnel-modeling
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
- Stages defined by observable events
- Small-sample rates flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
