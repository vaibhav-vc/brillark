---
name: product-requirements-doc
category: product
description: "Write requirements an engineer can build and a tester can verify."
output: "prd.md"
used_by:
  - cpo-agent
  - product-requirements-agent
---

# Product Requirements Doc

`product` · produces `prd.md` · used by `cpo-agent`, `product-requirements-agent`

Write requirements an engineer can build and a tester can verify.

## Procedure
1. Open with the problem and the evidence for it, never with a solution.
2. Define the users and the specific situation the feature addresses.
3. State the success signal and how it will be measured.
4. Describe the required behaviour, including the unhappy paths.
5. List what is explicitly out of scope and why.

## Output contract
`prd.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Opens with an evidenced problem
- Out-of-scope list explicit
- The output states its confidence grade and names the evidence behind every load-bearing claim.
