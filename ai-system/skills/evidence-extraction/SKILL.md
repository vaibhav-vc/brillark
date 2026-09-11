---
name: evidence-extraction
category: market
description: "Turn raw conversation into structured, countable evidence."
output: "evidence-extract.md"
used_by:
  - customer-discovery-interviewer
---

# Evidence Extraction

`market` · produces `evidence-extract.md` · used by `customer-discovery-interviewer`

Turn raw conversation into structured, countable evidence.

## Procedure
1. Extract statements about pains, workarounds, spend, and triggers.
2. Tag each with the participant, their segment, and the strength of the signal.
3. Separate what they did from what they said they would do.
4. Keep the original quote alongside the extraction.
5. Load into the evidence store so patterns can be counted.

## Output contract
`evidence-extract.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Behaviour separated from stated intent
- Original quotes retained
- The output states its confidence grade and names the evidence behind every load-bearing claim.
