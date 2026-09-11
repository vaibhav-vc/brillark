---
name: fail-fast-resequencing
category: improvement
description: "Move the cheap disconfirming step earlier."
output: "resequencing.md"
used_by:
  - workflow-optimizer
---

# Fail Fast Resequencing

**Category:** `improvement` · **Output artifact:** `resequencing.md`

## What this skill does
Move the cheap disconfirming step earlier.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `workflow-optimizer`.

## Procedure
1. Identify the step most likely to stop the work.
2. Check whether it depends on anything that must come first.
3. Move it as early as its dependencies allow.
4. Measure the work avoided when it fires.
5. Re-check the sequence after each change.

## Output contract
Write `resequencing.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** fail-fast-resequencing
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
- Dependencies verified before moving a step
- Work avoided measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
