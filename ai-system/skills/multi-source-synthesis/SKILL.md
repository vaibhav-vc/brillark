---
name: multi-source-synthesis
category: research
description: "Combine many sources into one answer without inventing consensus."
output: "synthesis.md"
used_by:
  - research-analyst
---

# Multi Source Synthesis

`research` · produces `synthesis.md` · used by `research-analyst`

Combine many sources into one answer without inventing consensus.

## Procedure
1. Group sources by what they actually claim, not by whether they agree with you.
2. Weight by evidence grade and independence, not by how recently you read them.
3. Preserve genuine disagreement explicitly rather than averaging it away.
4. Distinguish a claim repeated by many outlets from a claim independently established.
5. State the answer, then the confidence, then the dissenting sources.

## Output contract
`synthesis.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Disagreement preserved, not averaged
- Repetition distinguished from independent confirmation
- The output states its confidence grade and names the evidence behind every load-bearing claim.
