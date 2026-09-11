---
name: definition-of-done-writing
category: orchestration
description: "Write a completion condition that can be checked by someone other than the author."
output: "definition-of-done.md"
used_by:
  - planning-decomposer
---

# Definition Of Done Writing

`orchestration` · produces `definition-of-done.md` · used by `planning-decomposer`

Write a completion condition that can be checked by someone other than the author.

## Procedure
1. State the artifact that must exist, by name and location.
2. State the properties it must have, each independently checkable.
3. Include the review or validation that must have passed.
4. Exclude anything subjective — 'high quality' is not a condition.
5. Have the receiving agent confirm the DoD is sufficient before work begins.

## Output contract
`definition-of-done.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Every condition independently checkable
- Receiver confirmed sufficiency in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
