---
name: intent-clarification
category: orchestration
description: "Convert a vague request into a restatement the requester confirms before work starts."
output: "clarified-brief.md"
used_by:
  - director
  - intake-router
---

# Intent Clarification

**Category:** `orchestration` · **Output artifact:** `clarified-brief.md`

## What this skill does
Convert a vague request into a restatement the requester confirms before work starts.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `director`, `intake-router`.

## Procedure
1. Restate the request in your own words, including what you believe the output should be.
2. Name the decision the output is meant to support.
3. List the interpretations you considered and which one you chose.
4. Ask a question only where different readings would produce materially different work.
5. Get confirmation, or state the assumption you are proceeding under.

## Output contract
Write `clarified-brief.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** intent-clarification
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
- Restatement names the supported decision
- Only material ambiguities are escalated as questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
