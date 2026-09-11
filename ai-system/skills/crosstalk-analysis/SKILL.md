---
name: crosstalk-analysis
category: hardware
description: "Keep signals from corrupting their neighbours."
output: "crosstalk-report.md"
used_by:
  - signal-integrity-engineer
---

# Crosstalk Analysis

`hardware` · produces `crosstalk-report.md` · used by `signal-integrity-engineer`

Keep signals from corrupting their neighbours.

## Procedure
1. Identify aggressor and victim pairs by edge rate and coupled length.
2. Apply spacing rules derived from the stack-up, not from folklore.
3. Check coupling between layers, not only within a layer.
4. Pay attention to connectors and cables, where coupling is worst.
5. Verify on hardware for the interfaces that would cost a spin.

## Output contract
`crosstalk-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Spacing derived from the stack-up
- Inter-layer and connector coupling both checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
