---
name: step-concreteness-review
category: improvement
description: "Check every step can actually be followed."
output: "concreteness-review.md"
used_by:
  - skill-refiner
---

# Step Concreteness Review

`improvement` · produces `concreteness-review.md` · used by `skill-refiner`

Check every step can actually be followed.

## Procedure
1. Read each step and ask what you would literally do.
2. Flag steps that state a principle rather than an action.
3. Flag steps whose completion cannot be checked.
4. Rewrite flagged steps as observable actions.
5. Verify a different agent can follow the result without asking.

## Output contract
`concreteness-review.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Principles disguised as steps flagged
- Verified by someone who did not write it
- The output states its confidence grade and names the evidence behind every load-bearing claim.
