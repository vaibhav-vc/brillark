---
name: severity-triage
category: council
description: "Assign a severity that means the same thing to everyone."
output: "severity-ratings.md"
used_by:
  - council-director
  - council-red-team
  - escalation-manager
---

# Severity Triage

`council` · produces `severity-ratings.md` · used by `council-director`, `council-red-team`, `escalation-manager`

Assign a severity that means the same thing to everyone.

## Procedure
1. Apply the fixed scale: blocker, major, minor, note.
2. Require a concrete failure scenario for anything rated blocker or major.
3. Rate on consequence, not on how strongly it was argued.
4. Check the rating against how similar findings were rated before.
5. Drop findings that cannot be made concrete.

## Output contract
`severity-ratings.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Blockers carry a concrete failure scenario
- Consistency with prior ratings checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
