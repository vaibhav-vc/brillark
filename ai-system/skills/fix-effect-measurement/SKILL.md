---
name: fix-effect-measurement
category: improvement
description: "Measure whether the fix actually helped."
output: "fix-effect.md"
used_by:
  - agent-performance-analyst
---

# Fix Effect Measurement

`improvement` · produces `fix-effect.md` · used by `agent-performance-analyst`

Measure whether the fix actually helped.

## Procedure
1. Record the baseline before the change, on the same cases.
2. Apply one change at a time so the effect is attributable.
3. Re-measure on the same cases after the change.
4. Check for regressions outside the targeted area.
5. Record the delta, and revert changes that did not deliver.

## Output contract
`fix-effect.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Baseline recorded before the change
- Non-delivering changes reverted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
