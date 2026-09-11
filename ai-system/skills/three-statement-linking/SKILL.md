---
name: three-statement-linking
category: finance
description: "Connect profit and loss, balance sheet, and cash flow so the model cannot lie."
output: "three-statement-model.md"
used_by:
  - financial-model-builder
---

# Three Statement Linking

`finance` · produces `three-statement-model.md` · used by `financial-model-builder`

Connect profit and loss, balance sheet, and cash flow so the model cannot lie.

## Procedure
1. Build the P&L from the revenue and cost drivers.
2. Flow net income into retained earnings on the balance sheet.
3. Derive cash flow from net income plus non-cash adjustments and working capital movements.
4. Check that the balance sheet balances in every period; an imbalance is a bug, not a rounding issue.
5. Verify the closing cash in the cash flow matches the balance sheet cash exactly.

## Output contract
`three-statement-model.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Balance sheet balances every period
- Closing cash reconciles across statements
- The output states its confidence grade and names the evidence behind every load-bearing claim.
