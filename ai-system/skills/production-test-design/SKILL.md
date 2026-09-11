---
name: production-test-design
category: hardware
description: "Design the test that every unit passes through."
output: "production-test-spec.md"
used_by:
  - hardware-test-engineer
---

# Production Test Design

`hardware` · produces `production-test-spec.md` · used by `hardware-test-engineer`

Design the test that every unit passes through.

## Procedure
1. Define coverage: what defects the test must catch, and what it will not.
2. Design the fixture for reliable contact and fast cycle time.
3. Define pass limits from measured distribution, not from datasheet extremes.
4. Design for diagnosis, so a failure identifies the cause.
5. Measure test coverage and yield, and improve both.

## Output contract
`production-test-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Limits set from measured distribution
- Failures identify a cause, not just a reject
- The output states its confidence grade and names the evidence behind every load-bearing claim.
