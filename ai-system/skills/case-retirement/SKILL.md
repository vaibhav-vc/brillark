---
name: case-retirement
category: improvement
description: "Remove cases that no longer teach anything."
output: "retirement-log.md"
used_by:
  - benchmark-curator
---

# Case Retirement

**Category:** `improvement` · **Output artifact:** `retirement-log.md`

## What this skill does
Remove cases that no longer teach anything.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `benchmark-curator`.

## Procedure
1. Identify cases every candidate passes across several cycles.
2. Check the case is not passing because the suite is over-tuned to it.
3. Archive rather than delete, so history remains.
4. Replace retired coverage with a harder case in the same area.
5. Record the retirement and its reason.

## Output contract
Write `retirement-log.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** case-retirement
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
- Over-tuning ruled out before retiring
- Retired coverage replaced
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
