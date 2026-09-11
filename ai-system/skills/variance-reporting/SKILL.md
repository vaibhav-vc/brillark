---
name: variance-reporting
category: orchestration
description: "Report the gap between plan and reality early and without spin."
output: "variance-report.md"
used_by:
  - progress-tracker
---

# Variance Reporting

`orchestration` · produces `variance-report.md` · used by `progress-tracker`

Report the gap between plan and reality early and without spin.

## Procedure
1. Compare actual against plan for schedule, scope, and budget.
2. Report variance as soon as it is detectable, not at the deadline.
3. Explain the cause, distinguishing estimation error from scope change from blockage.
4. State the revised forecast and its confidence.
5. Propose the recovery option or state that there is none.

## Output contract
`variance-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Reported before the deadline
- Cause classified, not just described
- The output states its confidence grade and names the evidence behind every load-bearing claim.
