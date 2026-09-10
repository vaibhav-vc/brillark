---
name: runbook-authoring
category: orchestration
description: "Write a procedure another agent can execute without asking questions."
output: "runbook.md"
used_by:
  - coo-agent
---

# Runbook Authoring

**Category:** `orchestration` · **Output artifact:** `runbook.md`

## What this skill does
Write a procedure another agent can execute without asking questions.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `coo-agent`.

## Procedure
1. State the trigger condition and the expected end state.
2. Write numbered steps with the exact command, query, or decision at each.
3. Include the verification after each step that proves it worked.
4. Cover the failure branches, not only the happy path.
5. Have a different agent execute it once and fix everything they had to ask about.

## Output contract
Write `runbook.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** runbook-authoring
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
- Tested by a different agent
- Failure branches covered
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
