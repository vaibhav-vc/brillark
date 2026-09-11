---
name: lesson-distillation
category: improvement
description: "Compress a lesson into the shortest instruction that prevents the failure."
output: "distilled-lesson.md"
used_by:
  - knowledge-distiller
---

# Lesson Distillation

**Category:** `improvement` · **Output artifact:** `distilled-lesson.md`

## What this skill does
Compress a lesson into the shortest instruction that prevents the failure.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-distiller`.

## Procedure
1. State the failure in one sentence.
2. Write the shortest instruction that would have prevented it.
3. Prefer a constraint to an explanation.
4. Check it does not duplicate an existing instruction.
5. Pair it with a removal so total instruction length does not grow.

## Output contract
Write `distilled-lesson.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** lesson-distillation
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
- Paired with a removal to keep length flat
- Constraint preferred over explanation
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
