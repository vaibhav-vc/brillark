---
name: graph-query-design
category: memory
description: "Build the specific queries agents need rather than a generic search box."
output: "query-catalogue.md"
used_by:
  - knowledge-graph-librarian
---

# Graph Query Design

`memory` · produces `query-catalogue.md` · used by `knowledge-graph-librarian`

Build the specific queries agents need rather than a generic search box.

## Procedure
1. Collect the questions agents actually ask, in their own words.
2. Turn each into a parameterised graph traversal.
3. Return provenance alongside every answer.
4. Cap result size and rank by evidence grade.
5. Retire queries nobody uses and add ones the retrospectives reveal.

## Output contract
`query-catalogue.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Answers carry provenance
- Queries derived from real agent questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
