---
name: prompt-variant-generation
category: improvement
description: "Produce candidate instruction changes worth testing."
output: "variants.md"
used_by:
  - prompt-optimizer
---

# Prompt Variant Generation

**Category:** `improvement` · **Output artifact:** `variants.md`

## What this skill does
Produce candidate instruction changes worth testing.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prompt-optimizer`.

## Procedure
1. Start from a diagnosed failure and the step that allowed it.
2. Generate variants that differ in one dimension each.
3. Include a variant that removes instruction rather than adding it.
4. State the hypothesis for each variant before testing.
5. Discard variants whose hypothesis you cannot state.

## Output contract
Write `variants.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prompt-variant-generation
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- One dimension changed per variant
- A removal variant always included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
