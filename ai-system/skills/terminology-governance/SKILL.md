---
name: terminology-governance
category: design
description: "Keep one name per concept across every surface."
output: "terminology-record.md"
used_by:
  - content-designer
---

# Terminology Governance

`design` · produces `terminology-record.md` · used by `content-designer`

Keep one name per concept across every surface.

## Procedure
1. Check the glossary before introducing any new term.
2. Add new terms with their definition and rejected alternatives.
3. Audit surfaces for drift between the glossary and reality.
4. Coordinate renames across product, docs, marketing, and support together.
5. Record the rename so support can recognise the old term.

## Output contract
`terminology-record.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Glossary checked before new terms
- Renames coordinated across all surfaces
- The output states its confidence grade and names the evidence behind every load-bearing claim.
