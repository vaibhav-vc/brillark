---
name: copy-comprehension-testing
category: design
description: "Check that people understand the words before shipping them."
output: "comprehension-results.md"
used_by:
  - content-designer
---

# Copy Comprehension Testing

`design` · produces `comprehension-results.md` · used by `content-designer`

Check that people understand the words before shipping them.

## Procedure
1. Show the copy to people outside the team who match the audience.
2. Ask what they think it means and what they would do next.
3. Note every misreading; a single misreading usually predicts many.
4. Rewrite and retest rather than explaining the original.
5. Test the error and empty-state copy too, not just the happy path.

## Output contract
`comprehension-results.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Tested with people outside the team
- Misreadings rewritten and retested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
