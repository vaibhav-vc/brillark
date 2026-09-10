---
name: resource-allocation
category: orchestration
description: "Decide which agents and budget go to which bets this cycle."
output: "allocation-decision.md"
used_by:
  - director
---

# Resource Allocation

**Category:** `orchestration` · **Output artifact:** `allocation-decision.md`

## What this skill does
Decide which agents and budget go to which bets this cycle.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `director`.

## Procedure
1. List the candidate bets with their expected value and confidence.
2. Rank by value per unit of scarce resource, not by absolute value.
3. Fund fewer things properly rather than everything partially.
4. State explicitly what is being starved so the trade-off is visible.
5. Set the review point at which allocation is revisited.

## Output contract
Write `allocation-decision.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** resource-allocation
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
- Trade-offs stated explicitly
- Fewer, fully funded bets over partial funding
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
