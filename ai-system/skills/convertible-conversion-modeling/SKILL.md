---
name: convertible-conversion-modeling
category: finance
description: "Model what convertible instruments turn into under real terms."
output: "conversion-model.md"
used_by:
  - cap-table-steward
---

# Convertible Conversion Modeling

**Category:** `finance` · **Output artifact:** `conversion-model.md`

## What this skill does
Model what convertible instruments turn into under real terms.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cap-table-steward`.

## Procedure
1. List each instrument with its cap, discount, interest, and maturity.
2. Model conversion at the priced round under each instrument's mechanics.
3. Apply the more favourable of cap or discount per instrument, as the terms specify.
4. Show the resulting ownership and the effect on the new investor's stake.
5. Test edge cases: low valuations, high valuations, and a non-qualifying round.

## Output contract
Write `conversion-model.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** convertible-conversion-modeling
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
- Each instrument's mechanics applied individually
- Edge-case valuations tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
