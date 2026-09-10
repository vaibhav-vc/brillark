---
name: duplicate-detection
category: orchestration
description: "Find out whether this request is already answered or already in flight before spending effort."
output: "duplicate-check.md"
used_by:
  - intake-router
---

# Duplicate Detection

**Category:** `orchestration` · **Output artifact:** `duplicate-check.md`

## What this skill does
Find out whether this request is already answered or already in flight before spending effort.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `intake-router`.

## Procedure
1. Search semantic memory for the same question in different words.
2. Scan the live task graph for overlapping scope.
3. Compare against decision records — the answer may exist as a past decision.
4. If a near-match exists, report the delta rather than the whole answer.
5. Link the new request to the prior work instead of forking it.

## Output contract
Write `duplicate-check.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** duplicate-detection
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
- Memory and task graph both searched
- Near-matches reported as deltas, not reruns
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
