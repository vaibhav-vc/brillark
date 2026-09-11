---
name: circular-logic-detection
category: council
description: "Find reasoning that assumes what it is trying to prove."
output: "circularity-report.md"
used_by:
  - council-economics-skeptic
---

# Circular Logic Detection

`council` · produces `circularity-report.md` · used by `council-economics-skeptic`

Find reasoning that assumes what it is trying to prove.

## Procedure
1. Trace each key output back through its inputs to their origins.
2. Look for inputs that depend on the output — revenue funding the spend that creates the revenue.
3. Check whether growth assumptions are justified by the growth plan itself.
4. Identify metrics defined in terms of each other.
5. Report the loop explicitly and propose an independent anchor.

## Output contract
`circularity-report.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Loops traced to their origin
- Independent anchor proposed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
