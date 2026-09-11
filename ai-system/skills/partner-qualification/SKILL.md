---
name: partner-qualification
category: gtm
description: "Decide whether a candidate partner is worth the effort."
output: "partner-qualification.md"
used_by:
  - partnership-bd-agent
---

# Partner Qualification

`gtm` · produces `partner-qualification.md` · used by `partnership-bd-agent`

Decide whether a candidate partner is worth the effort.

## Procedure
1. Verify they actually reach our ICP at meaningful volume.
2. Check the mutual incentive: what do they lose by not doing this?
3. Assess their capacity to execute, not just their willingness to sign.
4. Check for conflicts with their existing partners or roadmap.
5. Score and rank rather than pursuing everyone who responds.

## Output contract
`partner-qualification.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Mutual incentive verified
- Execution capacity assessed, not just intent
- The output states its confidence grade and names the evidence behind every load-bearing claim.
