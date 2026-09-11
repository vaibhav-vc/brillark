---
name: moderation-discipline
category: design
description: "Run the session without contaminating the data."
output: "session-notes.md"
used_by:
  - usability-tester
---

# Moderation Discipline

`design` · produces `session-notes.md` · used by `usability-tester`

Run the session without contaminating the data.

## Procedure
1. Explain that you are testing the product, not the participant, and mean it.
2. Ask what they expect to happen before they act.
3. Sit on your hands: never point, never hint, never explain the interface.
4. When they ask for help, ask what they would do if you were not there.
5. Save your explanation for the debrief, after all tasks are finished.

## Output contract
`session-notes.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- No hints or rescues during tasks
- Expectations captured before each action
- The output states its confidence grade and names the evidence behind every load-bearing claim.
