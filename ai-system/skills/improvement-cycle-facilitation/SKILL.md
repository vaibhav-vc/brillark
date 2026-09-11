---
name: improvement-cycle-facilitation
category: improvement
description: "Run the loop that makes the organisation better."
output: "cycle-report.md"
used_by:
  - improvement-head
---

# Improvement Cycle Facilitation

**Category:** `improvement` · **Output artifact:** `cycle-report.md`

## What this skill does
Run the loop that makes the organisation better.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `improvement-head`.

## Procedure
1. Open with measurement, never with an idea.
2. Diagnose before proposing; most prompt problems are context problems.
3. Require a held-out trial before any adoption.
4. Adopt one change at a time per agent.
5. Close by verifying last cycle's adoptions actually held.

## Output contract
Write `cycle-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** improvement-cycle-facilitation
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
- Cycle opens with measurement
- Prior adoptions verified at close
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
