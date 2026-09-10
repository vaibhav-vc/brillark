---
name: remedy-design
category: council
description: "Propose a fix alongside every criticism."
output: "remedy-proposal.md"
used_by:
  - council-ethics-and-responsibility
---

# Remedy Design

**Category:** `council` · **Output artifact:** `remedy-proposal.md`

## What this skill does
Propose a fix alongside every criticism.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-ethics-and-responsibility`.

## Procedure
1. State the finding and the specific harm it causes.
2. Propose at least two remedies at different cost levels.
3. Assess what each remedy costs in effort and in product value.
4. Recommend one and state the trade-off accepted.
5. Verify the remedy would actually eliminate the finding.

## Output contract
Write `remedy-proposal.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** remedy-design
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
- At least two remedy options offered
- Remedy verified against the finding
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
