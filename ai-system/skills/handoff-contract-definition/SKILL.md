---
name: handoff-contract-definition
category: orchestration
description: "Define what must accompany work passed between two specific roles."
output: "handoff-contract.md"
used_by:
  - handoff-coordinator
---

# Handoff Contract Definition

`orchestration` · produces `handoff-contract.md` · used by `handoff-coordinator`

Define what must accompany work passed between two specific roles.

## Procedure
1. Ask the receiving role what inputs it actually needs to start.
2. Specify the artifact, its format, and its completeness conditions.
3. Require stated assumptions and open questions as part of the handoff.
4. Define what the receiver may reject for, and how.
5. Version the contract; roles evolve and stale contracts cause silent gaps.

## Output contract
`handoff-contract.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Receiver defined the requirements
- Rejection grounds specified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
