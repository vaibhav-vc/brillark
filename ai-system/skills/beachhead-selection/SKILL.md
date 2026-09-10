---
name: beachhead-selection
category: gtm
description: "Choose the one segment to win first."
output: "beachhead.md"
used_by:
  - gtm-strategist
---

# Beachhead Selection

**Category:** `gtm` · **Output artifact:** `beachhead.md`

## What this skill does
Choose the one segment to win first.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `gtm-strategist`.

## Procedure
1. Score candidate segments on pain intensity, reachability, budget, and reference value.
2. Prefer a segment small enough to dominate and connected enough to spread.
3. Check that winning it creates a credible path to the next segment.
4. Commit to it explicitly and state what is being deferred.
5. Define what 'won' means before starting.

## Output contract
Write `beachhead.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** beachhead-selection
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
- Segment small enough to dominate
- Definition of won stated in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
