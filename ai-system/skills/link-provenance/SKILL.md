---
name: link-provenance
category: memory
description: "Ensure every graph edge points at the artifact that justifies it."
output: "edge-provenance-report.md"
used_by:
  - knowledge-graph-librarian
---

# Link Provenance

**Category:** `memory` · **Output artifact:** `edge-provenance-report.md`

## What this skill does
Ensure every graph edge points at the artifact that justifies it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-graph-librarian`.

## Procedure
1. Require a source artifact reference on every relationship write.
2. Reject edges whose justification is another unsourced edge.
3. Record the grade of the justifying evidence on the edge itself.
4. Re-verify edges whose source artifact has been superseded.
5. Prune edges whose justification no longer exists.

## Output contract
Write `edge-provenance-report.md` into `workspace/<venture-id>/memory/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** link-provenance
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
- No edge without a source artifact
- Superseded justifications re-verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `memory` category
- Storing a claim without provenance, so nobody can later tell whether to trust it.
- Keeping two contradicting facts because resolving them is inconvenient.
- Treating a stale memory as current because it is well written.
