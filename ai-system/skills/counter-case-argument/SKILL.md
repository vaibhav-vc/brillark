---
name: counter-case-argument
category: council
description: "Argue against the leading option in full."
output: "counter-case.md"
used_by:
  - council-devils-advocate
---

# Counter Case Argument

`council` · produces `counter-case.md` · used by `council-devils-advocate`

Argue against the leading option in full.

## Procedure
1. State the strongest version of the case against, without hedging.
2. Attack the evidence base as well as the reasoning.
3. Show what the recommendation assumes that may not hold.
4. Name what the room may be overlooking because it agrees.
5. Concede explicitly if the case survives; a rubber-stamp adversary is worthless.

## Output contract
`counter-case.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Argued without hedging
- Explicit concession when the case survives
- The output states its confidence grade and names the evidence behind every load-bearing claim.
