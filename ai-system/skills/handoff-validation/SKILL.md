---
name: handoff-validation
category: orchestration
description: "Check that arriving work is complete before accepting it."
output: "handoff-record.md"
used_by:
  - handoff-coordinator
---

# Handoff Validation

**Category:** `orchestration` · **Output artifact:** `handoff-record.md`

## What this skill does
Check that arriving work is complete before accepting it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `handoff-coordinator`.

## Procedure
1. Check the artifact exists and matches the agreed format.
2. Verify the definition of done was met, item by item.
3. Confirm assumptions and open questions are stated.
4. Reject immediately with the specific gap if anything is missing.
5. Record acceptance, so responsibility transfers cleanly.

## Output contract
Write `handoff-record.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** handoff-validation
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
- Rejection names the specific gap
- Acceptance recorded explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
