---
name: component-library-management
category: engineering
description: "Keep the shared component set coherent as it grows."
output: "component-library.md"
used_by:
  - frontend-implementation-agent
---

# Component Library Management

**Category:** `engineering` · **Output artifact:** `component-library.md`

## What this skill does
Keep the shared component set coherent as it grows.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `frontend-implementation-agent`.

## Procedure
1. Require a search for an existing component before a new one is added.
2. Define the criteria a component must meet to be shared.
3. Version and document each component with usage examples.
4. Deprecate duplicates deliberately and migrate usages.
5. Review the library periodically for drift and dead components.

## Output contract
Write `component-library.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** component-library-management
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
- Duplicate check enforced before addition
- Deprecations migrated, not just marked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
