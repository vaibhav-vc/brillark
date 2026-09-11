---
name: safe-field-update-design
category: hardware
description: "Make sure an update cannot brick a unit in the field."
output: "update-spec.md"
used_by:
  - embedded-firmware-engineer
---

# Safe Field Update Design

`hardware` · produces `update-spec.md` · used by `embedded-firmware-engineer`

Make sure an update cannot brick a unit in the field.

## Procedure
1. Make the update atomic: it either completes or the old image still runs.
2. Verify image integrity and authenticity before switching to it.
3. Keep a recovery path that works when the main image does not.
4. Handle power loss at every point in the update.
5. Test the update by interrupting it repeatedly on real hardware.

## Output contract
`update-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Recovery path works when the main image fails
- Tested by interrupting at every stage
- The output states its confidence grade and names the evidence behind every load-bearing claim.
