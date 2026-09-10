---
name: revenue-plan-decomposition
category: finance
description: "Break a revenue target into drivers someone can own."
output: "revenue-plan.md"
used_by:
  - chief-revenue-officer-agent
---

# Revenue Plan Decomposition

**Category:** `finance` · **Output artifact:** `revenue-plan.md`

## What this skill does
Break a revenue target into drivers someone can own.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-revenue-officer-agent`.

## Procedure
1. Decompose the target into volume, conversion, price, and retention.
2. Assign each driver to one owner.
3. Check the implied numbers for plausibility against current performance.
4. Identify the driver requiring the largest improvement — that is the real plan.
5. Set the leading indicator for each driver.

## Output contract
Write `revenue-plan.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** revenue-plan-decomposition
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
- Every driver has one owner
- Implied improvements checked for plausibility
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
