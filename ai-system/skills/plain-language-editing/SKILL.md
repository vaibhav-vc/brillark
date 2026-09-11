---
name: plain-language-editing
category: design
description: "Cut the text down to what people will actually read."
output: "edited-copy.md"
used_by:
  - content-designer
---

# Plain Language Editing

`design` · produces `edited-copy.md` · used by `content-designer`

Cut the text down to what people will actually read.

## Procedure
1. Replace jargon with the word a new user would use.
2. Break long sentences into one idea each.
3. Prefer active voice and concrete subjects.
4. Check reading level against the target audience.
5. Re-read for what can be deleted entirely rather than shortened.

## Output contract
`edited-copy.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Reading level within target
- Deletion preferred over compression
- The output states its confidence grade and names the evidence behind every load-bearing claim.
