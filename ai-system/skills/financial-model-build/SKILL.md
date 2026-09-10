---
name: financial-model-build
category: finance
description: "Build the integrated model where every money assumption meets its consequences."
output: "financial-model.md"
used_by:
  - finance-head
  - financial-model-builder
---

# Financial Model Build

**Category:** `finance` · **Output artifact:** `financial-model.md`

## What this skill does
Build the integrated model where every money assumption meets its consequences.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `finance-head`, `financial-model-builder`.

## Procedure
1. Separate inputs, calculations, and outputs into distinct sheets or modules.
2. Drive revenue from volume, price, and retention rather than a growth percentage.
3. Model headcount by role and start date, with fully loaded costs.
4. Link the cash statement properly — profit is not cash.
5. Expose every assumption on the input sheet with an owner and a source.

## Output contract
Write `financial-model.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** financial-model-build
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
- No hard-coded numbers inside formulas
- Every input has an owner and a source
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
