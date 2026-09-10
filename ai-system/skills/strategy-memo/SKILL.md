---
name: strategy-memo
category: strategy
description: "State the strategy as a set of explicit choices."
output: "strategy-memo.md"
used_by:
  - ceo-agent
---

# Strategy Memo

**Category:** `strategy` · **Output artifact:** `strategy-memo.md`

## What this skill does
State the strategy as a set of explicit choices.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ceo-agent`.

## Procedure
1. State the objective and the single most important constraint.
2. Describe the chosen approach and, equally, what is being deliberately not done.
3. Name the assumptions the strategy depends on.
4. Define what success looks like and by when.
5. State what evidence would cause the strategy to change.

## Output contract
Write `strategy-memo.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** strategy-memo
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
- What we are not doing is stated explicitly
- Change-of-mind evidence defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
