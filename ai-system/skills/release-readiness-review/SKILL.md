---
name: release-readiness-review
category: engineering
description: "Decide honestly whether this can ship."
output: "release-readiness.md"
used_by:
  - engineering-head
  - release-manager
---

# Release Readiness Review

`engineering` · produces `release-readiness.md` · used by `engineering-head`, `release-manager`

Decide honestly whether this can ship.

## Procedure
1. Check tests, security review, and observability are all complete.
2. Confirm the rollback path is verified.
3. Confirm acceptance criteria are met, including the unhappy paths.
4. Confirm support and documentation are ready for the change.
5. Record go or no-go with the reason; never waive the gate under deadline pressure.

## Output contract
`release-readiness.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- All gates checked, none waived
- Decision recorded with a reason
- The output states its confidence grade and names the evidence behind every load-bearing claim.
