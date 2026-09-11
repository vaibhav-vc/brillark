---
name: claim-weight-proportionality
category: research
description: "Match the evidence demanded to the weight the claim will carry."
output: "weight-assessment.md"
used_by:
  - source-verifier
---

# Claim Weight Proportionality

`research` · produces `weight-assessment.md` · used by `source-verifier`

Match the evidence demanded to the weight the claim will carry.

## Procedure
1. Establish what decision rests on the claim and how reversible it is.
2. Set the required grade from that consequence before assessing sources.
3. Compare the available evidence against the requirement, not against convenience.
4. State explicitly when a claim cannot support the weight being put on it.
5. Escalate rather than letting a decision quietly rest on a weak claim.

## Output contract
`weight-assessment.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Required grade set from consequence, before searching
- Under-supported claims escalated, not softened
- The output states its confidence grade and names the evidence behind every load-bearing claim.
