---
name: throughput-reporting
category: orchestration
description: "Measure how much work actually completes per cycle so capacity claims can be checked."
output: "throughput-report.md"
used_by:
  - progress-tracker
---

# Throughput Reporting

`orchestration` · produces `throughput-report.md` · used by `progress-tracker`

Measure how much work actually completes per cycle so capacity claims can be checked.

## Procedure
1. Count completed tasks that passed their DoD, not tasks started.
2. Normalise by task size class so the count means something.
3. Report the trend over at least three cycles.
4. Separate rework from new work; rework is a quality signal.
5. Use the trend, not a single cycle, for capacity planning.

## Output contract
`throughput-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Only DoD-passed work counted
- Rework separated from new work
- The output states its confidence grade and names the evidence behind every load-bearing claim.
