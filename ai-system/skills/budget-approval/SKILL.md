---
name: budget-approval
category: finance
description: "Approve or refuse spend with a stated reason either way."
output: "budget-decision.md"
used_by:
  - cfo-agent
---

# Budget Approval

`finance` · produces `budget-decision.md` · used by `cfo-agent`

Approve or refuse spend with a stated reason either way.

## Procedure
1. Require a written case: amount, purpose, expected outcome, and alternative.
2. Check the request against the budget envelope and the runway impact.
3. Compare against the next-best use of the same money.
4. Approve, refuse, or approve with conditions — always in writing.
5. When refusing, state the condition that would turn it into a yes.

## Output contract
`budget-decision.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Compared against next-best use
- Refusals state their reversal condition
- The output states its confidence grade and names the evidence behind every load-bearing claim.
