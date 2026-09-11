---
name: brand-voice-guidelines
category: gtm
description: "Define how the company sounds, with examples."
output: "voice-guidelines.md"
used_by:
  - brand-narrative-agent
---

# Brand Voice Guidelines

`gtm` · produces `voice-guidelines.md` · used by `brand-narrative-agent`

Define how the company sounds, with examples.

## Procedure
1. State the personality in three adjectives and what each rules out.
2. Give side-by-side examples of what we say and what we never say.
3. Define the rules for jargon, humour, and claims.
4. Cover the hard cases: outages, price rises, and bad news.
5. Make it short enough to be used rather than filed.

## Output contract
`voice-guidelines.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Side-by-side examples included
- Hard cases covered
- The output states its confidence grade and names the evidence behind every load-bearing claim.
