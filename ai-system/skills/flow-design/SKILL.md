---
name: flow-design
category: design
description: "Design the complete path through a task, including the ways it goes wrong."
output: "flow-spec.md"
used_by:
  - interaction-designer
---

# Flow Design

`design` · produces `flow-spec.md` · used by `interaction-designer`

Design the complete path through a task, including the ways it goes wrong.

## Procedure
1. Map the entry points; users rarely arrive at step one.
2. Design the happy path, then every branch off it.
3. Design interruption and re-entry: what happens if they leave halfway.
4. Specify what each step needs from the user and what it gives back.
5. Identify the step most likely to be abandoned and reduce its cost.

## Output contract
`flow-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Entry, interruption, and re-entry all designed
- Every branch specified, not just the happy path
- The output states its confidence grade and names the evidence behind every load-bearing claim.
