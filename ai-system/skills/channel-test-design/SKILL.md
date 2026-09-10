---
name: channel-test-design
category: gtm
description: "Test a channel cheaply enough that failure is affordable."
output: "channel-test.md"
used_by:
  - gtm-strategist
---

# Channel Test Design

**Category:** `gtm` · **Output artifact:** `channel-test.md`

## What this skill does
Test a channel cheaply enough that failure is affordable.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `gtm-strategist`.

## Procedure
1. State the hypothesis: this channel reaches this ICP at this cost.
2. Set the budget, the duration, and the sample size needed for a readable result.
3. Define the success threshold and the kill criterion before spending.
4. Instrument attribution before the test starts.
5. Decide on the criterion and record the outcome either way.

## Output contract
Write `channel-test.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** channel-test-design
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
- Kill criterion set before spend
- Attribution instrumented in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
