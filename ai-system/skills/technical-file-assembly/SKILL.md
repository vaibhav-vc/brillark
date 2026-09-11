---
name: technical-file-assembly
category: hardware
description: "Keep the certification evidence current with what actually ships."
output: "technical-file"
used_by:
  - compliance-emc-engineer
---

# Technical File Assembly

`hardware` · produces `technical-file` · used by `compliance-emc-engineer`

Keep the certification evidence current with what actually ships.

## Procedure
1. Assemble the file as the design progresses rather than reconstructing it later.
2. Include schematics, BOM, test reports, risk assessment, and declarations.
3. Keep the file tied to a specific design revision.
4. Update the file after any change affecting compliance.
5. Check the file matches the shipping configuration before declaring conformity.

## Output contract
`technical-file` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- File tied to a specific design revision
- Checked against the shipping configuration
- The output states its confidence grade and names the evidence behind every load-bearing claim.
