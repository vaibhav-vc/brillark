---
name: tolerance-stackup-analysis
category: hardware
description: "Work out whether the parts will actually assemble."
output: "stackup.md"
used_by:
  - mechanical-engineer
---

# Tolerance Stackup Analysis

`hardware` · produces `stackup.md` · used by `mechanical-engineer`

Work out whether the parts will actually assemble.

## Procedure
1. Identify the dimension chain that controls the critical fit.
2. Compute worst-case and statistical stack results for that chain.
3. Compare against the required fit, including clearance for assembly.
4. Identify the contributor that dominates and tighten only that one.
5. Re-run after any dimension or process change.

## Output contract
`stackup.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Both worst-case and statistical results computed
- Dominant contributor identified before tightening
- The output states its confidence grade and names the evidence behind every load-bearing claim.
