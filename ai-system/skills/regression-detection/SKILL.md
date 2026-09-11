---
name: regression-detection
category: orchestration
description: "Catch quality drops when a prompt, skill, or agent definition changes."
output: "regression-report.md"
used_by:
  - evaluation-harness-agent
---

# Regression Detection

`orchestration` · produces `regression-report.md` · used by `evaluation-harness-agent`

Catch quality drops when a prompt, skill, or agent definition changes.

## Procedure
1. Run the evaluation suite before and after the change.
2. Compare scores per case, not just in aggregate — averages hide regressions.
3. Investigate any case that moved down, however small the aggregate change.
4. Block the change or accept the regression explicitly with a reason.
5. Record the result alongside the change in version history.

## Output contract
`regression-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Per-case comparison, not just aggregate
- Accepted regressions explicitly justified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
