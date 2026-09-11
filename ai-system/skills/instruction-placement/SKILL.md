---
name: instruction-placement
category: improvement
description: "Put the instruction where it will actually be read."
output: "placement-record.md"
used_by:
  - knowledge-distiller
---

# Instruction Placement

**Category:** `improvement` · **Output artifact:** `placement-record.md`

## What this skill does
Put the instruction where it will actually be read.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-distiller`.

## Procedure
1. Identify the exact moment the agent needs it.
2. Place it in the skill step or guardrail active at that moment.
3. Avoid distant documents that are never loaded at the point of decision.
4. Check the placement is inside the context the agent actually receives.
5. Verify by tracing a real run.

## Output contract
Write `placement-record.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** instruction-placement
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
- Placed inside the context the agent actually receives
- Verified by tracing a real run
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
