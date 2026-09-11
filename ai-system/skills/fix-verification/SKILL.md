---
name: fix-verification
category: design
description: "Confirm the fix actually fixed it."
output: "retest-report.md"
used_by:
  - usability-tester
---

# Fix Verification

**Category:** `design` · **Output artifact:** `retest-report.md`

## What this skill does
Confirm the fix actually fixed it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `usability-tester`.

## Procedure
1. Retest the same task with fresh participants from the same segment.
2. Compare against the prior round's success rate and error count.
3. Check whether the fix created a new problem elsewhere in the flow.
4. Close the finding only when the retest passes.
5. Record the before and after so the change's value is visible.

## Output contract
Write `retest-report.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** fix-verification
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
- Retested with fresh participants
- Closure requires a passing retest
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
