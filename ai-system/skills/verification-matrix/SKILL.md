---
name: verification-matrix
category: hardware
description: "Prove every requirement was actually tested."
output: "verification-matrix.csv"
used_by:
  - hardware-test-engineer
---

# Verification Matrix

`hardware` · produces `verification-matrix.csv` · used by `hardware-test-engineer`

Prove every requirement was actually tested.

## Procedure
1. List every requirement with a unique identifier.
2. Map each to the test that verifies it and the phase it runs in.
3. Record the result and the evidence reference for each.
4. Flag requirements with no verification method as a gap.
5. Keep the matrix current; it is the evidence the product meets its spec.

## Output contract
`verification-matrix.csv` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Every requirement mapped to a test and a result
- Unverifiable requirements flagged as gaps
- The output states its confidence grade and names the evidence behind every load-bearing claim.
