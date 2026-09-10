---
name: dunning-flow-design
category: finance
description: "Recover failed payments without losing the customer."
output: "dunning-flow.md"
used_by:
  - billing-systems-designer
---

# Dunning Flow Design

**Category:** `finance` · **Output artifact:** `dunning-flow.md`

## What this skill does
Recover failed payments without losing the customer.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `billing-systems-designer`.

## Procedure
1. Map the failure reasons and which are recoverable.
2. Design the retry schedule around bank behaviour, not arbitrary intervals.
3. Write the customer communication for each stage, escalating in clarity not aggression.
4. Define the grace period and exactly what access is retained.
5. Measure recovery rate by failure reason and tune the sequence.

## Output contract
Write `dunning-flow.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dunning-flow-design
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
- Retry schedule matches failure reason
- Recovery measured by reason
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
