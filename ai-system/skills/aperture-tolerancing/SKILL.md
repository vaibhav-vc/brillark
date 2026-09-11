---
name: aperture-tolerancing
category: hardware
description: "Size openings so the mating part actually fits every time."
output: "aperture-spec.md"
used_by:
  - enclosure-designer
---

# Aperture Tolerancing

`hardware` · produces `aperture-spec.md` · used by `enclosure-designer`

Size openings so the mating part actually fits every time.

## Procedure
1. Compute the stack from board location through connector position to aperture.
2. Size the aperture for the mating connector's full engagement tolerance.
3. Check appearance: an oversized aperture looks like a defect.
4. Check finger and tool access where the user must reach through.
5. Verify on assembled units across the tolerance range.

## Output contract
`aperture-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Stack computed from board datum to aperture
- Appearance and access both checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
