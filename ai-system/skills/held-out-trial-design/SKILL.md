---
name: held-out-trial-design
category: improvement
description: "Design the trial so its result means something."
output: "trial-design.md"
used_by:
  - prompt-optimizer
---

# Held Out Trial Design

**Category:** `improvement` · **Output artifact:** `trial-design.md`

## What this skill does
Design the trial so its result means something.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prompt-optimizer`.

## Procedure
1. Split cases into a tuning set and a held-out set before generating variants.
2. Never look at held-out cases while designing a variant.
3. Fix the adoption threshold and the sample size in advance.
4. Define what counts as a regression elsewhere.
5. Record the design before running anything.

## Output contract
Write `trial-design.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** held-out-trial-design
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
- Held-out set untouched during variant design
- Threshold fixed before the trial
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
