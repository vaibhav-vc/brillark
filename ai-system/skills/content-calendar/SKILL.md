---
name: content-calendar
category: gtm
description: "Plan content that serves the funnel rather than filling a schedule."
output: "content-calendar.md"
used_by:
  - cmo-agent
---

# Content Calendar

**Category:** `gtm` · **Output artifact:** `content-calendar.md`

## What this skill does
Plan content that serves the funnel rather than filling a schedule.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cmo-agent`.

## Procedure
1. Map content to funnel stage and to a specific ICP question.
2. Prioritise questions prospects actually ask, sourced from sales and support.
3. Set a cadence the team can sustain, then reduce it by a third.
4. Assign an owner and a review step per piece.
5. Measure by pipeline influence, not by publication count.

## Output contract
Write `content-calendar.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** content-calendar
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
- Every piece answers a real prospect question
- Measured by influence, not volume
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
