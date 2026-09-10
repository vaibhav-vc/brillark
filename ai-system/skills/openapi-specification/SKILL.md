---
name: openapi-specification
category: engineering
description: "Specify the interface formally so clients and tests can be generated."
output: "openapi.yaml"
used_by:
  - api-designer
---

# Openapi Specification

**Category:** `engineering` · **Output artifact:** `openapi.yaml`

## What this skill does
Specify the interface formally so clients and tests can be generated.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `api-designer`.

## Procedure
1. Define every endpoint, parameter, and response schema explicitly.
2. Specify required versus optional fields and their constraints.
3. Document every error response with its condition.
4. Include realistic examples for each operation.
5. Validate the specification and keep it as the source of truth.

## Output contract
Write `openapi.yaml` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** openapi-specification
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
- Error responses fully specified
- Specification is the source of truth
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
