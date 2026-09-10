---
name: packaging-design
category: finance
description: "Group capabilities into tiers customers can choose between."
output: "packaging.md"
used_by:
  - pricing-strategist
---

# Packaging Design

**Category:** `finance` · **Output artifact:** `packaging.md`

## What this skill does
Group capabilities into tiers customers can choose between.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `pricing-strategist`.

## Procedure
1. Identify the dimensions on which customer needs genuinely differ.
2. Build tiers around those differences, not around feature counts.
3. Ensure each tier is coherent for the segment it targets.
4. Design the upgrade trigger so growth naturally moves customers up.
5. Test that a customer can self-select the right tier without help.

## Output contract
Write `packaging.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** packaging-design
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
- Tiers reflect real segment differences
- Self-selection tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
