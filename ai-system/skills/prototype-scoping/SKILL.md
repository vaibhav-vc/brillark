---
name: prototype-scoping
category: design
description: "Be explicit about what the prototype proves and what it fakes."
output: "prototype-scope.md"
used_by:
  - prototyper
---

# Prototype Scoping

`design` · produces `prototype-scope.md` · used by `prototyper`

Be explicit about what the prototype proves and what it fakes.

## Procedure
1. List what is real and what is simulated.
2. State the questions the prototype cannot answer.
3. Warn testers and stakeholders before they see it.
4. Set the boundary for feedback so critique stays on the question.
5. Record the scope alongside the results.

## Output contract
`prototype-scope.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Faked elements listed explicitly
- Unanswerable questions stated up front
- The output states its confidence grade and names the evidence behind every load-bearing claim.
