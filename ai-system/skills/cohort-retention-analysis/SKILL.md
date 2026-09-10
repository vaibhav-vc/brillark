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

**Category:** `finance` · **Output artifact:** `cohort-analysis.md`

## What this skill does
Understand how customers actually behave over time rather than in aggregate.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `revenue-forecaster`, `unit-economics-architect`.

## Procedure
1. Group customers by acquisition period and track each cohort separately.
2. Plot retention by period since acquisition, not by calendar date.
3. Identify where the curve flattens — that plateau is the real long-term retention.
4. Compare cohorts to detect whether product changes improved retention.
5. Report the sample size per cohort; small cohorts produce confident-looking noise.

## Output contract
Write `cohort-analysis.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cohort-retention-analysis
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
- Curve plateau identified
- Sample sizes reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
