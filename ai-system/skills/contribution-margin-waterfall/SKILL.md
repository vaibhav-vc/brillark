---
name: contribution-margin-waterfall
category: finance
description: "Show exactly where revenue per unit is consumed before it becomes margin."
output: "margin-waterfall.md"
used_by:
  - unit-economics-architect
---

# Contribution Margin Waterfall

**Category:** `finance` · **Output artifact:** `margin-waterfall.md`

## What this skill does
Show exactly where revenue per unit is consumed before it becomes margin.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `unit-economics-architect`.

## Procedure
1. Start from gross revenue per unit.
2. Subtract each cost category in order of size, largest first.
3. Label every step with its source and whether it is fixed or variable.
4. Show the residual contribution margin in both currency and percentage.
5. Highlight the two steps whose improvement would matter most.

## Output contract
Write `margin-waterfall.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contribution-margin-waterfall
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
- Steps ordered by size with sources
- Fixed vs variable labelled per step
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
