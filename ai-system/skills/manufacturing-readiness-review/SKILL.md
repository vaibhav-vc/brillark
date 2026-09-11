---
name: manufacturing-readiness-review
category: hardware
description: "Check the factory can actually build it."
output: "readiness-review.md"
used_by:
  - hardware-head
---

# Manufacturing Readiness Review

`hardware` · produces `readiness-review.md` · used by `hardware-head`

Check the factory can actually build it.

## Procedure
1. Confirm the design is frozen and documentation matches it.
2. Confirm every part is sourced with lead time inside the schedule.
3. Confirm process capability, fixtures, and production test are ready.
4. Confirm operator instructions exist and have been followed by a real operator.
5. Confirm quality criteria and what happens to units that fail.

## Output contract
`readiness-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Documentation confirmed to match the frozen design
- Instructions validated by a real operator
- The output states its confidence grade and names the evidence behind every load-bearing claim.
