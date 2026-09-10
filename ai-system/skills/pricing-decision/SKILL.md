---
name: pricing-decision
category: finance
description: "Decide what to charge and be able to defend it from both directions."
output: "pricing-decision.md"
used_by:
  - finance-head
  - pricing-strategist
---

# Pricing Decision

**Category:** `finance` · **Output artifact:** `pricing-decision.md`

## What this skill does
Decide what to charge and be able to defend it from both directions.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `finance-head`, `pricing-strategist`.

## Procedure
1. Establish the floor from unit economics and the ceiling from value delivered.
2. Gather willingness-to-pay evidence from real prospects.
3. Choose the position within the band and state the reason.
4. Model the revenue effect at the chosen point, including volume response.
5. Define the migration path for existing customers before changing anything.

## Output contract
Write `pricing-decision.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** pricing-decision
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
- Floor and ceiling both established
- Migration path defined before change
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
