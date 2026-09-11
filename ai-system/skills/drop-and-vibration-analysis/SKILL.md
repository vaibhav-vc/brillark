---
name: drop-and-vibration-analysis
category: hardware
description: "Check the product survives being dropped and shaken."
output: "drop-vibration-report.md"
used_by:
  - mechanical-engineer
---

# Drop And Vibration Analysis

`hardware` · produces `drop-vibration-report.md` · used by `mechanical-engineer`

Check the product survives being dropped and shaken.

## Procedure
1. Define drop heights and orientations from real use and shipping.
2. Define the vibration profile from the transport and use environment.
3. Identify the components most at risk: connectors, displays, and heavy masses.
4. Analyse, then verify on real hardware — simulation alone misses joint behaviour.
5. Fix at the structure rather than by adding foam.

## Output contract
`drop-vibration-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Profiles drawn from real transport and use
- Verified on real hardware, not simulation alone
- The output states its confidence grade and names the evidence behind every load-bearing claim.
