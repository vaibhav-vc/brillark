---
name: fix-effect-measurement
category: improvement
description: "Measure whether the fix actually helped."
output: "fix-effect.md"
used_by:
  - agent-performance-analyst
---

# Fix Effect Measurement

**Category:** `improvement` · **Output artifact:** `fix-effect.md`

## What this skill does
Measure whether the fix actually helped.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `agent-performance-analyst`.

## Procedure
1. Record the baseline before the change, on the same cases.
2. Apply one change at a time so the effect is attributable.
3. Re-measure on the same cases after the change.
4. Check for regressions outside the targeted area.
5. Record the delta, and revert changes that did not deliver.

## Output contract
Write `fix-effect.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** fix-effect-measurement
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
- Baseline recorded before the change
- Non-delivering changes reverted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
