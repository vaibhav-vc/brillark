---
name: thermal-validation-testing
category: hardware
description: "Measure what the product actually runs at."
output: "thermal-test-report.md"
used_by:
  - thermal-engineer
---

# Thermal Validation Testing

`hardware` · produces `thermal-test-report.md` · used by `thermal-engineer`

Measure what the product actually runs at.

## Procedure
1. Instrument the components the analysis identified as critical.
2. Run the worst-case workload at the worst-case ambient.
3. Run long enough to reach steady state, not just to a plateau that looks stable.
4. Compare measurements against the model and investigate differences.
5. Record margins per component against their limits.

## Output contract
`thermal-test-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Run to true steady state at worst-case ambient
- Margins recorded per component
- The output states its confidence grade and names the evidence behind every load-bearing claim.
