---
name: memory-retrieval-tuning
category: memory
description: "Make sure the right memory reaches the agent that needs it."
output: "retrieval-quality-report.md"
used_by:
  - context-memory-curator
---

# Memory Retrieval Tuning

**Category:** `memory` · **Output artifact:** `retrieval-quality-report.md`

## What this skill does
Make sure the right memory reaches the agent that needs it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `context-memory-curator`.

## Procedure
1. Sample recent tasks and check which known facts were not retrieved.
2. Diagnose the miss: bad keys, bad chunking, or bad ranking.
3. Adjust retrieval keys and entity links rather than adding more text.
4. Re-run the sample and measure the hit rate change.
5. Record rediscovery incidents as retrieval defects, not agent errors.

## Output contract
Write `retrieval-quality-report.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** memory-retrieval-tuning
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
- Hit rate measured on real tasks
- Rediscovery logged as a retrieval defect
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
