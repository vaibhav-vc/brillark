---
name: error-message-design
category: design
description: "Write errors that let the user recover."
output: "error-catalogue.md"
used_by:
  - content-designer
---

# Error Message Design

`design` · produces `error-catalogue.md` · used by `content-designer`

Write errors that let the user recover.

## Procedure
1. Say what happened in plain language, without codes as the primary message.
2. Say why, when the reason helps the user act.
3. Give the specific next action, and make it doable from where they are.
4. Never blame the user, and never expose internal detail.
5. Keep a reference identifier available but secondary, for support.

## Output contract
`error-catalogue.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Every message offers a doable next action
- No blame and no internal detail exposed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
