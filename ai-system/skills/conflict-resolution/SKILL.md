---
name: conflict-resolution
category: council
description: "Resolve a direct disagreement between critics."
output: "conflict-resolution.md"
used_by:
  - council-synthesis-arbiter
---

# Conflict Resolution

`council` · produces `conflict-resolution.md` · used by `council-synthesis-arbiter`

Resolve a direct disagreement between critics.

## Procedure
1. State both positions precisely, in their own strongest form.
2. Identify whether they disagree on facts, values, or predictions.
3. For factual disagreements, find the evidence that settles it.
4. For predictive disagreements, define the observation that would settle it later.
5. Decide on evidence, never by averaging or splitting the difference.

## Output contract
`conflict-resolution.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Type of disagreement identified
- Decided on evidence, not by compromise
- The output states its confidence grade and names the evidence behind every load-bearing claim.
