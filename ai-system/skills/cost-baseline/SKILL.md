---
name: cost-baseline
category: finance
description: "Establish what things currently cost before trying to optimise."
output: "cost-baseline.md"
used_by:
  - cost-optimization-analyst
---

# Cost Baseline

**Category:** `finance` · **Output artifact:** `cost-baseline.md`

## What this skill does
Establish what things currently cost before trying to optimise.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cost-optimization-analyst`.

## Procedure
1. Pull twelve months of actual spend by vendor and category.
2. Normalise for one-offs and seasonality.
3. Attribute costs to drivers — per customer, per request, per employee.
4. Identify the largest three lines and their growth rates.
5. Publish the baseline as the reference point for all savings claims.

## Output contract
Write `cost-baseline.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cost-baseline
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
- Costs attributed to drivers
- Baseline published before optimisation begins
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
