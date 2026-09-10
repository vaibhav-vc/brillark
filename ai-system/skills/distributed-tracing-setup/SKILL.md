---
name: distributed-tracing-setup
category: engineering
description: "Follow a request across every service it touches."
output: "tracing-setup.md"
used_by:
  - observability-agent
---

# Distributed Tracing Setup

**Category:** `engineering` · **Output artifact:** `tracing-setup.md`

## What this skill does
Follow a request across every service it touches.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `observability-agent`.

## Procedure
1. Propagate trace context across all service and queue boundaries.
2. Instrument the spans that represent real work, not every function.
3. Add attributes that make traces searchable by business identifier.
4. Sample deliberately, keeping all error traces.
5. Verify traces are continuous end to end before relying on them.

## Output contract
Write `tracing-setup.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** distributed-tracing-setup
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
- Context propagated through async boundaries
- Error traces always retained
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
