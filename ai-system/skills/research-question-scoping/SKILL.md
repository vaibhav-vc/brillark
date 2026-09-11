---
name: research-question-scoping
category: research
description: "Narrow a request until a finite search could actually answer it."
output: "research-question.md"
used_by:
  - research-analyst
---

# Research Question Scoping

`research` · produces `research-question.md` · used by `research-analyst`

Narrow a request until a finite search could actually answer it.

## Procedure
1. Name the decision the answer will inform and who makes it.
2. Restate the question so a specific observation would settle it.
3. Split compound questions; a question with an 'and' is two searches.
4. State what you are deliberately narrowing away, so the requester can object now.
5. Agree the required evidence grade and the stopping point before searching.

## Output contract
`research-question.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Question answerable by a finite search
- What was narrowed away is recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
