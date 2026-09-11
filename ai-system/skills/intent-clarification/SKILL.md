---
name: intent-clarification
category: orchestration
description: "Convert a vague request into a restatement the requester confirms before work starts."
output: "clarified-brief.md"
used_by:
  - director
  - intake-router
---

# Intent Clarification

`orchestration` · produces `clarified-brief.md` · used by `director`, `intake-router`

Convert a vague request into a restatement the requester confirms before work starts.

## Procedure
1. Restate the request in your own words, including what you believe the output should be.
2. Name the decision the output is meant to support.
3. List the interpretations you considered and which one you chose.
4. Ask a question only where different readings would produce materially different work.
5. Get confirmation, or state the assumption you are proceeding under.

## Output contract
`clarified-brief.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Restatement names the supported decision
- Only material ambiguities are escalated as questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
