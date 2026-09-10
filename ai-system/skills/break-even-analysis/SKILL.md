---
name: break-even-analysis
category: finance
description: "Find the volume or price at which the business stops losing money."
output: "break-even.md"
used_by:
  - council-economics-skeptic
---

# Break Even Analysis

**Category:** `finance` · **Output artifact:** `break-even.md`

## What this skill does
Find the volume or price at which the business stops losing money.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-economics-skeptic`.

## Procedure
1. Separate fixed from variable costs rigorously.
2. Compute contribution margin per unit.
3. Divide fixed costs by contribution margin to get break-even volume.
4. Show how break-even moves with price, cost, and fixed-base changes.
5. State the time to reach break-even at the current growth rate.

## Output contract
Write `break-even.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** break-even-analysis
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
- Fixed and variable separated rigorously
- Time to break-even stated at current growth
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
