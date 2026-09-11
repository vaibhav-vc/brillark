---
name: architecture-decision-record
category: engineering
description: "Record a technical decision with the alternatives and the trade-offs."
output: "adr.md"
used_by:
  - cto-agent
  - engineering-head
  - system-architect
---

# Architecture Decision Record

`engineering` · produces `adr.md` · used by `cto-agent`, `engineering-head`, `system-architect`

Record a technical decision with the alternatives and the trade-offs.

## Procedure
1. State the decision and its status in one line.
2. Describe the context: the forces and constraints in play.
3. List the options considered, with the genuine case for each.
4. State the decision and the consequences accepted, including negative ones.
5. Name what would make this decision wrong and worth revisiting.

## Output contract
`adr.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- At least two genuine alternatives recorded
- Negative consequences stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
