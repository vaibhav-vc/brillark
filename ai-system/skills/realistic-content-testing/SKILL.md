---
name: realistic-content-testing
category: design
description: "Test the design with the content it will actually hold."
output: "content-stress-results.md"
used_by:
  - prototyper
  - visual-designer
---

# Realistic Content Testing

`design` · produces `content-stress-results.md` · used by `prototyper`, `visual-designer`

Test the design with the content it will actually hold.

## Procedure
1. Use real data, including the longest, shortest, and missing cases.
2. Test with the volume real users have, not with three tidy items.
3. Check every supported language, including the ones that expand text.
4. Check names, numbers, and dates in their real formats.
5. Fix what breaks before the design is called complete.

## Output contract
`content-stress-results.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Longest, shortest, and missing cases tested
- Real data volumes used
- The output states its confidence grade and names the evidence behind every load-bearing claim.
