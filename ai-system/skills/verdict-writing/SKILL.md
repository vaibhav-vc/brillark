---
name: verdict-writing
category: council
description: "Produce the decision-grade output of a review."
output: "council-verdict.md"
used_by:
  - council-director
  - council-synthesis-arbiter
---

# Verdict Writing

**Category:** `council` · **Output artifact:** `council-verdict.md`

## What this skill does
Produce the decision-grade output of a review.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-director`, `council-synthesis-arbiter`.

## Procedure
1. State the overall verdict: approve, approve with conditions, or reject.
2. List blockers with owner, acceptance criterion, and failure scenario.
3. List improvements separately from blockers.
4. Record dissent verbatim, including minority positions.
5. State the deadline and who confirms the blockers are cleared.

## Output contract
Write `council-verdict.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** verdict-writing
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
- Blockers have owners and acceptance criteria
- Dissent recorded verbatim
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
