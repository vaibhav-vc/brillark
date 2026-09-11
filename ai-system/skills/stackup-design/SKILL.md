---
name: stackup-design
category: hardware
description: "Decide the layer structure before anything is routed."
output: "stackup.md"
used_by:
  - pcb-layout-designer
---

# Stackup Design

`hardware` · produces `stackup.md` · used by `pcb-layout-designer`

Decide the layer structure before anything is routed.

## Procedure
1. Agree the stack-up with the actual fabricator, including materials and thicknesses.
2. Assign layers so every signal layer has an adjacent reference plane.
3. Compute trace geometry for the required impedances from that stack-up.
4. Check the stack-up supports the board's thickness and rigidity needs.
5. Document it in the fabrication package with impedance requirements.

## Output contract
`stackup.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Agreed with the actual fabricator
- Every signal layer has an adjacent reference plane
- The output states its confidence grade and names the evidence behind every load-bearing claim.
