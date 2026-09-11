---
name: research-intake-triage
category: research
description: "Decide which questions are worth answering."
output: "intake-decision.md"
used_by:
  - research-head
---

# Research Intake Triage

`research` · produces `intake-decision.md` · used by `research-head`

Decide which questions are worth answering.

## Procedure
1. Require a named decision and decision-maker for every request.
2. Check the repository for an existing answer before accepting.
3. Estimate the cost of answering against the value of the decision.
4. Decline requests that are curiosity rather than decision support, and say so.
5. Queue accepted requests by decision urgency, not request order.

## Output contract
`intake-decision.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Named decision required per request
- Declines recorded with reasons
- The output states its confidence grade and names the evidence behind every load-bearing claim.
