---
name: stage-gate-review
category: orchestration
description: "Decide whether a venture stage is complete and what happens next."
output: "stage-gate-decision.md"
used_by:
  - director
---

# Stage Gate Review

**Category:** `orchestration` · **Output artifact:** `stage-gate-decision.md`

## What this skill does
Decide whether a venture stage is complete and what happens next.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `director`.

## Procedure
1. Assemble the evidence pack the gate requires; refuse to review without it.
2. Check each exit criterion against evidence, not against effort spent.
3. Require the Council verdict before deciding.
4. Decide go, no-go, pivot, or kill in writing, naming the deciding evidence.
5. State what evidence would reverse the decision, and instruct memory consolidation.

## Output contract
Write `stage-gate-decision.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** stage-gate-review
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
- Decision names its deciding evidence
- Reversal condition stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
