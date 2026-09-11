---
name: research-repository-lookup
category: research
description: "Check what the organisation already knows before spending on finding out."
output: "repository-check.md"
used_by:
  - research-analyst
---

# Research Repository Lookup

`research` · produces `repository-check.md` · used by `research-analyst`

Check what the organisation already knows before spending on finding out.

## Procedure
1. Search the repository by question, entity, and decision, not just by keyword.
2. Check whether an existing finding answers the question or merely touches it.
3. Check the finding's date and whether its conditions still hold.
4. Report a partial match as a delta to establish, not as a fresh question.
5. Record the lookup so repeated misses expose a retrieval problem.

## Output contract
`repository-check.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Partial matches reported as deltas
- Currency of existing findings checked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
