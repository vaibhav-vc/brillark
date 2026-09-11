---
name: sensitivity-analysis
category: finance
description: "Find which inputs actually move the outcome."
output: "sensitivity-table.md"
used_by:
  - council-economics-skeptic
  - scenario-stress-tester
  - unit-economics-architect
---

# Sensitivity Analysis

`finance` · produces `sensitivity-table.md` · used by `council-economics-skeptic`, `scenario-stress-tester`, `unit-economics-architect`

Find which inputs actually move the outcome.

## Procedure
1. Flex one input at a time across a realistic range.
2. Record the outcome change per input and rank by impact.
3. Identify the inputs where a small error produces a large outcome swing.
4. Cross-check that the high-impact inputs are the best-evidenced ones; if not, that is the finding.
5. Present as a ranked table, not a wall of scenarios.

## Output contract
`sensitivity-table.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Ranges realistic, not symmetric by default
- High-impact inputs cross-checked against evidence grade
- The output states its confidence grade and names the evidence behind every load-bearing claim.
