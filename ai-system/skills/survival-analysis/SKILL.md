---
name: survival-analysis
category: finance
description: "State the minimum performance required to avoid failure."
output: "survival-requirements.md"
used_by:
  - scenario-stress-tester
---

# Survival Analysis

**Category:** `finance` · **Output artifact:** `survival-requirements.md`

## What this skill does
State the minimum performance required to avoid failure.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `scenario-stress-tester`.

## Procedure
1. Define failure concretely: cash exhausted, covenant breached, or commitment missed.
2. Work backwards to the minimum revenue, retention, and cost levels that avoid it.
3. Compare the minimum against current performance and the trend.
4. State the margin of safety in months, not percentages.
5. Define the trigger point at which contingency plans activate.

## Output contract
Write `survival-requirements.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** survival-analysis
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
- Failure defined concretely
- Margin of safety stated in time
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
