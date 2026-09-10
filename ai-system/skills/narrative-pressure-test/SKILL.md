---
name: narrative-pressure-test
category: finance
description: "Test whether the fundraising story survives hostile questioning."
output: "narrative-test.md"
used_by:
  - fundraising-strategist
---

# Narrative Pressure Test

**Category:** `finance` · **Output artifact:** `narrative-test.md`

## What this skill does
Test whether the fundraising story survives hostile questioning.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `fundraising-strategist`.

## Procedure
1. List the three questions a skeptical investor would ask first.
2. Answer each honestly, in writing, with evidence.
3. Identify where the honest answer is weak and decide whether to fix it or disclose it.
4. Check for internal contradictions between the narrative and the model.
5. Rehearse the answers until they are short and non-defensive.

## Output contract
Write `narrative-test.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** narrative-pressure-test
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
- Weak answers identified rather than hidden
- Narrative checked against the model
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
