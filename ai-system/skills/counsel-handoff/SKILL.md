---
name: counsel-handoff
category: research
description: "Route a legal question to counsel instead of answering it."
output: "counsel-handoff.md"
used_by:
  - prior-art-researcher
---

# Counsel Handoff

`research` · produces `counsel-handoff.md` · used by `prior-art-researcher`

Route a legal question to counsel instead of answering it.

## Procedure
1. Recognise when a finding has legal consequence: infringement, compliance, liability.
2. Assemble the factual findings without offering a legal conclusion.
3. State the specific question counsel needs to answer.
4. Mark the handoff clearly so no downstream reader treats research as advice.
5. Track the handoff to an answer rather than letting it lapse.

## Output contract
`counsel-handoff.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- No legal conclusion offered
- Handoff tracked to an answer
- The output states its confidence grade and names the evidence behind every load-bearing claim.
