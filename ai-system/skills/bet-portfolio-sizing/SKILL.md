---
name: bet-portfolio-sizing
category: strategy
description: "Allocate effort across bets according to their expected value and risk."
output: "bet-portfolio.md"
used_by:
  - ceo-agent
---

# Bet Portfolio Sizing

**Category:** `strategy` · **Output artifact:** `bet-portfolio.md`

## What this skill does
Allocate effort across bets according to their expected value and risk.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ceo-agent`.

## Procedure
1. List the bets with their thesis, cost, and expected payoff.
2. Classify by horizon: core, adjacent, and speculative.
3. Size each so a failure is survivable and a success is meaningful.
4. Set the kill criterion and the review point for each.
5. Check the portfolio balance rather than optimising each bet alone.

## Output contract
Write `bet-portfolio.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** bet-portfolio-sizing
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
- Each bet's failure is survivable
- Portfolio balance assessed, not just individual bets
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
