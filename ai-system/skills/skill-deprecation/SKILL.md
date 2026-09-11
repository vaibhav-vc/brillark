---
name: skill-deprecation
category: improvement
description: "Retire a skill without breaking the agents that name it."
output: "deprecation-record.md"
used_by:
  - skill-refiner
---

# Skill Deprecation

**Category:** `improvement` · **Output artifact:** `deprecation-record.md`

## What this skill does
Retire a skill without breaking the agents that name it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `skill-refiner`.

## Procedure
1. Confirm no usage across three cycles and no agent reference remains.
2. Identify the replacement, if any, and the migration.
3. Update every referencing agent in the same change.
4. Run the integrity tests before and after.
5. Record the retirement and its reason.

## Output contract
Write `deprecation-record.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** skill-deprecation
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
- All references updated in the same change
- Integrity tests run before and after
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
