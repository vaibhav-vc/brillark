---
name: design-for-assembly
category: hardware
description: "Reduce the cost and error rate of putting it together."
output: "dfa-report.md"
used_by:
  - dfm-engineer
---

# Design For Assembly

`hardware` · produces `dfa-report.md` · used by `dfm-engineer`

Reduce the cost and error rate of putting it together.

## Procedure
1. Count parts and operations; both are direct cost.
2. Combine parts where function allows and eliminate fasteners where a feature will do.
3. Design self-locating features so parts can only go in the right way.
4. Design for assembly from one direction where possible.
5. Check the sequence with a real person building a real unit.

## Output contract
`dfa-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Parts can only assemble the correct way
- Sequence validated with a real build
- The output states its confidence grade and names the evidence behind every load-bearing claim.
