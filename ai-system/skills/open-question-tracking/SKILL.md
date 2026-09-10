---
name: open-question-tracking
category: orchestration
description: "Keep unresolved questions alive across handoffs instead of dropping them."
output: "open-questions.md"
used_by:
  - handoff-coordinator
---

# Open Question Tracking

**Category:** `orchestration` · **Output artifact:** `open-questions.md`

## What this skill does
Keep unresolved questions alive across handoffs instead of dropping them.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `handoff-coordinator`.

## Procedure
1. Capture every open question with the work it affects.
2. Assign an owner and a by-when to each.
3. Carry the list through every handoff without editing it down for tidiness.
4. Close questions with an answer and its source, not with silence.
5. Escalate questions that survive two handoffs unanswered.

## Output contract
Write `open-questions.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** open-question-tracking
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
- Questions survive handoffs intact
- Closure requires a sourced answer
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
