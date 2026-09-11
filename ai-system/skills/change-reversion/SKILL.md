---
name: change-reversion
category: improvement
description: "Undo a change that did not hold."
output: "reversion-record.md"
used_by:
  - improvement-head
---

# Change Reversion

**Category:** `improvement` · **Output artifact:** `reversion-record.md`

## What this skill does
Undo a change that did not hold.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `improvement-head`.

## Procedure
1. Check the following cycle whether the measured gain persisted.
2. Compare against the recorded baseline, not against impression.
3. Revert cleanly to the logged previous version.
4. Record why it was reverted so it is not retried identically.
5. Re-open the underlying problem in the improvement queue.

## Output contract
Write `reversion-record.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** change-reversion
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
- Persistence checked in the following cycle
- Underlying problem reopened, not closed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
