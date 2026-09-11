---
name: bet-portfolio-sizing
category: strategy
description: "Allocate effort across bets according to their expected value and risk."
output: "bet-portfolio.md"
used_by:
  - ceo-agent
---

# Bet Portfolio Sizing

`strategy` · produces `bet-portfolio.md` · used by `ceo-agent`

Allocate effort across bets according to their expected value and risk.

## Procedure
1. List the bets with their thesis, cost, and expected payoff.
2. Classify by horizon: core, adjacent, and speculative.
3. Size each so a failure is survivable and a success is meaningful.
4. Set the kill criterion and the review point for each.
5. Check the portfolio balance rather than optimising each bet alone.

## Output contract
`bet-portfolio.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Each bet's failure is survivable
- Portfolio balance assessed, not just individual bets
- The output states its confidence grade and names the evidence behind every load-bearing claim.
