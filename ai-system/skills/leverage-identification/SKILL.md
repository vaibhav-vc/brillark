---
name: leverage-identification
category: council
description: "Find where a small effort produces an outsized return."
output: "leverage-list.md"
used_by:
  - council-expansion-scout
---

# Leverage Identification

**Category:** `council` · **Output artifact:** `leverage-list.md`

## What this skill does
Find where a small effort produces an outsized return.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-expansion-scout`.

## Procedure
1. List actions whose output is reused many times or by many people.
2. Identify constraints whose removal unblocks several workstreams at once.
3. Look for compounding effects rather than one-time gains.
4. Estimate effort and return for each.
5. Recommend the top two rather than a long list.

## Output contract
Write `leverage-list.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** leverage-identification
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
- Compounding effects distinguished from one-off gains
- Recommendation limited to a top few
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
