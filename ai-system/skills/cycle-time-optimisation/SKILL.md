---
name: cycle-time-optimisation
category: gtm
description: "Make the loop turn faster, not just convert better."
output: "cycle-time-optimisation.md"
used_by:
  - growth-loop-designer
---

# Cycle Time Optimisation

`gtm` · produces `cycle-time-optimisation.md` · used by `growth-loop-designer`

Make the loop turn faster, not just convert better.

## Procedure
1. Measure the elapsed time at each loop step.
2. Identify waiting steps that add no value.
3. Remove or parallelise the largest delay.
4. Verify the shortened cycle did not reduce conversion.
5. Re-project growth with the new cycle time.

## Output contract
`cycle-time-optimisation.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Conversion checked after shortening
- Growth re-projected with new timing
- The output states its confidence grade and names the evidence behind every load-bearing claim.
