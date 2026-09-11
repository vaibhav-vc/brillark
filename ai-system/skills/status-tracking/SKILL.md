---
name: status-tracking
category: orchestration
description: "Report the true state of work from artifacts rather than self-assessment."
output: "status-board.md"
used_by:
  - progress-tracker
---

# Status Tracking

`orchestration` · produces `status-board.md` · used by `progress-tracker`

Report the true state of work from artifacts rather than self-assessment.

## Procedure
1. Derive status from artifact existence and DoD checks, not from percentages.
2. Use a strict state set: not started, in progress, blocked, in review, done.
3. Record the last observed change and its timestamp.
4. Flag any divergence between reported and observed status.
5. Publish on a fixed cadence so absence of news is itself information.

## Output contract
`status-board.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Status derived from artifacts
- Divergence from self-reports flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
