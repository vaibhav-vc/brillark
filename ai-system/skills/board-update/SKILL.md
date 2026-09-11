---
name: board-update
category: strategy
description: "Report to a board so they can help rather than merely be informed."
output: "board-update.md"
used_by:
  - ceo-agent
---

# Board Update

`strategy` · produces `board-update.md` · used by `ceo-agent`

Report to a board so they can help rather than merely be informed.

## Procedure
1. Lead with the decisions you want from the board.
2. Report metrics against plan, with the same definitions as last time.
3. State the top three risks and what you are doing about each.
4. Be explicit about what is going badly before they find it themselves.
5. Send in advance so the meeting can be discussion rather than presentation.

## Output contract
`board-update.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Decisions requested up front
- Bad news surfaced by us first
- The output states its confidence grade and names the evidence behind every load-bearing claim.
