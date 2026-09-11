---
name: narrative-one-pager
category: strategy
description: "Compress the whole company onto one page a new person could absorb."
output: "one-pager.md"
used_by:
  - ceo-agent
---

# Narrative One Pager

`strategy` · produces `one-pager.md` · used by `ceo-agent`

Compress the whole company onto one page a new person could absorb.

## Procedure
1. State who we serve, what problem, and why it matters.
2. State what we do and why it is different.
3. Include the current stage and the next milestone.
4. Include the numbers that matter most, current as of a stated date.
5. Test it on someone unfamiliar and fix what they misunderstand.

## Output contract
`one-pager.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Tested on an unfamiliar reader
- Numbers dated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
