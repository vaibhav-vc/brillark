---
name: resource-allocation
category: orchestration
description: "Decide which agents and budget go to which bets this cycle."
output: "allocation-decision.md"
used_by:
  - director
---

# Resource Allocation

`orchestration` · produces `allocation-decision.md` · used by `director`

Decide which agents and budget go to which bets this cycle.

## Procedure
1. List the candidate bets with their expected value and confidence.
2. Rank by value per unit of scarce resource, not by absolute value.
3. Fund fewer things properly rather than everything partially.
4. State explicitly what is being starved so the trade-off is visible.
5. Set the review point at which allocation is revisited.

## Output contract
`allocation-decision.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Trade-offs stated explicitly
- Fewer, fully funded bets over partial funding
- The output states its confidence grade and names the evidence behind every load-bearing claim.
