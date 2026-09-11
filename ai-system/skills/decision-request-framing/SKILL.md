---
name: decision-request-framing
category: orchestration
description: "Escalate a problem as a decision someone can actually make."
output: "decision-request.md"
used_by:
  - escalation-manager
---

# Decision Request Framing

`orchestration` · produces `decision-request.md` · used by `escalation-manager`

Escalate a problem as a decision someone can actually make.

## Procedure
1. State the decision being requested in one sentence.
2. Give the two or three viable options, not an open question.
3. State your recommendation and your confidence in it.
4. Provide the minimum context needed to decide without further reading.
5. State the deadline and what happens by default if no decision arrives.

## Output contract
`decision-request.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Options provided, not an open question
- Default-if-no-decision stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
