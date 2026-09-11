---
name: touch-temperature-compliance
category: hardware
description: "Keep the outside safe to touch."
output: "touch-temp-report.md"
used_by:
  - thermal-engineer
---

# Touch Temperature Compliance

`hardware` · produces `touch-temp-report.md` · used by `thermal-engineer`

Keep the outside safe to touch.

## Procedure
1. Identify every accessible surface and its material.
2. Apply the temperature limit for that material and contact duration.
3. Measure at the hottest accessible point under worst-case operation.
4. Fix by spreading or relocating heat, not by adding a warning label.
5. Record the measurement as certification evidence.

## Output contract
`touch-temp-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Limits applied per material and contact duration
- Fixed by design, not by warning label
- The output states its confidence grade and names the evidence behind every load-bearing claim.
