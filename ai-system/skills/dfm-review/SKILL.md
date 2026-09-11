---
name: dfm-review
category: hardware
description: "Check every part can be made by the intended process."
output: "dfm-report.md"
used_by:
  - dfm-engineer
---

# Dfm Review

`hardware` · produces `dfm-report.md` · used by `dfm-engineer`

Check every part can be made by the intended process.

## Procedure
1. Review draft, wall thickness, radii, undercuts, and uniformity per part.
2. Check features against the supplier's stated capability, in numbers.
3. Identify what each finding costs to fix now versus after tooling.
4. Rank findings by cost and risk rather than by ease.
5. Close every finding or record the accepted risk with an owner.

## Output contract
`dfm-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Checked against numeric supplier capability
- Cost of fixing now versus after tooling stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
