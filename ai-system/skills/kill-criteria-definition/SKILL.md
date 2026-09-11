---
name: kill-criteria-definition
category: orchestration
description: "Decide in advance what would make us stop, while judgement is still uncommitted."
output: "kill-criteria.md"
used_by:
  - director
---

# Kill Criteria Definition

`orchestration` · produces `kill-criteria.md` · used by `director`

Decide in advance what would make us stop, while judgement is still uncommitted.

## Procedure
1. State the belief the bet depends on.
2. Define the observation that would disprove it.
3. Set the threshold and the deadline for that observation.
4. Name who declares the kill and who executes it.
5. Record it before the work starts; kill criteria written afterwards are rationalisations.

## Output contract
`kill-criteria.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Threshold and deadline both numeric
- Recorded before work begins
- The output states its confidence grade and names the evidence behind every load-bearing claim.
