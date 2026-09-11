---
name: packaging-design
category: finance
description: "Group capabilities into tiers customers can choose between."
output: "packaging.md"
used_by:
  - pricing-strategist
---

# Packaging Design

`finance` · produces `packaging.md` · used by `pricing-strategist`

Group capabilities into tiers customers can choose between.

## Procedure
1. Identify the dimensions on which customer needs genuinely differ.
2. Build tiers around those differences, not around feature counts.
3. Ensure each tier is coherent for the segment it targets.
4. Design the upgrade trigger so growth naturally moves customers up.
5. Test that a customer can self-select the right tier without help.

## Output contract
`packaging.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Tiers reflect real segment differences
- Self-selection tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
