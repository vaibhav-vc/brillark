---
name: differentiation-analysis
category: market
description: "State the reason a customer would switch, or admit there is none."
output: "differentiation.md"
used_by:
  - competitor-intel-analyst
---

# Differentiation Analysis

`market` · produces `differentiation.md` · used by `competitor-intel-analyst`

State the reason a customer would switch, or admit there is none.

## Procedure
1. List what we do that alternatives do not, from the customer's perspective.
2. Test each difference against 'would this alone justify switching?'
3. Assess how easily each difference could be copied and how fast.
4. Identify the difference that compounds rather than the one that is merely present.
5. State the differentiation in one sentence a customer would recognise.

## Output contract
`differentiation.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Stated as a switching reason
- Copyability of each difference assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
