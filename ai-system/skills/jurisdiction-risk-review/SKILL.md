---
name: jurisdiction-risk-review
category: legal
description: "Treat each new market as a new risk surface."
output: "jurisdiction-review.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Jurisdiction Risk Review

`legal` · produces `jurisdiction-review.md` · used by `council-legal-and-regulatory-critic`

Treat each new market as a new risk surface.

## Procedure
1. Identify what changes legally when entering this jurisdiction.
2. Check data localisation, consumer protection, and tax obligations.
3. Check whether the product or content is restricted there.
4. Assess enforcement reality, not just the written rule.
5. Decide entry, deferral, or geo-blocking explicitly.

## Output contract
`jurisdiction-review.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Enforcement reality assessed
- Explicit entry decision recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
