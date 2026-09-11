---
name: narrative-pressure-test
category: finance
description: "Test whether the fundraising story survives hostile questioning."
output: "narrative-test.md"
used_by:
  - fundraising-strategist
---

# Narrative Pressure Test

`finance` · produces `narrative-test.md` · used by `fundraising-strategist`

Test whether the fundraising story survives hostile questioning.

## Procedure
1. List the three questions a skeptical investor would ask first.
2. Answer each honestly, in writing, with evidence.
3. Identify where the honest answer is weak and decide whether to fix it or disclose it.
4. Check for internal contradictions between the narrative and the model.
5. Rehearse the answers until they are short and non-defensive.

## Output contract
`narrative-test.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Weak answers identified rather than hidden
- Narrative checked against the model
- The output states its confidence grade and names the evidence behind every load-bearing claim.
