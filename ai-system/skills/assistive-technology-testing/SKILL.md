---
name: assistive-technology-testing
category: design
description: "Test with the tools people actually use, not only with automated checkers."
output: "at-test-report.md"
used_by:
  - accessibility-designer
---

# Assistive Technology Testing

`design` · produces `at-test-report.md` · used by `accessibility-designer`

Test with the tools people actually use, not only with automated checkers.

## Procedure
1. Test with at least one screen reader on each supported platform.
2. Navigate the whole flow by keyboard alone.
3. Check that state changes and errors are announced.
4. Test at high zoom and with increased text size.
5. Record findings with the technology, version, and exact steps.

## Output contract
`at-test-report.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Real assistive technology used
- Findings reproducible with named tool and steps
- The output states its confidence grade and names the evidence behind every load-bearing claim.
