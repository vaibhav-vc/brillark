---
name: fabrication-output-review
category: hardware
description: "Check the package before the fabricator does."
output: "fab-package"
used_by:
  - pcb-layout-designer
---

# Fabrication Output Review

`hardware` · produces `fab-package` · used by `pcb-layout-designer`

Check the package before the fabricator does.

## Procedure
1. Generate outputs and re-import them, reviewing what the fabricator will see.
2. Check the drill, layer, mask, and paste files against intent.
3. Include a readme with stack-up, impedance, finish, and any special requirement.
4. Check the assembly files: placement, orientation, and polarity marks.
5. Run the fabricator's own design rule check before sending.

## Output contract
`fab-package` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Outputs re-imported and reviewed as the fabricator sees them
- Fabricator's own rule check run before sending
- The output states its confidence grade and names the evidence behind every load-bearing claim.
