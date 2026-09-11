---
name: sprawl-resistance
category: improvement
description: "Recommend against filling a gap when that is the right answer."
output: "non-proposal.md"
used_by:
  - capability-gap-scout
---

# Sprawl Resistance

`improvement` · produces `non-proposal.md` · used by `capability-gap-scout`

Recommend against filling a gap when that is the right answer.

## Procedure
1. Compare the cost of the gap against the cost of the addition.
2. Check whether the gap is genuinely recurring or a one-off.
3. Check whether an existing agent could absorb it within its charter.
4. Record the explicit non-proposal with the reasoning.
5. Re-examine only when new evidence arrives.

## Output contract
`non-proposal.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Explicit non-proposals recorded with reasoning
- Re-examination gated on new evidence
- The output states its confidence grade and names the evidence behind every load-bearing claim.
