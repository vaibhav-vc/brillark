---
name: interface-copywriting
category: design
description: "Write the words in the product so they do the explaining."
output: "interface-copy.md"
used_by:
  - content-designer
---

# Interface Copywriting

`design` · produces `interface-copy.md` · used by `content-designer`

Write the words in the product so they do the explaining.

## Procedure
1. Write the label for what the user is trying to do, not for what the system does.
2. Front-load the meaningful word so scanning works.
3. Cut every word that does not change the user's next action.
4. Use the vocabulary from research and the glossary.
5. Read it aloud; awkward copy is usually ambiguous copy.

## Output contract
`interface-copy.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Labels named for user intent
- Every word changes the next action
- The output states its confidence grade and names the evidence behind every load-bearing claim.
