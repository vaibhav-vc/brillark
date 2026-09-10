---
name: idempotency-design
category: engineering
description: "Make retries safe."
output: "idempotency-design.md"
used_by:
  - api-designer
  - backend-implementation-agent
---

# Idempotency Design

**Category:** `engineering` · **Output artifact:** `idempotency-design.md`

## What this skill does
Make retries safe.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `api-designer`, `backend-implementation-agent`.

## Procedure
1. Identify every operation a client might retry.
2. Define the idempotency key and its scope.
3. Store the result so a repeat returns the original outcome, not a new one.
4. Define the retention period for idempotency records.
5. Test duplicate submission explicitly, including concurrent duplicates.

## Output contract
Write `idempotency-design.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** idempotency-design
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
- Repeat returns the original result
- Concurrent duplicates tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
