---
name: finding-deduplication
category: council
description: "Merge findings that are the same objection in different words."
output: "deduplicated-findings.md"
used_by:
  - council-synthesis-arbiter
---

# Finding Deduplication

**Category:** `council` · **Output artifact:** `deduplicated-findings.md`

## What this skill does
Merge findings that are the same objection in different words.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-synthesis-arbiter`.

## Procedure
1. Group findings by the underlying failure they describe.
2. Merge duplicates, keeping the clearest statement and all evidence.
3. Preserve distinct aspects rather than flattening them.
4. Credit all raising critics so the signal strength stays visible.
5. Report the merged count as an indicator of consensus.

## Output contract
Write `deduplicated-findings.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** finding-deduplication
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
- Merged on underlying failure, not wording
- Signal strength preserved
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
