---
name: weekly-scorecard
category: orchestration
description: "Publish a small set of numbers that show whether the organisation is on track."
output: "scorecard.md"
used_by:
  - coo-agent
---

# Weekly Scorecard

`orchestration` · produces `scorecard.md` · used by `coo-agent`

Publish a small set of numbers that show whether the organisation is on track.

## Procedure
1. Select metrics from the metrics tree only — no ad hoc additions.
2. Show the value, the target, and the trend, never the value alone.
3. Flag only off-trend metrics for discussion.
4. Attach the owner to each line.
5. Keep definitions stable; a changed definition resets the trend's meaning.

## Output contract
`scorecard.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Trend shown alongside value
- Definitions stable across periods
- The output states its confidence grade and names the evidence behind every load-bearing claim.
