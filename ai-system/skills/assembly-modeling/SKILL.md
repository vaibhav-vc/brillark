---
name: assembly-modeling
category: hardware
description: "Model the assembly so it reflects how the product is actually put together."
output: "assembly-model"
used_by:
  - cad-modeler
---

# Assembly Modeling

`hardware` · produces `assembly-model` · used by `cad-modeler`

Model the assembly so it reflects how the product is actually put together.

## Procedure
1. Structure the assembly to match the real build sequence and sub-assemblies.
2. Mate to datums rather than to arbitrary faces.
3. Include fasteners, cables, and the space a hand needs during assembly.
4. Model the worst-case positions of moving and floating parts.
5. Keep part numbering consistent between model, drawing, and BOM.

## Output contract
`assembly-model` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Structure matches the real build sequence
- Fasteners and cable routing modelled
- The output states its confidence grade and names the evidence behind every load-bearing claim.
