---
name: strategy-memo
category: strategy
description: "State the strategy as a set of explicit choices."
output: "strategy-memo.md"
used_by:
  - ceo-agent
---

# Strategy Memo

`strategy` · produces `strategy-memo.md` · used by `ceo-agent`

State the strategy as a set of explicit choices.

## Procedure
1. State the objective and the single most important constraint.
2. Describe the chosen approach and, equally, what is being deliberately not done.
3. Name the assumptions the strategy depends on.
4. Define what success looks like and by when.
5. State what evidence would cause the strategy to change.

## Output contract
`strategy-memo.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- What we are not doing is stated explicitly
- Change-of-mind evidence defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
