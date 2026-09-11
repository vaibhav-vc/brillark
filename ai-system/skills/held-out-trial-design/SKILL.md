---
name: held-out-trial-design
category: improvement
description: "Design the trial so its result means something."
output: "trial-design.md"
used_by:
  - prompt-optimizer
---

# Held Out Trial Design

`improvement` · produces `trial-design.md` · used by `prompt-optimizer`

Design the trial so its result means something.

## Procedure
1. Split cases into a tuning set and a held-out set before generating variants.
2. Never look at held-out cases while designing a variant.
3. Fix the adoption threshold and the sample size in advance.
4. Define what counts as a regression elsewhere.
5. Record the design before running anything.

## Output contract
`trial-design.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Held-out set untouched during variant design
- Threshold fixed before the trial
- The output states its confidence grade and names the evidence behind every load-bearing claim.
