---
name: closure-and-retention-design
category: hardware
description: "Make it close properly and stay closed."
output: "closure-spec.md"
used_by:
  - enclosure-designer
---

# Closure And Retention Design

`hardware` · produces `closure-spec.md` · used by `enclosure-designer`

Make it close properly and stay closed.

## Procedure
1. Design the closure for the force a user will actually apply.
2. Design snap features for the required insertion and retention forces separately.
3. Check retention after thermal cycling and creep, not just at build.
4. Design for the number of open-close cycles the product needs.
5. Test to failure to know the margin, not just to the requirement.

## Output contract
`closure-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Insertion and retention forces specified separately
- Tested to failure to establish margin
- The output states its confidence grade and names the evidence behind every load-bearing claim.
