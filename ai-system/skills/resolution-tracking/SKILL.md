---
name: resolution-tracking
category: orchestration
description: "Follow escalations and blockers through to an actual outcome."
output: "resolution-log.md"
used_by:
  - escalation-manager
---

# Resolution Tracking

**Category:** `orchestration` · **Output artifact:** `resolution-log.md`

## What this skill does
Follow escalations and blockers through to an actual outcome.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `escalation-manager`.

## Procedure
1. Record every escalation with an owner, a deadline, and the decision requested.
2. Chase before the deadline, not after it.
3. Record the outcome and the date, including 'decided not to act'.
4. Close only on evidence of resolution, never on elapsed time.
5. Report items that missed their deadline to the next level up.

## Output contract
Write `resolution-log.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** resolution-tracking
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
- Closure requires evidence
- Missed deadlines escalated automatically
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
