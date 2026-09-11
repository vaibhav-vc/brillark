---
name: resolution-tracking
category: orchestration
description: "Follow escalations and blockers through to an actual outcome."
output: "resolution-log.md"
used_by:
  - escalation-manager
---

# Resolution Tracking

`orchestration` · produces `resolution-log.md` · used by `escalation-manager`

Follow escalations and blockers through to an actual outcome.

## Procedure
1. Record every escalation with an owner, a deadline, and the decision requested.
2. Chase before the deadline, not after it.
3. Record the outcome and the date, including 'decided not to act'.
4. Close only on evidence of resolution, never on elapsed time.
5. Report items that missed their deadline to the next level up.

## Output contract
`resolution-log.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Closure requires evidence
- Missed deadlines escalated automatically
- The output states its confidence grade and names the evidence behind every load-bearing claim.
