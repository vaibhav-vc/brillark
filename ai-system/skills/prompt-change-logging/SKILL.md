---
name: prompt-change-logging
category: improvement
description: "Keep the history of what changed and what it bought."
output: "prompt-change-log.md"
used_by:
  - prompt-optimizer
---

# Prompt Change Logging

**Category:** `improvement` · **Output artifact:** `prompt-change-log.md`

## What this skill does
Keep the history of what changed and what it bought.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prompt-optimizer`.

## Procedure
1. Record the before and after text of the change.
2. Record the diagnosed failure that motivated it.
3. Record the measured delta and the sample.
4. Record the date and who adopted it.
5. Keep reverted changes in the log with the reason.

## Output contract
Write `prompt-change-log.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prompt-change-logging
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
- Measured delta recorded with each change
- Reverted changes retained with reasons
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
