---
name: goal-anchored-feedback
category: design
description: "Give feedback that can be acted on."
output: "feedback-notes.md"
used_by:
  - design-critic
---

# Goal Anchored Feedback

`design` · produces `feedback-notes.md` · used by `design-critic`

Give feedback that can be acted on.

## Procedure
1. Restate the goal before commenting.
2. Describe the problem you observed, not the solution you prefer.
3. Say who it affects and in what situation.
4. Rate how much it matters against the goal.
5. Offer a direction rather than a redesign.

## Output contract
`feedback-notes.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Problem described rather than solution prescribed
- Impact tied to the goal
- The output states its confidence grade and names the evidence behind every load-bearing claim.
