---
name: scope-boundary-definition
category: product
description: "Draw the line around what this work includes."
output: "scope.md"
used_by:
  - product-requirements-agent
---

# Scope Boundary Definition

**Category:** `product` · **Output artifact:** `scope.md`

## What this skill does
Draw the line around what this work includes.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `product-requirements-agent`.

## Procedure
1. List what is in scope, concretely.
2. List what is out of scope and why each exclusion is safe.
3. Identify the adjacent work this depends on or enables.
4. Name the person who may change the boundary.
5. Record boundary changes as decisions, not as drift.

## Output contract
Write `scope.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** scope-boundary-definition
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
- Exclusions justified individually
- Boundary changes recorded as decisions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
