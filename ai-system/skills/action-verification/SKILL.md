---
name: action-verification
category: orchestration
description: "Confirm that agreed changes were actually made."
output: "action-verification.md"
used_by:
  - retrospective-agent
---

# Action Verification

`orchestration` · produces `action-verification.md` · used by `retrospective-agent`

Confirm that agreed changes were actually made.

## Procedure
1. List the actions agreed in the previous cycle with their owners.
2. Check the artifact each action was supposed to change.
3. Mark each as implemented, partially implemented, or not started — from evidence.
4. Ask why for anything not implemented, and decide whether to re-commit or drop it.
5. Report the implementation rate as a standing metric.

## Output contract
`action-verification.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Verification from artifacts, not reports
- Unimplemented actions explicitly re-decided
- The output states its confidence grade and names the evidence behind every load-bearing claim.
