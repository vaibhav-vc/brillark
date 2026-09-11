---
name: open-question-tracking
category: orchestration
description: "Keep unresolved questions alive across handoffs instead of dropping them."
output: "open-questions.md"
used_by:
  - handoff-coordinator
---

# Open Question Tracking

`orchestration` · produces `open-questions.md` · used by `handoff-coordinator`

Keep unresolved questions alive across handoffs instead of dropping them.

## Procedure
1. Capture every open question with the work it affects.
2. Assign an owner and a by-when to each.
3. Carry the list through every handoff without editing it down for tidiness.
4. Close questions with an answer and its source, not with silence.
5. Escalate questions that survive two handoffs unanswered.

## Output contract
`open-questions.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Questions survive handoffs intact
- Closure requires a sourced answer
- The output states its confidence grade and names the evidence behind every load-bearing claim.
