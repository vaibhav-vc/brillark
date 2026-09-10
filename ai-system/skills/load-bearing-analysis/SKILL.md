---
name: load-bearing-analysis
category: council
description: "Determine which assumptions the plan cannot survive without."
output: "load-bearing-report.md"
used_by:
  - council-assumption-auditor
---

# Load Bearing Analysis

**Category:** `council` · **Output artifact:** `load-bearing-report.md`

## What this skill does
Determine which assumptions the plan cannot survive without.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-assumption-auditor`.

## Procedure
1. For each assumption, ask what remains true if it is false.
2. Score how much of the plan collapses in each case.
3. Cross-reference the score against the evidence grade.
4. Flag the high-load, low-evidence assumptions as the critical set.
5. Rank the critical set by the cost of being wrong.

## Output contract
Write `load-bearing-report.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** load-bearing-analysis
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
- Load cross-referenced against evidence grade
- Critical set explicitly ranked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
