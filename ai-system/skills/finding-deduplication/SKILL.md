---
name: finding-deduplication
category: council
description: "Merge findings that are the same objection in different words."
output: "deduplicated-findings.md"
used_by:
  - council-synthesis-arbiter
---

# Finding Deduplication

`council` · produces `deduplicated-findings.md` · used by `council-synthesis-arbiter`

Merge findings that are the same objection in different words.

## Procedure
1. Group findings by the underlying failure they describe.
2. Merge duplicates, keeping the clearest statement and all evidence.
3. Preserve distinct aspects rather than flattening them.
4. Credit all raising critics so the signal strength stays visible.
5. Report the merged count as an indicator of consensus.

## Output contract
`deduplicated-findings.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Merged on underlying failure, not wording
- Signal strength preserved
- The output states its confidence grade and names the evidence behind every load-bearing claim.
