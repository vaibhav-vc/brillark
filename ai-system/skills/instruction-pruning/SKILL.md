---
name: instruction-pruning
category: improvement
description: "Remove instructions that no longer earn their tokens."
output: "pruning-record.md"
used_by:
  - knowledge-distiller
---

# Instruction Pruning

**Category:** `improvement` · **Output artifact:** `pruning-record.md`

## What this skill does
Remove instructions that no longer earn their tokens.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-distiller`.

## Procedure
1. Identify instructions that no failure in recent cycles relates to.
2. Identify instructions duplicated across layers.
3. Identify instructions superseded by a newer one.
4. Remove and record, rather than leaving them to dilute the rest.
5. Watch the next cycle for the failure returning, and restore if it does.

## Output contract
Write `pruning-record.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** instruction-pruning
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
- Removals watched for the failure returning
- Duplicated instructions consolidated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
