---
name: message-testing
category: gtm
description: "Find out whether a message works before paying to distribute it."
output: "message-test.md"
used_by:
  - cmo-agent
  - positioning-messaging-agent
---

# Message Testing

`gtm` · produces `message-test.md` · used by `cmo-agent`, `positioning-messaging-agent`

Find out whether a message works before paying to distribute it.

## Procedure
1. Prepare at least two genuinely different messages, not variations.
2. Test with people who match the ICP, not with colleagues.
3. Measure comprehension and relevance before measuring preference.
4. Ask what they think it does and who it is for — misunderstanding is the main failure.
5. Choose on evidence and record why the loser lost.

## Output contract
`message-test.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Comprehension tested before preference
- Tested with ICP-matching participants
- The output states its confidence grade and names the evidence behind every load-bearing claim.
