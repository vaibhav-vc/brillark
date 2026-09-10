---
name: performance-budgeting
category: engineering
description: "Set limits on the performance of critical journeys."
output: "performance-budgets.md"
used_by:
  - performance-engineer
---

# Performance Budgeting

**Category:** `engineering` · **Output artifact:** `performance-budgets.md`

## What this skill does
Set limits on the performance of critical journeys.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `performance-engineer`.

## Procedure
1. Define budgets on user-perceived journeys, not component benchmarks.
2. Set them from user expectation and competitive comparison.
3. Measure the current position honestly, at the tail not the mean.
4. Attribute the budget across the components involved.
5. Review when the journey or the platform changes.

## Output contract
Write `performance-budgets.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** performance-budgeting
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
- Budgets set on user journeys
- Measured at the tail, not the mean
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
