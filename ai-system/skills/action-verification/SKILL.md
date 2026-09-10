---
name: action-verification
category: orchestration
description: "Confirm that agreed changes were actually made."
output: "action-verification.md"
used_by:
  - retrospective-agent
---

# Action Verification

**Category:** `orchestration` · **Output artifact:** `action-verification.md`

## What this skill does
Confirm that agreed changes were actually made.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `retrospective-agent`.

## Procedure
1. List the actions agreed in the previous cycle with their owners.
2. Check the artifact each action was supposed to change.
3. Mark each as implemented, partially implemented, or not started — from evidence.
4. Ask why for anything not implemented, and decide whether to re-commit or drop it.
5. Report the implementation rate as a standing metric.

## Output contract
Write `action-verification.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** action-verification
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
- Verification from artifacts, not reports
- Unimplemented actions explicitly re-decided
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
