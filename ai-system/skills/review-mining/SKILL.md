---
name: review-mining
category: market
description: "Learn from what customers already say publicly about the alternatives."
output: "review-analysis.md"
used_by:
  - competitor-intel-analyst
---

# Review Mining

`market` · produces `review-analysis.md` · used by `competitor-intel-analyst`

Learn from what customers already say publicly about the alternatives.

## Procedure
1. Collect reviews, forum threads, and support discussions across alternatives.
2. Code complaints and praise into themes rather than reading anecdotally.
3. Count theme frequency and note severity.
4. Identify unmet needs that appear repeatedly across products.
5. Quote directly; paraphrase loses the customer's own language.

## Output contract
`review-analysis.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Themes counted, not just noticed
- Direct quotes preserved
- The output states its confidence grade and names the evidence behind every load-bearing claim.
