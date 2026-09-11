---
name: interaction-pattern-selection
category: design
description: "Reuse an established pattern before inventing one."
output: "pattern-decision.md"
used_by:
  - interaction-designer
---

# Interaction Pattern Selection

`design` · produces `pattern-decision.md` · used by `interaction-designer`

Reuse an established pattern before inventing one.

## Procedure
1. Identify the interaction problem in general terms before reaching for a solution.
2. Check the design system and platform conventions for an existing pattern.
3. Judge a novel pattern against the learning cost it imposes on every user.
4. If inventing, define the pattern properly so it can be reused and documented.
5. Record the decision so the next designer does not re-litigate it.

## Output contract
`pattern-decision.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Existing pattern checked before invention
- Novel patterns justified against learning cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.
