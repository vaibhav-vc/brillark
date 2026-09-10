---
name: pre-mortem
category: council
description: "Assume the venture failed and reconstruct how."
output: "pre-mortem.md"
used_by:
  - chief-risk-officer-agent
  - council-risk-and-failure-modes
---

# Pre Mortem

**Category:** `council` · **Output artifact:** `pre-mortem.md`

## What this skill does
Assume the venture failed and reconstruct how.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-risk-officer-agent`, `council-risk-and-failure-modes`.

## Procedure
1. Set the scene: it is twelve months later and this failed.
2. Write the story of the failure in specific steps.
3. Trace back to the earliest point the failure was detectable.
4. Identify which failures were recoverable and which were not.
5. Propose an early indicator for each failure path.

## Output contract
Write `pre-mortem.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** pre-mortem
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
- Failure written as a specific narrative
- Earliest detection point identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
