---
name: load-testing
category: engineering
description: "Find the system's real limits under realistic conditions."
output: "load-test-report.md"
used_by:
  - performance-engineer
---

# Load Testing

`engineering` · produces `load-test-report.md` · used by `performance-engineer`

Find the system's real limits under realistic conditions.

## Procedure
1. Model realistic traffic shape, including think time and mixed operations.
2. Use production-like data volumes; small datasets hide the real bottlenecks.
3. Ramp to failure to find the breaking point, not just to the target.
4. Observe the whole system during the test, not only the response times.
5. Record the limit, the failure mode, and the first component to break.

## Output contract
`load-test-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Ramped to failure, not just to target
- Failure mode recorded, not just the limit
- The output states its confidence grade and names the evidence behind every load-bearing claim.
