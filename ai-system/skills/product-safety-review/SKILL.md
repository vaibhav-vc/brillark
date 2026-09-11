---
name: product-safety-review
category: hardware
description: "Check the product cannot hurt anyone."
output: "safety-review.md"
used_by:
  - compliance-emc-engineer
---

# Product Safety Review

`hardware` · produces `safety-review.md` · used by `compliance-emc-engineer`

Check the product cannot hurt anyone.

## Procedure
1. Identify hazards: electrical, thermal, mechanical, chemical, and radiation.
2. Check creepage, clearance, and insulation for the working voltages.
3. Check accessible parts, sharp edges, and trapping points.
4. Check battery safety, charging, and failure behaviour where applicable.
5. Verify markings, warnings, and instructions meet the standard.

## Output contract
`safety-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Creepage and clearance checked for working voltage
- Battery failure behaviour verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
