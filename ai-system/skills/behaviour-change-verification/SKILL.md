---
name: behaviour-change-verification
category: improvement
description: "Check the instruction actually changed what agents do."
output: "verification-record.md"
used_by:
  - knowledge-distiller
---

# Behaviour Change Verification

**Category:** `improvement` · **Output artifact:** `verification-record.md`

## What this skill does
Check the instruction actually changed what agents do.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-distiller`.

## Procedure
1. Record the behaviour before the instruction was added.
2. Sample runs after the change and check for the behaviour.
3. Distinguish the instruction being followed from the outcome improving.
4. If nothing changed, the instruction is in the wrong place or too vague.
5. Record the verification and act on a null result.

## Output contract
Write `verification-record.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** behaviour-change-verification
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
- Following distinguished from outcome improvement
- Null results acted on, not filed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
