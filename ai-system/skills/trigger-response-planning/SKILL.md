---
name: trigger-response-planning
category: finance
description: "Decide the response before the trigger fires, while thinking is still calm."
output: "trigger-response-plan.md"
used_by:
  - scenario-stress-tester
---

# Trigger Response Planning

`finance` · produces `trigger-response-plan.md` · used by `scenario-stress-tester`

Decide the response before the trigger fires, while thinking is still calm.

## Procedure
1. List the triggers from scenario and stress analysis.
2. For each, define the observable indicator and its threshold.
3. Write the response as specific actions with owners, not intentions.
4. Pre-approve the actions that would otherwise need a slow decision.
5. Instrument the indicators so the trigger is actually detected.

## Output contract
`trigger-response-plan.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Responses are specific actions with owners
- Indicators instrumented, not just named
- The output states its confidence grade and names the evidence behind every load-bearing claim.
