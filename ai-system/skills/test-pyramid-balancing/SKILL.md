---
name: test-pyramid-balancing
category: engineering
description: "Keep the suite fast and meaningful."
output: "pyramid-report.md"
used_by:
  - qa-test-strategist
---

# Test Pyramid Balancing

`engineering` · produces `pyramid-report.md` · used by `qa-test-strategist`

Keep the suite fast and meaningful.

## Procedure
1. Count tests at each level and their runtime contribution.
2. Identify high-level tests that duplicate lower-level coverage.
3. Push coverage down where the same bug can be caught cheaper.
4. Keep end-to-end tests for genuine integration risk only.
5. Track suite runtime as a first-class metric.

## Output contract
`pyramid-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Duplicated coverage pushed down
- Suite runtime tracked as a metric
- The output states its confidence grade and names the evidence behind every load-bearing claim.
