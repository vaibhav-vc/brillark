---
name: financial-model-build
category: finance
description: "Build the integrated model where every money assumption meets its consequences."
output: "financial-model.md"
used_by:
  - finance-head
  - financial-model-builder
---

# Financial Model Build

`finance` · produces `financial-model.md` · used by `finance-head`, `financial-model-builder`

Build the integrated model where every money assumption meets its consequences.

## Procedure
1. Separate inputs, calculations, and outputs into distinct sheets or modules.
2. Drive revenue from volume, price, and retention rather than a growth percentage.
3. Model headcount by role and start date, with fully loaded costs.
4. Link the cash statement properly — profit is not cash.
5. Expose every assumption on the input sheet with an owner and a source.

## Output contract
`financial-model.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- No hard-coded numbers inside formulas
- Every input has an owner and a source
- The output states its confidence grade and names the evidence behind every load-bearing claim.
