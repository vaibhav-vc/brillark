---
name: parametric-modeling
category: hardware
description: "Build a 3D model that survives change."
output: "cad-model"
used_by:
  - cad-modeler
---

# Parametric Modeling

`hardware` · produces `cad-model` · used by `cad-modeler`

Build a 3D model that survives change.

## Procedure
1. Anchor sketches to datums and origins, never to faces that move.
2. Drive dimensions from named parameters a change can propagate through.
3. Keep the feature tree ordered, named, and readable by someone else.
4. Avoid imported dead geometry where a parametric feature would do.
5. Test the model by changing a driving parameter and confirming a clean rebuild.

## Output contract
`cad-model` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Rebuilds cleanly under a parameter change
- Feature tree named and readable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
