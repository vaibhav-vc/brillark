---
name: motion-performance-check
category: design
description: "Confirm the animation does not cost more than it gives."
output: "motion-performance.md"
used_by:
  - motion-designer
---

# Motion Performance Check

`design` · produces `motion-performance.md` · used by `motion-designer`

Confirm the animation does not cost more than it gives.

## Procedure
1. Measure frame rate on the slowest supported device.
2. Prefer properties that do not force layout recalculation.
3. Check the animation's cost against the frontend performance budget.
4. Verify behaviour when animations overlap or interrupt.
5. Cut or simplify any animation that cannot hold frame rate.

## Output contract
`motion-performance.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Measured on the slowest supported device
- Within the frontend performance budget
- The output states its confidence grade and names the evidence behind every load-bearing claim.
