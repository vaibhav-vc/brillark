---
name: from-scratch-reconstruction
category: council
description: "Rebuild the plan from the irreducible requirements alone."
output: "reconstruction.md"
used_by:
  - council-first-principles
---

# From Scratch Reconstruction

`council` · produces `reconstruction.md` · used by `council-first-principles`

Rebuild the plan from the irreducible requirements alone.

## Procedure
1. Start from the reduced requirement set, ignoring the existing plan.
2. Design the simplest approach that satisfies all of them.
3. Compare against the proposal and enumerate every difference.
4. For each difference, ask which version is justified.
5. Recommend adopting the differences that survive scrutiny.

## Output contract
`reconstruction.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Built without reference to the existing plan
- Every difference examined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
