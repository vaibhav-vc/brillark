---
name: held-out-set-construction
category: improvement
description: "Build a measurement set that stays honest."
output: "held-out-set.md"
used_by:
  - eval-designer
---

# Held Out Set Construction

**Category:** `improvement` · **Output artifact:** `held-out-set.md`

## What this skill does
Build a measurement set that stays honest.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `eval-designer`.

## Procedure
1. Split before any tuning begins, and record the split.
2. Make the held-out set representative of the real task mix.
3. Keep it large enough to detect the effect you care about.
4. Restrict access so it is not consulted during development.
5. Audit periodically for leakage.

## Output contract
Write `held-out-set.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** held-out-set-construction
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
- Split recorded before tuning begins
- Leakage audited periodically
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
