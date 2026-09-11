---
name: assistive-technology-testing
category: design
description: "Test with the tools people actually use, not only with automated checkers."
output: "at-test-report.md"
used_by:
  - accessibility-designer
---

# Assistive Technology Testing

**Category:** `design` · **Output artifact:** `at-test-report.md`

## What this skill does
Test with the tools people actually use, not only with automated checkers.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `accessibility-designer`.

## Procedure
1. Test with at least one screen reader on each supported platform.
2. Navigate the whole flow by keyboard alone.
3. Check that state changes and errors are announced.
4. Test at high zoom and with increased text size.
5. Record findings with the technology, version, and exact steps.

## Output contract
Write `at-test-report.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** assistive-technology-testing
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Real assistive technology used
- Findings reproducible with named tool and steps
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
