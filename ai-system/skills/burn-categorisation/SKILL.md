---
name: burn-categorisation
category: finance
description: "Show where the money is actually going."
output: "burn-report.md"
used_by:
  - burn-runway-analyst
---

# Burn Categorisation

**Category:** `finance` · **Output artifact:** `burn-report.md`

## What this skill does
Show where the money is actually going.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `burn-runway-analyst`.

## Procedure
1. Split gross burn from net burn; revenue can mask a spending problem.
2. Categorise spend so the top three categories are always visible.
3. Separate one-off from recurring commitments.
4. Compare each category against the prior period and explain movements.
5. Rank categories by output produced per unit of cash.

## Output contract
Write `burn-report.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** burn-categorisation
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
- Gross and net reported separately
- One-off separated from recurring
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
