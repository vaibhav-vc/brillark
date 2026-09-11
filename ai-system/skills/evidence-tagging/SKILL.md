---
name: evidence-tagging
category: market
description: "Mark how much each claim in an artifact is actually supported."
output: "evidence-tags.md"
used_by:
  - business-model-canvas-agent
---

# Evidence Tagging

`market` · produces `evidence-tags.md` · used by `business-model-canvas-agent`

Mark how much each claim in an artifact is actually supported.

## Procedure
1. Tag each claim as measured, sourced, benchmarked, estimated, or guessed.
2. Attach the source reference to every non-guessed tag.
3. Compute the proportion of the artifact resting on guesses.
4. Highlight guessed claims that carry significant weight.
5. Refuse to advance a stage gate on guessed load-bearing claims.

## Output contract
`evidence-tags.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Every claim carries a grade
- Load-bearing guesses highlighted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
