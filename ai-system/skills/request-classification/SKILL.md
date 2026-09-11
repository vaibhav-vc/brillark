---
name: request-classification
category: orchestration
description: "Put an incoming request into the taxonomy that determines how it is handled."
output: "intake-record.md"
used_by:
  - intake-router
---

# Request Classification

`orchestration` · produces `intake-record.md` · used by `intake-router`

Put an incoming request into the taxonomy that determines how it is handled.

## Procedure
1. Determine the primary domain: finance, business, engineering, orchestration, legal, or council.
2. Classify the work type: decide, build, research, review, or operate.
3. Rate reversibility — a one-way door needs a heavier process than a two-way door.
4. Set urgency from a real deadline, not from the requester's tone.
5. Attach the classification to the intake record.

## Output contract
`intake-record.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Reversibility explicitly rated
- Urgency justified by a real deadline
- The output states its confidence grade and names the evidence behind every load-bearing claim.
