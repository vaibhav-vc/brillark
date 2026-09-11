---
name: design-decision-record
category: design
description: "Record a design decision so it is not re-argued every week."
output: "design-decision.md"
used_by:
  - design-critic
---

# Design Decision Record

`design` · produces `design-decision.md` · used by `design-critic`

Record a design decision so it is not re-argued every week.

## Procedure
1. State the decision and the goal it serves.
2. Record the alternatives considered and why each was rejected.
3. Record the evidence: research, testing, or constraint.
4. Record what would reopen the decision.
5. Store it with the surface so the next designer finds it.

## Output contract
`design-decision.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Rejected alternatives recorded with reasons
- Reopening condition stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
