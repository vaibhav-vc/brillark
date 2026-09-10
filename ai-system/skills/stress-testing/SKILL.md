---
name: stress-testing
category: finance
description: "Break the plan deliberately to find where it fails."
output: "stress-test.md"
used_by:
  - scenario-stress-tester
---

# Stress Testing

**Category:** `finance` · **Output artifact:** `stress-test.md`

## What this skill does
Break the plan deliberately to find where it fails.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `scenario-stress-tester`.

## Procedure
1. Identify the drivers whose failure would be most damaging.
2. Push each to a plausible worst case and observe what breaks first.
3. Combine the shocks that historically occur together.
4. Record the breaking point value for each driver.
5. State the mitigation or the acceptance for each breaking point.

## Output contract
Write `stress-test.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** stress-testing
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
- Breaking point recorded per driver
- Correlated shocks tested together
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
