---
name: ui-implementation
category: engineering
description: "Build the interface to the acceptance criteria, including the hard states."
output: "ui-code"
used_by:
  - frontend-implementation-agent
---

# Ui Implementation

`engineering` · produces `ui-code` · used by `frontend-implementation-agent`

Build the interface to the acceptance criteria, including the hard states.

## Procedure
1. Implement against acceptance criteria, not against the mock alone.
2. Reuse existing components before creating new ones.
3. Handle loading, empty, and error states as first-class work.
4. Meet accessibility requirements while building, not afterwards.
5. Measure the bundle impact and justify any new dependency.

## Output contract
`ui-code` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Reuse checked before creation
- Accessibility built in, not retrofitted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
