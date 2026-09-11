---
name: skill-step-revision
category: improvement
description: "Fix the specific step that let the failure through."
output: "step-revision.md"
used_by:
  - skill-refiner
---

# Skill Step Revision

`improvement` · produces `step-revision.md` · used by `skill-refiner`

Fix the specific step that let the failure through.

## Procedure
1. Trace the failure to the step that permitted it.
2. Rewrite that step to be concrete and checkable.
3. Check the revision does not contradict adjacent steps.
4. Keep the step count stable; adding steps dilutes all of them.
5. Verify against the golden case that exposed the failure.

## Output contract
`step-revision.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Revision targets the permitting step
- Step count kept stable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
