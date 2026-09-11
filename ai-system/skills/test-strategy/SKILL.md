---
name: test-strategy
category: engineering
description: "Decide what to test, at what level, and why."
output: "test-strategy.md"
used_by:
  - engineering-head
  - qa-test-strategist
---

# Test Strategy

`engineering` · produces `test-strategy.md` · used by `engineering-head`, `qa-test-strategist`

Decide what to test, at what level, and why.

## Procedure
1. Identify the areas where failure would be most costly.
2. Assign each risk to the cheapest level that can catch it.
3. Define what will deliberately not be tested and the risk accepted.
4. Define the gating suite and its maximum runtime.
5. Review after escaped defects to see which level should have caught them.

## Output contract
`test-strategy.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Coverage driven by failure cost
- Untested areas and accepted risk stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
