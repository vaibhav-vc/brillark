---
name: design-token-architecture
category: design
description: "Structure tokens so themes, modes, and brands work without rework."
output: "token-architecture.md"
used_by:
  - design-system-architect
---

# Design Token Architecture

`design` · produces `token-architecture.md` · used by `design-system-architect`

Structure tokens so themes, modes, and brands work without rework.

## Procedure
1. Separate primitive values from semantic tokens that name an intent.
2. Name semantic tokens by role — surface, border, text-danger — never by colour.
3. Define the full set for each theme and mode rather than patching one.
4. Define the token for state variations: hover, focus, disabled, selected.
5. Version tokens and define how a change propagates to consumers.

## Output contract
`token-architecture.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Semantic layer named by role, not colour
- Every theme defined in full
- The output states its confidence grade and names the evidence behind every load-bearing claim.
