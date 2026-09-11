---
name: state-specification
category: design
description: "Specify every state a view can be in, so none is discovered in production."
output: "state-spec.md"
used_by:
  - interaction-designer
---

# State Specification

`design` · produces `state-spec.md` · used by `interaction-designer`

Specify every state a view can be in, so none is discovered in production.

## Procedure
1. Specify empty, loading, partial, error, and success for every view.
2. Design the first-use empty state as an onboarding opportunity, not a blank box.
3. Specify what the error state says and what action it offers.
4. Define the loading behaviour by expected duration, not one spinner for everything.
5. Specify the partial state where some data arrived and some did not.

## Output contract
`state-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- All five states specified per view
- Error states offer a recovery action
- The output states its confidence grade and names the evidence behind every load-bearing claim.
