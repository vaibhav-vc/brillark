---
name: ask-framing
category: council
description: "Make a request specific enough to be acted on."
output: "ask.md"
used_by:
  - investor-reporting-agent
---

# Ask Framing

`council` · produces `ask.md` · used by `investor-reporting-agent`

Make a request specific enough to be acted on.

## Procedure
1. State exactly what you need: a decision, an introduction, or a resource.
2. Name the person or role who can provide it.
3. State why it matters and what it unblocks.
4. State the deadline and what happens without it.
5. Make it small enough that saying yes is easy.

## Output contract
`ask.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Names the specific person or role
- Deadline and consequence stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
