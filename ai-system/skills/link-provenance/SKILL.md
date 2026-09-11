---
name: link-provenance
category: memory
description: "Ensure every graph edge points at the artifact that justifies it."
output: "edge-provenance-report.md"
used_by:
  - knowledge-graph-librarian
---

# Link Provenance

`memory` · produces `edge-provenance-report.md` · used by `knowledge-graph-librarian`

Ensure every graph edge points at the artifact that justifies it.

## Procedure
1. Require a source artifact reference on every relationship write.
2. Reject edges whose justification is another unsourced edge.
3. Record the grade of the justifying evidence on the edge itself.
4. Re-verify edges whose source artifact has been superseded.
5. Prune edges whose justification no longer exists.

## Output contract
`edge-provenance-report.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- No edge without a source artifact
- Superseded justifications re-verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
