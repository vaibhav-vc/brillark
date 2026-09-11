---
name: lifecycle-and-obsolescence-review
category: hardware
description: "Avoid designing in a part that is about to disappear."
output: "lifecycle-report.md"
used_by:
  - electronics-component-engineer
---

# Lifecycle And Obsolescence Review

`hardware` · produces `lifecycle-report.md` · used by `electronics-component-engineer`

Avoid designing in a part that is about to disappear.

## Procedure
1. Check lifecycle status for every part at selection, not at production.
2. Check for end-of-life and last-time-buy notices across distributors.
3. Prefer parts early in their lifecycle for products with a long life.
4. Flag parts with no published lifecycle status as a risk.
5. Re-review the BOM at every build phase.

## Output contract
`lifecycle-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Lifecycle checked at selection
- BOM re-reviewed at every build phase
- The output states its confidence grade and names the evidence behind every load-bearing claim.
