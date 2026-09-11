---
name: stage-gate-review
category: orchestration
description: "Decide whether a venture stage is complete and what happens next."
output: "stage-gate-decision.md"
used_by:
  - director
---

# Stage Gate Review

`orchestration` · produces `stage-gate-decision.md` · used by `director`

Decide whether a venture stage is complete and what happens next.

## Procedure
1. Assemble the evidence pack the gate requires; refuse to review without it.
2. Check each exit criterion against evidence, not against effort spent.
3. Require the Council verdict before deciding.
4. Decide go, no-go, pivot, or kill in writing, naming the deciding evidence.
5. State what evidence would reverse the decision, and instruct memory consolidation.

## Output contract
`stage-gate-decision.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Decision names its deciding evidence
- Reversal condition stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
