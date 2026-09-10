---
name: dashboard-design
category: engineering
description: "Build dashboards that answer a specific question."
output: "dashboard-spec.md"
used_by:
  - observability-agent
---

# Dashboard Design

**Category:** `engineering` · **Output artifact:** `dashboard-spec.md`

## What this skill does
Build dashboards that answer a specific question.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `observability-agent`.

## Procedure
1. State the one question the dashboard answers before building it.
2. Show the metric, its target, and its trend together.
3. Order panels by the sequence a person would investigate.
4. Remove panels nobody looks at during real incidents.
5. Name the audience and the decision it supports.

## Output contract
Write `dashboard-spec.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dashboard-design
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
- One named question per dashboard
- Unused panels removed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
