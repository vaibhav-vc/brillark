---
name: skill-step-revision
category: improvement
description: "Fix the specific step that let the failure through."
output: "step-revision.md"
used_by:
  - skill-refiner
---

# Skill Step Revision

**Category:** `improvement` · **Output artifact:** `step-revision.md`

## What this skill does
Fix the specific step that let the failure through.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `skill-refiner`.

## Procedure
1. Trace the failure to the step that permitted it.
2. Rewrite that step to be concrete and checkable.
3. Check the revision does not contradict adjacent steps.
4. Keep the step count stable; adding steps dilutes all of them.
5. Verify against the golden case that exposed the failure.

## Output contract
Write `step-revision.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** skill-step-revision
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
- Revision targets the permitting step
- Step count kept stable
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
