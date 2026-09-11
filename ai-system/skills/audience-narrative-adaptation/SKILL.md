---
name: audience-narrative-adaptation
category: gtm
description: "Tell the same story to customers, investors, and candidates without contradicting yourself."
output: "narrative-variants.md"
used_by:
  - brand-narrative-agent
---

# Audience Narrative Adaptation

`gtm` · produces `narrative-variants.md` · used by `brand-narrative-agent`

Tell the same story to customers, investors, and candidates without contradicting yourself.

## Procedure
1. Identify the spine that must not change across audiences.
2. For each audience, identify what they need to believe and what they fear.
3. Adapt emphasis and evidence, never the underlying claims.
4. Check the versions side by side for contradictions.
5. Update all versions together when the strategy changes.

## Output contract
`narrative-variants.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Spine identical across versions
- Versions checked side by side
- The output states its confidence grade and names the evidence behind every load-bearing claim.
