---
name: service-implementation
category: engineering
description: "Build the server-side behaviour to match the contract exactly."
output: "service-code"
used_by:
  - backend-implementation-agent
---

# Service Implementation

**Category:** `engineering` · **Output artifact:** `service-code`

## What this skill does
Build the server-side behaviour to match the contract exactly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `backend-implementation-agent`.

## Procedure
1. Implement against the specification, not against an assumption of intent.
2. Validate every input at the boundary and reject clearly.
3. Make write paths idempotent where retries are possible.
4. Fail loudly and specifically rather than swallowing errors.
5. Instrument the decision points, not just the entry and exit.

## Output contract
Write `service-code` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** service-implementation
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
- Behaviour matches the specification exactly
- Decision points instrumented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
