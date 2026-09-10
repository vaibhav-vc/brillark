---
name: code-health-metrics
category: engineering
description: "Measure whether the codebase is getting easier or harder to change."
output: "code-health-report.md"
used_by:
  - tech-debt-refactor-agent
---

# Code Health Metrics

**Category:** `engineering` · **Output artifact:** `code-health-report.md`

## What this skill does
Measure whether the codebase is getting easier or harder to change.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tech-debt-refactor-agent`.

## Procedure
1. Track change lead time and defect density by area.
2. Identify files and modules with disproportionate churn and defects.
3. Measure test coverage where it correlates with defect rate, not as an end.
4. Report the trend, not the absolute value.
5. Use the metrics to target refactoring, never to rank people.

## Output contract
Write `code-health-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** code-health-metrics
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
- Trend reported rather than absolutes
- Metrics used for targeting, not ranking
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
