---
name: design-critique-facilitation
category: design
description: "Run critique that improves the work rather than asserting rank."
output: "critique-record.md"
used_by:
  - design-critic
  - design-head
---

# Design Critique Facilitation

`design` · produces `critique-record.md` · used by `design-critic`, `design-head`

Run critique that improves the work rather than asserting rank.

## Procedure
1. Have the designer state the goal, the constraints, and the open questions first.
2. Restrict feedback to the stated goal.
3. Require each objection to name who fails to do what.
4. Separate 'does not work' from 'I would have done it differently'.
5. Close with decisions and owners, not a list of opinions.

## Output contract
`critique-record.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Feedback restricted to the stated goal
- Closes with decisions, not opinions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
