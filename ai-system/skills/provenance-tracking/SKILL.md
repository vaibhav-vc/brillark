---
name: provenance-tracking
category: memory
description: "Keep every claim traceable to the evidence that produced it."
output: "provenance-record.json"
used_by:
  - context-memory-curator
---

# Provenance Tracking

**Category:** `memory` · **Output artifact:** `provenance-record.json`

## What this skill does
Keep every claim traceable to the evidence that produced it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `context-memory-curator`.

## Procedure
1. Record the author agent, the skill used, and the timestamp on every write.
2. Link to the source artifact, not just to its conclusion.
3. Grade the evidence at the moment of writing.
4. Preserve the chain when a claim is derived from another claim.
5. Refuse to promote a claim to semantic memory without traceable provenance.

## Output contract
Write `provenance-record.json` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** provenance-tracking
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
- Chain preserved through derivations
- No ungraded claims promoted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
