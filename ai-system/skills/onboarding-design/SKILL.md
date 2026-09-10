---
name: onboarding-design
category: gtm
description: "Get a new customer to their first real value quickly."
output: "onboarding-design.md"
used_by:
  - customer-success-agent
---

# Onboarding Design

**Category:** `gtm` · **Output artifact:** `onboarding-design.md`

## What this skill does
Get a new customer to their first real value quickly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-success-agent`.

## Procedure
1. Define first value concretely — the specific moment the customer gets something they wanted.
2. Map every step between signup and that moment.
3. Remove or defer every step that is not required to reach it.
4. Instrument the time to first value and the drop-off per step.
5. Design the recovery path for customers who stall.

## Output contract
Write `onboarding-design.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** onboarding-design
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
- First value defined concretely
- Time to first value instrumented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
