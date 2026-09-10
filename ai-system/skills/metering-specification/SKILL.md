---
name: metering-specification
category: finance
description: "Define the billable event precisely enough that nobody disputes the invoice."
output: "metering-spec.md"
used_by:
  - billing-systems-designer
---

# Metering Specification

**Category:** `finance` · **Output artifact:** `metering-spec.md`

## What this skill does
Define the billable event precisely enough that nobody disputes the invoice.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `billing-systems-designer`.

## Procedure
1. Define the event, its unit, and the exact moment it counts.
2. Specify deduplication and idempotency for retried events.
3. Define late-arriving and out-of-order event handling.
4. Specify aggregation windows and rounding rules.
5. Define the customer-visible usage view so disputes can be self-resolved.

## Output contract
Write `metering-spec.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** metering-specification
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
- Deduplication and late events specified
- Customer-visible usage defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
