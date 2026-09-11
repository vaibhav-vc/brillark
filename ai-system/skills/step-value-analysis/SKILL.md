---
name: step-value-analysis
category: improvement
description: "Find workflow steps that change no outcome."
output: "step-value.md"
used_by:
  - workflow-optimizer
---

# Step Value Analysis

`improvement` · produces `step-value.md` · used by `workflow-optimizer`

Find workflow steps that change no outcome.

## Procedure
1. For each step, ask what decision or artifact it changes.
2. Check the historical record: did this step ever alter an outcome?
3. Distinguish a step that rarely fires from one that never matters.
4. Flag ceremony steps for removal.
5. Keep steps that are the only evidence for a gate, however rarely they fire.

## Output contract
`step-value.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Rarely-firing distinguished from never-mattering
- Gate-evidence steps protected
- The output states its confidence grade and names the evidence behind every load-bearing claim.
