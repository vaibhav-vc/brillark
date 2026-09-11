---
name: relevance-assessment
category: research
description: "Judge honestly whether prior work is actually the same problem."
output: "relevance-notes.md"
used_by:
  - prior-art-researcher
---

# Relevance Assessment

`research` · produces `relevance-notes.md` · used by `prior-art-researcher`

Judge honestly whether prior work is actually the same problem.

## Procedure
1. Compare the problem solved, not the vocabulary used.
2. Check the constraints: scale, cost, environment, and users.
3. Identify what the prior work assumed that we cannot.
4. Rate relevance explicitly rather than implying it by inclusion.
5. Exclude superficially similar work with a stated reason.

## Output contract
`relevance-notes.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Compared on problem, not vocabulary
- Exclusions stated with reasons
- The output states its confidence grade and names the evidence behind every load-bearing claim.
