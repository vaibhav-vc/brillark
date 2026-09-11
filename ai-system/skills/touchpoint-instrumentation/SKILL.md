---
name: touchpoint-instrumentation
category: design
description: "Measure the service where the customer actually experiences it."
output: "instrumentation-plan.md"
used_by:
  - service-designer
---

# Touchpoint Instrumentation

**Category:** `design` · **Output artifact:** `instrumentation-plan.md`

## What this skill does
Measure the service where the customer actually experiences it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `service-designer`.

## Procedure
1. Identify the touchpoints that most determine the customer's judgement.
2. Define a measure for each: completion, wait, effort, or resolution.
3. Instrument at the touchpoint rather than inferring from downstream data.
4. Set thresholds that trigger investigation.
5. Review the measures against qualitative feedback so numbers stay grounded.

## Output contract
Write `instrumentation-plan.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** touchpoint-instrumentation
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
- Measured at the touchpoint, not inferred
- Thresholds trigger investigation
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
