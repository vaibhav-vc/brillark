---
name: component-library-management
category: engineering
description: "Keep the shared component set coherent as it grows."
output: "component-library.md"
used_by:
  - frontend-implementation-agent
---

# Component Library Management

`engineering` · produces `component-library.md` · used by `frontend-implementation-agent`

Keep the shared component set coherent as it grows.

## Procedure
1. Require a search for an existing component before a new one is added.
2. Define the criteria a component must meet to be shared.
3. Version and document each component with usage examples.
4. Deprecate duplicates deliberately and migrate usages.
5. Review the library periodically for drift and dead components.

## Output contract
`component-library.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Duplicate check enforced before addition
- Deprecations migrated, not just marked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
