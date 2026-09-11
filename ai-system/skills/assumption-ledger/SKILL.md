---
name: assumption-ledger
category: finance
description: "Collect every assumption that touches money into one auditable list."
output: "assumption-ledger.md"
used_by:
  - council-assumption-auditor
  - finance-head
  - financial-model-builder
---

# Assumption Ledger

`finance` · produces `assumption-ledger.md` · used by `council-assumption-auditor`, `finance-head`, `financial-model-builder`

Collect every assumption that touches money into one auditable list.

## Procedure
1. Extract assumptions from the model, including defaults buried inside formulas.
2. Record the value, the source, the evidence grade, and the owner for each.
3. Score how much of the plan depends on each assumption.
4. Flag high-dependency, low-evidence assumptions as priority tests.
5. Re-review the ledger whenever the model changes materially.

## Output contract
`assumption-ledger.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Assumptions inside formulas surfaced
- Dependency scored per assumption
- The output states its confidence grade and names the evidence behind every load-bearing claim.
