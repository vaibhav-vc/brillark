---
name: board-mounting-design
category: hardware
description: "Hold the board so its connectors land where they should."
output: "mounting-spec.md"
used_by:
  - enclosure-designer
---

# Board Mounting Design

`hardware` · produces `mounting-spec.md` · used by `enclosure-designer`

Hold the board so its connectors land where they should.

## Procedure
1. Locate the board on defined datums rather than on nominal geometry.
2. Specify standoffs and fastening that do not flex the board.
3. Check clearance under and over the board across the tolerance range.
4. Provide strain relief where cables attach.
5. Verify connector alignment with apertures at tolerance extremes.

## Output contract
`mounting-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Board located on datums
- Connector alignment verified at extremes
- The output states its confidence grade and names the evidence behind every load-bearing claim.
