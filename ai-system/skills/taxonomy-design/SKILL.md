---
name: taxonomy-design
category: design
description: "Build the controlled vocabulary the whole organisation uses."
output: "taxonomy.md"
used_by:
  - information-architect
---

# Taxonomy Design

`design` · produces `taxonomy.md` · used by `information-architect`

Build the controlled vocabulary the whole organisation uses.

## Procedure
1. Derive terms from user language in research, not from internal shorthand.
2. Define one term per concept and record the rejected synonyms.
3. Check each term for ambiguity across the product's contexts.
4. Define the rules for adding a term and who approves it.
5. Publish it where product, design, content, and engineering will all see it.

## Output contract
`taxonomy.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- One term per concept with rejected synonyms recorded
- Terms drawn from user language
- The output states its confidence grade and names the evidence behind every load-bearing claim.
