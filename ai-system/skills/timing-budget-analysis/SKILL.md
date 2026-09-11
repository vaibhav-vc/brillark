---
name: timing-budget-analysis
category: hardware
description: "Prove the data arrives when the receiver expects it."
output: "timing-budget.md"
used_by:
  - signal-integrity-engineer
---

# Timing Budget Analysis

`hardware` · produces `timing-budget.md` · used by `signal-integrity-engineer`

Prove the data arrives when the receiver expects it.

## Procedure
1. Build the budget from driver, board, and receiver contributions, including package delay.
2. Include clock skew, jitter, and setup-and-hold requirements.
3. Derive the length-matching requirement from the budget, not from a default.
4. Check the budget at temperature and voltage extremes.
5. Confirm the routed board meets the budget it was constrained to.

## Output contract
`timing-budget.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Package delay and jitter included
- Checked at voltage and temperature extremes
- The output states its confidence grade and names the evidence behind every load-bearing claim.
