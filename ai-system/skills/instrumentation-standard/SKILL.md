---
name: instrumentation-standard
category: engineering
description: "Define how the system reports on itself."
output: "instrumentation-standard.md"
used_by:
  - observability-agent
---

# Instrumentation Standard

**Category:** `engineering` · **Output artifact:** `instrumentation-standard.md`

## What this skill does
Define how the system reports on itself.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `observability-agent`.

## Procedure
1. Define the naming convention for metrics, logs, and spans.
2. Require a correlation identifier propagated across all boundaries.
3. Define the required attributes on every telemetry type.
4. Specify what must never be emitted: secrets and personal data.
5. Make the standard easy to follow with a shared library.

## Output contract
Write `instrumentation-standard.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** instrumentation-standard
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
- Correlation propagated across boundaries
- Forbidden fields specified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
