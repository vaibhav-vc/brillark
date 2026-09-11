---
name: prioritisation-forcing
category: orchestration
description: "Break a tie or a 'everything is critical' deadlock into a decision."
output: "prioritisation-decision.md"
used_by:
  - ceo-agent
---

# Prioritisation Forcing

`orchestration` · produces `prioritisation-decision.md` · used by `ceo-agent`

Break a tie or a 'everything is critical' deadlock into a decision.

## Procedure
1. Ask what happens if each item is delayed one cycle; consequence separates them.
2. Force a pairwise comparison rather than an absolute rating.
3. Apply the constraint: you may pick two of three.
4. Make the loser's cost explicit and accepted, not hidden.
5. Record the decision and the reasoning for future comparison.

## Output contract
`prioritisation-decision.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Decision reached, not deferred
- Cost of the deprioritised item accepted in writing
- The output states its confidence grade and names the evidence behind every load-bearing claim.
