---
name: usability-test-design
category: design
description: "Design a test that produces findings rather than reassurance."
output: "test-plan.md"
used_by:
  - usability-tester
---

# Usability Test Design

`design` · produces `test-plan.md` · used by `usability-tester`

Design a test that produces findings rather than reassurance.

## Procedure
1. Write the tasks as goals the participant would actually have, never as instructions naming the UI.
2. Define the success criterion for each task before recruiting.
3. Recruit to the target segment; wrong participants produce confident wrong findings.
4. Plan five participants per segment per round, and plan the rounds.
5. Prepare what you will not say, so you do not rescue the participant mid-task.

## Output contract
`test-plan.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Tasks stated as goals, not UI instructions
- Success criteria set before recruitment
- The output states its confidence grade and names the evidence behind every load-bearing claim.
