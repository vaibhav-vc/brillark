---
name: interference-checking
category: hardware
description: "Find the collisions before the parts are made."
output: "interference-report.md"
used_by:
  - cad-modeler
---

# Interference Checking

`hardware` · produces `interference-report.md` · used by `cad-modeler`

Find the collisions before the parts are made.

## Procedure
1. Run interference detection on every assembly revision, not only before release.
2. Check at tolerance extremes, not only at nominal.
3. Check moving parts through their full travel.
4. Check assembly access: can a hand and tool reach every fastener?
5. Record and resolve every clash, including the ones that look small.

## Output contract
`interference-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Checked at tolerance extremes and through full travel
- Tool and hand access verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
