---
name: search-strategy-design
category: research
description: "Plan the search so coverage is deliberate rather than accidental."
output: "search-plan.md"
used_by:
  - research-analyst
---

# Search Strategy Design

`research` · produces `search-plan.md` · used by `research-analyst`

Plan the search so coverage is deliberate rather than accidental.

## Procedure
1. List the source types that could hold the answer: primary data, literature, filings, practitioners.
2. Write the terms the field actually uses, not the terms we use internally.
3. Plan for the opposite: search for evidence against the expected answer too.
4. Set the stopping rule — typically when new sources stop changing the answer.
5. Record what you searched and did not find; absence is a result.

## Output contract
`search-plan.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Search includes terms for the opposite conclusion
- Stopping rule set before searching
- The output states its confidence grade and names the evidence behind every load-bearing claim.
