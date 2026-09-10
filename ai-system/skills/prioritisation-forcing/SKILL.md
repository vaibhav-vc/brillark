---
name: prioritisation-forcing
category: orchestration
description: "Break a tie or a 'everything is critical' deadlock into a decision."
output: "prioritisation-decision.md"
used_by:
  - ceo-agent
---

# Prioritisation Forcing

**Category:** `orchestration` · **Output artifact:** `prioritisation-decision.md`

## What this skill does
Break a tie or a 'everything is critical' deadlock into a decision.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ceo-agent`.

## Procedure
1. Ask what happens if each item is delayed one cycle; consequence separates them.
2. Force a pairwise comparison rather than an absolute rating.
3. Apply the constraint: you may pick two of three.
4. Make the loser's cost explicit and accepted, not hidden.
5. Record the decision and the reasoning for future comparison.

## Output contract
Write `prioritisation-decision.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prioritisation-forcing
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
- Decision reached, not deferred
- Cost of the deprioritised item accepted in writing
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
