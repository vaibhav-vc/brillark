---
name: emc-design-review
category: hardware
description: "Design for compliance while it is still cheap."
output: "emc-review.md"
used_by:
  - compliance-emc-engineer
---

# Emc Design Review

`hardware` · produces `emc-review.md` · used by `compliance-emc-engineer`

Design for compliance while it is still cheap.

## Procedure
1. Review grounding, return paths, and cable entry points for emission risk.
2. Review filtering at every interface leaving the enclosure.
3. Review shielding and aperture sizes against the frequencies of concern.
4. Check clock and switching frequencies against known problem bands.
5. Fix at the source before designing in shielding.

## Output contract
`emc-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Emissions addressed at the source first
- Cable entry and aperture risks reviewed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
