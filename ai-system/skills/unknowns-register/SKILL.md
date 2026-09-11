---
name: unknowns-register
category: research
description: "Keep an explicit record of what the organisation does not know."
output: "unknowns-register.md"
used_by:
  - research-head
---

# Unknowns Register

`research` · produces `unknowns-register.md` · used by `research-head`

Keep an explicit record of what the organisation does not know.

## Procedure
1. Record each material unknown and the decision it affects.
2. Record whether it is being resolved, deliberately deferred, or accepted.
3. Record what resolving it would cost and what it would change.
4. Review at every stage gate so unknowns are chosen, not forgotten.
5. Distinguish unknowns from assumptions; assumptions live in the ledger.

## Output contract
`unknowns-register.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Each unknown tied to an affected decision
- Deferral is deliberate and recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
