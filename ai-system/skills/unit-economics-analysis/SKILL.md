---
name: unit-economics-analysis
category: finance
description: "Determine whether one unit of the business makes money, line by line."
output: "unit-economics.md"
used_by:
  - finance-head
  - unit-economics-architect
---

# Unit Economics Analysis

**Category:** `finance` · **Output artifact:** `unit-economics.md`

## What this skill does
Determine whether one unit of the business makes money, line by line.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `finance-head`, `unit-economics-architect`.

## Procedure
1. Define the unit precisely and defend the choice; ambiguity here corrupts everything downstream.
2. Build the revenue side per unit: price, frequency, and expected lifetime.
3. Build the cost stack bottom-up: COGS, delivery, support, payment fees, and infrastructure.
4. Compute contribution margin and payback period from actuals wherever they exist.
5. State how each line behaves at 10x volume and which are truly variable.

## Output contract
Write `unit-economics.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** unit-economics-analysis
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
- Every cost line traced to a source
- Behaviour at scale stated per line
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
