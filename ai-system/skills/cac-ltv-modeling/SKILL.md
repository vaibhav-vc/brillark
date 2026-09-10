---
name: cac-ltv-modeling
category: finance
description: "Compute what a customer costs to acquire and what they are worth, honestly."
output: "cac-ltv.md"
used_by:
  - unit-economics-architect
---

# CAC LTV Modeling

**Category:** `finance` · **Output artifact:** `cac-ltv.md`

## What this skill does
Compute what a customer costs to acquire and what they are worth, honestly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `unit-economics-architect`.

## Procedure
1. Compute CAC from total acquisition spend divided by customers actually acquired, including salaries.
2. Build LTV from observed cohort retention, not from an assumed churn rate.
3. Cap the LTV horizon conservatively when retention data is thin.
4. Report the ratio and the payback period separately; the ratio alone hides cash timing.
5. Segment by channel — blended numbers conceal both the best and worst channels.

## Output contract
Write `cac-ltv.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cac-ltv-modeling
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
- CAC includes fully loaded spend
- LTV derived from observed cohorts
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
