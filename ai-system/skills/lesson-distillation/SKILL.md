---
name: lesson-distillation
category: improvement
description: "Compress a lesson into the shortest instruction that prevents the failure."
output: "distilled-lesson.md"
used_by:
  - knowledge-distiller
---

# Lesson Distillation

`improvement` · produces `distilled-lesson.md` · used by `knowledge-distiller`

Compress a lesson into the shortest instruction that prevents the failure.

## Procedure
1. State the failure in one sentence.
2. Write the shortest instruction that would have prevented it.
3. Prefer a constraint to an explanation.
4. Check it does not duplicate an existing instruction.
5. Pair it with a removal so total instruction length does not grow.

## Output contract
`distilled-lesson.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Paired with a removal to keep length flat
- Constraint preferred over explanation
- The output states its confidence grade and names the evidence behind every load-bearing claim.
