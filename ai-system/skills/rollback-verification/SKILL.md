---
name: rollback-verification
category: engineering
description: "Prove the way back works before you need it."
output: "rollback-verification.md"
used_by:
  - release-manager
---

# Rollback Verification

`engineering` · produces `rollback-verification.md` · used by `release-manager`

Prove the way back works before you need it.

## Procedure
1. Identify what rollback means for code, data, and configuration together.
2. Verify data changes are backwards compatible with the previous version.
3. Execute the rollback in a realistic environment.
4. Measure how long it takes and who can do it.
5. Record the verification alongside the release record.

## Output contract
`rollback-verification.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Data compatibility verified, not just code
- Rollback time measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
