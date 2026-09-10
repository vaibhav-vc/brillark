---
name: decision-request-framing
category: orchestration
description: "Escalate a problem as a decision someone can actually make."
output: "decision-request.md"
used_by:
  - escalation-manager
---

# Decision Request Framing

**Category:** `orchestration` · **Output artifact:** `decision-request.md`

## What this skill does
Escalate a problem as a decision someone can actually make.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `escalation-manager`.

## Procedure
1. State the decision being requested in one sentence.
2. Give the two or three viable options, not an open question.
3. State your recommendation and your confidence in it.
4. Provide the minimum context needed to decide without further reading.
5. State the deadline and what happens by default if no decision arrives.

## Output contract
Write `decision-request.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** decision-request-framing
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
- Options provided, not an open question
- Default-if-no-decision stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
