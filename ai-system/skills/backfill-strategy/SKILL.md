---
name: backfill-strategy
category: engineering
description: "Populate new structures over existing data safely."
output: "backfill-plan.md"
used_by:
  - data-model-designer
---

# Backfill Strategy

**Category:** `engineering` · **Output artifact:** `backfill-plan.md`

## What this skill does
Populate new structures over existing data safely.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-model-designer`.

## Procedure
1. Estimate the data volume and the time the backfill will take.
2. Design it to be resumable and idempotent.
3. Throttle to protect production load.
4. Track progress and verify a sample for correctness as it runs.
5. Define how new writes are handled while the backfill is in flight.

## Output contract
Write `backfill-plan.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** backfill-strategy
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
- Resumable and idempotent by design
- In-flight writes handled explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
