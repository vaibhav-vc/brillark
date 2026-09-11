---
name: research-agenda-setting
category: research
description: "Choose which unknowns to resolve this period."
output: "research-agenda.md"
used_by:
  - chief-research-officer-agent
---

# Research Agenda Setting

`research` · produces `research-agenda.md` · used by `chief-research-officer-agent`

Choose which unknowns to resolve this period.

## Procedure
1. List the unknowns blocking decisions, from the register.
2. Estimate the value of resolving each and the cost of doing so.
3. Fund the ones that unblock decisions; decline the merely interesting.
4. State the deliberate non-priorities explicitly.
5. Review against decisions actually unblocked, not research produced.

## Output contract
`research-agenda.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Deliberate non-priorities stated
- Reviewed on decisions unblocked, not output volume
- The output states its confidence grade and names the evidence behind every load-bearing claim.
