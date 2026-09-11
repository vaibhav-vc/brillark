---
name: rapid-prototyping
category: design
description: "Build the testable artifact fast, without building the product."
output: "prototype"
used_by:
  - prototyper
---

# Rapid Prototyping

`design` · produces `prototype` · used by `prototyper`

Build the testable artifact fast, without building the product.

## Procedure
1. Build only the path under test and stub everything else visibly.
2. Use real content and realistic data volumes.
3. Fake the backend rather than building it.
4. Stop as soon as the artifact can answer the question.
5. Note every shortcut so results are not over-read.

## Output contract
`prototype` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Only the tested path built
- Shortcuts documented so results are read correctly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
