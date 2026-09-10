---
name: memory-write-standard
category: memory
description: "Enforce the structure that makes a memory retrievable months later."
output: "memory-record.json"
used_by:
  - context-memory-curator
---

# Memory Write Standard

**Category:** `memory` · **Output artifact:** `memory-record.json`

## What this skill does
Enforce the structure that makes a memory retrievable months later.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `context-memory-curator`.

## Procedure
1. Classify the memory: episodic, semantic, procedural, or decision.
2. Write the claim as a standalone statement that needs no surrounding context.
3. Attach provenance: author agent, evidence, date, and confidence grade.
4. Add retrieval keys — entities, venture stage, and domain.
5. Validate against the schema and reject the write if it fails.

## Output contract
Write `memory-record.json` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** memory-write-standard
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
- Claim is standalone and context-free
- Provenance and confidence attached
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
