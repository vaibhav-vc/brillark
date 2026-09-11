---
name: content-modeling
category: design
description: "Define the content types and their relationships before designing pages."
output: "content-model.md"
used_by:
  - information-architect
---

# Content Modeling

`design` · produces `content-model.md` · used by `information-architect`

Define the content types and their relationships before designing pages.

## Procedure
1. Identify the content types and the fields each genuinely needs.
2. Define the relationships between types and their cardinality.
3. Separate content from presentation so it can be reused across surfaces.
4. Define which fields are required and what happens when optional ones are absent.
5. Check the model against every surface that will consume it.

## Output contract
`content-model.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Content separated from presentation
- Absent-optional-field behaviour defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
