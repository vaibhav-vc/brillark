---
name: retrospective-facilitation
category: orchestration
description: "Run a cycle review that changes behaviour instead of producing notes."
output: "retrospective.md"
used_by:
  - orchestration-head
  - retrospective-agent
---

# Retrospective Facilitation

**Category:** `orchestration` · **Output artifact:** `retrospective.md`

## What this skill does
Run a cycle review that changes behaviour instead of producing notes.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `orchestration-head`, `retrospective-agent`.

## Procedure
1. Open by verifying whether last cycle's actions were actually implemented.
2. Establish what happened factually before discussing why.
3. Separate what worked from what did not, with equal rigour on both.
4. Convert each lesson into one specific artifact change with an owner and a date.
5. Close by recording which lessons go to the recurring-flaw register.

## Output contract
Write `retrospective.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** retrospective-facilitation
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
- Prior actions verified first
- Every lesson becomes an owned artifact change
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
