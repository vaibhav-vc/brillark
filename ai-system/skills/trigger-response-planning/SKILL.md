---
name: trigger-response-planning
category: finance
description: "Decide the response before the trigger fires, while thinking is still calm."
output: "trigger-response-plan.md"
used_by:
  - scenario-stress-tester
---

# Trigger Response Planning

**Category:** `finance` · **Output artifact:** `trigger-response-plan.md`

## What this skill does
Decide the response before the trigger fires, while thinking is still calm.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `scenario-stress-tester`.

## Procedure
1. List the triggers from scenario and stress analysis.
2. For each, define the observable indicator and its threshold.
3. Write the response as specific actions with owners, not intentions.
4. Pre-approve the actions that would otherwise need a slow decision.
5. Instrument the indicators so the trigger is actually detected.

## Output contract
Write `trigger-response-plan.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** trigger-response-planning
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
- Responses are specific actions with owners
- Indicators instrumented, not just named
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
