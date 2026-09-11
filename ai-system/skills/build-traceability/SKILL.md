---
name: build-traceability
category: hardware
description: "Know which parts are in which unit."
output: "build-record.md"
used_by:
  - prototyping-fabrication-agent
---

# Build Traceability

`hardware` · produces `build-record.md` · used by `prototyping-fabrication-agent`

Know which parts are in which unit.

## Procedure
1. Label every physical part and assembly with its revision at build.
2. Record the build configuration: part revisions, firmware, and any deviation.
3. Record every bodge, rework, and substitution on the unit's record.
4. Keep the record with the unit through testing.
5. Trace any test result back to the exact configuration that produced it.

## Output contract
`build-record.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Every unit's exact configuration recorded
- Bodges and reworks recorded, not remembered
- The output states its confidence grade and names the evidence behind every load-bearing claim.
