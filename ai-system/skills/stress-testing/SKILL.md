---
name: stress-testing
category: finance
description: "Break the plan deliberately to find where it fails."
output: "stress-test.md"
used_by:
  - scenario-stress-tester
---

# Stress Testing

`finance` · produces `stress-test.md` · used by `scenario-stress-tester`

Break the plan deliberately to find where it fails.

## Procedure
1. Identify the drivers whose failure would be most damaging.
2. Push each to a plausible worst case and observe what breaks first.
3. Combine the shocks that historically occur together.
4. Record the breaking point value for each driver.
5. State the mitigation or the acceptance for each breaking point.

## Output contract
`stress-test.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Breaking point recorded per driver
- Correlated shocks tested together
- The output states its confidence grade and names the evidence behind every load-bearing claim.
