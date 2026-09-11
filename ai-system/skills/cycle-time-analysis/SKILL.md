---
name: cycle-time-analysis
category: orchestration
description: "Find where time actually goes between request and delivery."
output: "cycle-time-report.md"
used_by:
  - progress-tracker
---

# Cycle Time Analysis

`orchestration` · produces `cycle-time-report.md` · used by `progress-tracker`

Find where time actually goes between request and delivery.

## Procedure
1. Measure end-to-end elapsed time, including waiting.
2. Break it into active work, waiting for input, and waiting for review.
3. Identify the largest waiting segment — it is usually not the work itself.
4. Attack the largest segment with a process change.
5. Re-measure to confirm the change moved the total, not just one segment.

## Output contract
`cycle-time-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Waiting time measured separately
- Improvement verified end to end
- The output states its confidence grade and names the evidence behind every load-bearing claim.
