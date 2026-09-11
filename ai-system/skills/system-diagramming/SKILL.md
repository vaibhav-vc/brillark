---
name: system-diagramming
category: engineering
description: "Draw the system so a newcomer can understand it."
output: "architecture-diagram.md"
used_by:
  - system-architect
---

# System Diagramming

`engineering` · produces `architecture-diagram.md` · used by `system-architect`

Draw the system so a newcomer can understand it.

## Procedure
1. Draw the context level first: who uses it and what it depends on.
2. Draw the container level: the deployable pieces and their protocols.
3. Draw component detail only where it is genuinely needed.
4. Label every arrow with what flows and in which direction.
5. Date the diagram and note what it deliberately omits.

## Output contract
`architecture-diagram.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Arrows labelled with what flows
- Omissions stated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
