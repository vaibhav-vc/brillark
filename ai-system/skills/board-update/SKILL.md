---
name: board-update
category: strategy
description: "Report to a board so they can help rather than merely be informed."
output: "board-update.md"
used_by:
  - ceo-agent
---

# Board Update

**Category:** `strategy` · **Output artifact:** `board-update.md`

## What this skill does
Report to a board so they can help rather than merely be informed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ceo-agent`.

## Procedure
1. Lead with the decisions you want from the board.
2. Report metrics against plan, with the same definitions as last time.
3. State the top three risks and what you are doing about each.
4. Be explicit about what is going badly before they find it themselves.
5. Send in advance so the meeting can be discussion rather than presentation.

## Output contract
Write `board-update.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** board-update
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
- Decisions requested up front
- Bad news surfaced by us first
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
