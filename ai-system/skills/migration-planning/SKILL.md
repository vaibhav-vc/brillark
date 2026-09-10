---
name: migration-planning
category: engineering
description: "Change a live schema without losing data or availability."
output: "migration-plan.md"
used_by:
  - data-model-designer
---

# Migration Planning

**Category:** `engineering` · **Output artifact:** `migration-plan.md`

## What this skill does
Change a live schema without losing data or availability.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-model-designer`.

## Procedure
1. Define the target state and the intermediate states.
2. Design each step to be backwards compatible with the running code.
3. Plan the backfill separately, with progress tracking and resumability.
4. Define the rollback for each step, or state why it is irreversible.
5. Test on production-shaped data volume before running.

## Output contract
Write `migration-plan.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** migration-planning
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
- Each step backwards compatible
- Rollback defined or irreversibility declared
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
