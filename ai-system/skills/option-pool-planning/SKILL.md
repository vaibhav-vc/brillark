---
name: option-pool-planning
category: finance
description: "Size the option pool against the actual hiring plan."
output: "option-pool-plan.md"
used_by:
  - cap-table-steward
---

# Option Pool Planning

**Category:** `finance` · **Output artifact:** `option-pool-plan.md`

## What this skill does
Size the option pool against the actual hiring plan.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cap-table-steward`.

## Procedure
1. Build the hiring plan by role and level for the funding period.
2. Assign target equity per role from benchmarks.
3. Sum to the required pool and add a buffer for refreshes and replacements.
4. Model the dilution cost of the pool.
5. Avoid oversizing — unallocated pool is dilution taken early for no reason.

## Output contract
Write `option-pool-plan.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** option-pool-planning
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
- Pool derived from the actual hiring plan
- Dilution cost of the pool stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
