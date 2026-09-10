---
name: evidence-grading
category: council
description: "Rate how well each claim is actually supported."
output: "evidence-grades.md"
used_by:
  - council-assumption-auditor
---

# Evidence Grading

**Category:** `council` · **Output artifact:** `evidence-grades.md`

## What this skill does
Rate how well each claim is actually supported.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-assumption-auditor`.

## Procedure
1. Assign one grade per claim: measured, sourced, benchmarked, estimated, or guessed.
2. Require a reference for any grade above 'estimated'.
3. Check that the evidence actually supports the specific claim made.
4. Downgrade claims where the evidence is adjacent but not on point.
5. Report the proportion of the plan resting on guesses.

## Output contract
Write `evidence-grades.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** evidence-grading
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
- Evidence checked for being on point
- Proportion resting on guesses reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
