---
name: leverage-identification
category: council
description: "Find where a small effort produces an outsized return."
output: "leverage-list.md"
used_by:
  - council-expansion-scout
---

# Leverage Identification

`council` · produces `leverage-list.md` · used by `council-expansion-scout`

Find where a small effort produces an outsized return.

## Procedure
1. List actions whose output is reused many times or by many people.
2. Identify constraints whose removal unblocks several workstreams at once.
3. Look for compounding effects rather than one-time gains.
4. Estimate effort and return for each.
5. Recommend the top two rather than a long list.

## Output contract
`leverage-list.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Compounding effects distinguished from one-off gains
- Recommendation limited to a top few
- The output states its confidence grade and names the evidence behind every load-bearing claim.
