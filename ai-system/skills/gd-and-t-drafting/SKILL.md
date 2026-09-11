---
name: gd-and-t-drafting
category: hardware
description: "Dimension drawings so the part can be inspected and accepted unambiguously."
output: "drawing"
used_by:
  - cad-modeler
---

# Gd And T Drafting

`hardware` · produces `drawing` · used by `cad-modeler`

Dimension drawings so the part can be inspected and accepted unambiguously.

## Procedure
1. Define datums that reflect how the part is located in the assembly.
2. Apply geometric tolerances to the features that matter functionally.
3. Avoid over-dimensioning; every tolerance costs money to hold.
4. Tolerance to process capability rather than to wishful precision.
5. Check the drawing is inspectable with the equipment the supplier has.

## Output contract
`drawing` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Datums reflect assembly location
- Tolerances within supplier process capability
- The output states its confidence grade and names the evidence behind every load-bearing claim.
