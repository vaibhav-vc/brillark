---
name: figure-reconciliation
category: finance
description: "Trace every externally reported number to its source before it leaves the building."
output: "reconciliation-trail.md"
used_by:
  - investor-reporting-agent
---

# Figure Reconciliation

**Category:** `finance` · **Output artifact:** `reconciliation-trail.md`

## What this skill does
Trace every externally reported number to its source before it leaves the building.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `investor-reporting-agent`.

## Procedure
1. List every figure appearing in the external document.
2. Trace each to its source system or calculation.
3. Recompute independently and compare.
4. Resolve any difference before publication, not after.
5. Record the reconciliation trail so the figure can be defended later.

## Output contract
Write `reconciliation-trail.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** figure-reconciliation
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
- Every external figure traced
- Differences resolved before publication
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
