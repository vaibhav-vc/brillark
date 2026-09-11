---
name: channel-handoff-design
category: design
description: "Design the moments where the service moves between channels or between machine and human."
output: "handoff-spec.md"
used_by:
  - service-designer
---

# Channel Handoff Design

**Category:** `design` · **Output artifact:** `handoff-spec.md`

## What this skill does
Design the moments where the service moves between channels or between machine and human.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `service-designer`.

## Procedure
1. Identify every handoff point in the journey.
2. Specify what context travels across, so the customer never repeats themselves.
3. Define who owns the customer at each stage.
4. Design what the customer sees and hears during the transition.
5. Define the fallback when the handoff fails.

## Output contract
Write `handoff-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** channel-handoff-design
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
- Context travels so customers never repeat themselves
- Fallback defined per handoff
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
