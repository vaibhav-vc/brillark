---
name: capital-plan
category: finance
description: "Decide how much money to raise, when, and against what milestone."
output: "capital-plan.md"
used_by:
  - cfo-agent
---

# Capital Plan

**Category:** `finance` · **Output artifact:** `capital-plan.md`

## What this skill does
Decide how much money to raise, when, and against what milestone.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cfo-agent`.

## Procedure
1. Define the milestone that justifies the next round.
2. Compute the capital needed to reach it plus a buffer for slippage.
3. Set the raise start date at least nine months before cash-out.
4. Model the dilution at plausible valuations.
5. Define the alternative if the raise does not happen.

## Output contract
Write `capital-plan.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** capital-plan
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
- Raise anchored to a milestone
- Non-raise alternative defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
