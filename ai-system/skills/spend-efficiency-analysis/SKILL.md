---
name: spend-efficiency-analysis
category: finance
description: "Rank spend by what it produces, and cut the worst."
output: "spend-efficiency.md"
used_by:
  - burn-runway-analyst
  - cost-optimization-analyst
---

# Spend Efficiency Analysis

**Category:** `finance` · **Output artifact:** `spend-efficiency.md`

## What this skill does
Rank spend by what it produces, and cut the worst.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `burn-runway-analyst`, `cost-optimization-analyst`.

## Procedure
1. Attribute output to spend at the category level.
2. Compute output per unit of cash for each category.
3. Rank and identify the bottom quartile.
4. Distinguish investments with delayed returns from genuine waste.
5. Recommend cuts with the expected output loss stated honestly.

## Output contract
Write `spend-efficiency.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** spend-efficiency-analysis
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
- Delayed-return spend distinguished from waste
- Expected output loss stated for each cut
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
