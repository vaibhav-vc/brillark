---
name: prompt-variant-generation
category: improvement
description: "Produce candidate instruction changes worth testing."
output: "variants.md"
used_by:
  - prompt-optimizer
---

# Prompt Variant Generation

`improvement` · produces `variants.md` · used by `prompt-optimizer`

Produce candidate instruction changes worth testing.

## Procedure
1. Start from a diagnosed failure and the step that allowed it.
2. Generate variants that differ in one dimension each.
3. Include a variant that removes instruction rather than adding it.
4. State the hypothesis for each variant before testing.
5. Discard variants whose hypothesis you cannot state.

## Output contract
`variants.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- One dimension changed per variant
- A removal variant always included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
