---
name: channel-test-design
category: gtm
description: "Test a channel cheaply enough that failure is affordable."
output: "channel-test.md"
used_by:
  - gtm-strategist
---

# Channel Test Design

`gtm` · produces `channel-test.md` · used by `gtm-strategist`

Test a channel cheaply enough that failure is affordable.

## Procedure
1. State the hypothesis: this channel reaches this ICP at this cost.
2. Set the budget, the duration, and the sample size needed for a readable result.
3. Define the success threshold and the kill criterion before spending.
4. Instrument attribution before the test starts.
5. Decide on the criterion and record the outcome either way.

## Output contract
`channel-test.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Kill criterion set before spend
- Attribution instrumented in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
