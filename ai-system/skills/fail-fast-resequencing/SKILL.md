---
name: fail-fast-resequencing
category: improvement
description: "Move the cheap disconfirming step earlier."
output: "resequencing.md"
used_by:
  - workflow-optimizer
---

# Fail Fast Resequencing

`improvement` · produces `resequencing.md` · used by `workflow-optimizer`

Move the cheap disconfirming step earlier.

## Procedure
1. Identify the step most likely to stop the work.
2. Check whether it depends on anything that must come first.
3. Move it as early as its dependencies allow.
4. Measure the work avoided when it fires.
5. Re-check the sequence after each change.

## Output contract
`resequencing.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Dependencies verified before moving a step
- Work avoided measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
