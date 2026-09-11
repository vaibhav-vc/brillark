---
name: service-recovery-design
category: design
description: "Design what happens when the service fails the customer."
output: "recovery-plan.md"
used_by:
  - service-designer
---

# Service Recovery Design

**Category:** `design` · **Output artifact:** `recovery-plan.md`

## What this skill does
Design what happens when the service fails the customer.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `service-designer`.

## Procedure
1. List the failure modes the customer will actually experience.
2. Design the acknowledgement: fast, specific, and without blame.
3. Define the remedy and who is empowered to give it without escalation.
4. Design the follow-through so the customer knows it was fixed.
5. Measure recovery satisfaction, not just failure frequency.

## Output contract
Write `recovery-plan.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** service-recovery-design
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
- Front-line empowered to remedy without escalation
- Recovery satisfaction measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
