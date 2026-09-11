---
name: identity-stress-testing
category: design
description: "Test the identity where it is most likely to fail."
output: "identity-stress.md"
used_by:
  - brand-identity-designer
---

# Identity Stress Testing

`design` · produces `identity-stress.md` · used by `brand-identity-designer`

Test the identity where it is most likely to fail.

## Procedure
1. Render at favicon size and check it still reads.
2. Convert to monochrome and to single-colour print.
3. Test on light, dark, and photographic backgrounds.
4. Test at low resolution and under heavy compression.
5. Fix the system rather than making one-off exceptions.

## Output contract
`identity-stress.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Tested at smallest size and in monochrome
- Fixes applied to the system, not as exceptions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
