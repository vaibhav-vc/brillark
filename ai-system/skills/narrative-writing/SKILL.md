---
name: narrative-writing
category: gtm
description: "Write the story of why the company exists and why it matters."
output: "narrative.md"
used_by:
  - brand-narrative-agent
  - investor-reporting-agent
---

# Narrative Writing

`gtm` · produces `narrative.md` · used by `brand-narrative-agent`, `investor-reporting-agent`

Write the story of why the company exists and why it matters.

## Procedure
1. Open with the tension in the world, not with the product.
2. Explain what changed that makes a new answer possible.
3. Position the company as the answer, specifically and provably.
4. Make the customer the protagonist, not the company.
5. Check every claim is one the product can actually back.

## Output contract
`narrative.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Opens with tension, not product
- Every claim backed by the product
- The output states its confidence grade and names the evidence behind every load-bearing claim.
