---
name: prototype-fidelity-selection
category: design
description: "Choose the cheapest fidelity that answers the question."
output: "fidelity-decision.md"
used_by:
  - prototyper
---

# Prototype Fidelity Selection

`design` · produces `fidelity-decision.md` · used by `prototyper`

Choose the cheapest fidelity that answers the question.

## Procedure
1. State the question the prototype must answer.
2. Match fidelity: sketch for structure, clickable for flow, coded for feel and performance.
3. Reject higher fidelity than the question requires.
4. Estimate build time and cap it before starting.
5. Confirm the chosen fidelity can actually produce the answer.

## Output contract
`fidelity-decision.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Fidelity justified by the question
- Build time capped in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
