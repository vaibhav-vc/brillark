---
name: service-blueprinting
category: design
description: "Map the whole service, including everything the customer never sees."
output: "service-blueprint.md"
used_by:
  - service-designer
---

# Service Blueprinting

**Category:** `design` · **Output artifact:** `service-blueprint.md`

## What this skill does
Map the whole service, including everything the customer never sees.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `service-designer`.

## Procedure
1. Lay out the customer actions across the journey.
2. Add the front-stage touchpoints they interact with.
3. Add the back-stage actions and systems that make each possible.
4. Mark the lines of visibility and internal interaction.
5. Identify where a front-stage promise depends on an unreliable back-stage step.

## Output contract
Write `service-blueprint.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** service-blueprinting
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
- Back-stage mapped alongside front-stage
- Fragile front-stage promises identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
