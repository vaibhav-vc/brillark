---
name: partnership-review
category: gtm
description: "Judge whether a partnership is producing and act on the answer."
output: "partnership-review.md"
used_by:
  - partnership-bd-agent
---

# Partnership Review

**Category:** `gtm` · **Output artifact:** `partnership-review.md`

## What this skill does
Judge whether a partnership is producing and act on the answer.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `partnership-bd-agent`.

## Procedure
1. Compare actual results against the metrics in the agreement.
2. Separate partner underperformance from thesis failure.
3. Check whether our side delivered its commitments before blaming theirs.
4. Decide: invest more, maintain, restructure, or exit.
5. Close dead partnerships explicitly rather than letting them decay.

## Output contract
Write `partnership-review.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** partnership-review
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
- Our own delivery assessed first
- Explicit decision, including exit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
