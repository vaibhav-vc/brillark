---
name: code-health-metrics
category: engineering
description: "Measure whether the codebase is getting easier or harder to change."
output: "code-health-report.md"
used_by:
  - tech-debt-refactor-agent
---

# Code Health Metrics

`engineering` · produces `code-health-report.md` · used by `tech-debt-refactor-agent`

Measure whether the codebase is getting easier or harder to change.

## Procedure
1. Track change lead time and defect density by area.
2. Identify files and modules with disproportionate churn and defects.
3. Measure test coverage where it correlates with defect rate, not as an end.
4. Report the trend, not the absolute value.
5. Use the metrics to target refactoring, never to rank people.

## Output contract
`code-health-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Trend reported rather than absolutes
- Metrics used for targeting, not ranking
- The output states its confidence grade and names the evidence behind every load-bearing claim.
