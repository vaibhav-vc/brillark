---
name: load-testing
category: engineering
description: "Find the system's real limits under realistic conditions."
output: "load-test-report.md"
used_by:
  - performance-engineer
---

# Load Testing

**Category:** `engineering` · **Output artifact:** `load-test-report.md`

## What this skill does
Find the system's real limits under realistic conditions.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `performance-engineer`.

## Procedure
1. Model realistic traffic shape, including think time and mixed operations.
2. Use production-like data volumes; small datasets hide the real bottlenecks.
3. Ramp to failure to find the breaking point, not just to the target.
4. Observe the whole system during the test, not only the response times.
5. Record the limit, the failure mode, and the first component to break.

## Output contract
Write `load-test-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** load-testing
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
- Ramped to failure, not just to target
- Failure mode recorded, not just the limit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
