---
name: workflow-change-measurement
category: improvement
description: "Prove the workflow change helped."
output: "workflow-change.md"
used_by:
  - workflow-optimizer
---

# Workflow Change Measurement

`improvement` · produces `workflow-change.md` · used by `workflow-optimizer`

Prove the workflow change helped.

## Procedure
1. Record cycle time, rework rate, and escaped defects before the change.
2. Change one workflow at a time.
3. Measure the same three after, over comparable volume.
4. Check none of the three got worse.
5. Revert if any did, and record why.

## Output contract
`workflow-change.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- One workflow changed at a time
- Reverted if any of the three measures worsened
- The output states its confidence grade and names the evidence behind every load-bearing claim.
