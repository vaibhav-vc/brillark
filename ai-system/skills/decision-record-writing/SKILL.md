---
name: decision-record-writing
category: orchestration
description: "Capture a decision so a future reader understands why, not just what."
output: "decision-record.md"
used_by:
  - director
---

# Decision Record Writing

**Category:** `orchestration` · **Output artifact:** `decision-record.md`

## What this skill does
Capture a decision so a future reader understands why, not just what.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `director`.

## Procedure
1. State the decision in one sentence, in the active voice.
2. Describe the context and the constraints in force at the time.
3. List the options considered and why each was rejected.
4. State the consequences accepted, including the bad ones.
5. Name the trigger that should cause this decision to be revisited.

## Output contract
Write `decision-record.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** decision-record-writing
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
- Rejected options recorded with reasons
- Revisit trigger named
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
