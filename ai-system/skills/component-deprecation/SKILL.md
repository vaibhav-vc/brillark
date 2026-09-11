---
name: component-deprecation
category: design
description: "Remove a component without stranding the people using it."
output: "deprecation-plan.md"
used_by:
  - design-system-architect
---

# Component Deprecation

`design` · produces `deprecation-plan.md` · used by `design-system-architect`

Remove a component without stranding the people using it.

## Procedure
1. Announce the deprecation with the replacement and a migration example.
2. Instrument usage so remaining consumers are known, not guessed.
3. Set a removal date with enough time for consumers to migrate.
4. Help migrate the largest consumers rather than waiting for them.
5. Remove it only when usage reaches zero, and confirm afterwards.

## Output contract
`deprecation-plan.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Usage instrumented, not guessed
- Removal only at zero usage
- The output states its confidence grade and names the evidence behind every load-bearing claim.
