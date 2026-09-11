---
name: dead-code-removal
category: engineering
description: "Delete what is no longer used."
output: "removal-record.md"
used_by:
  - tech-debt-refactor-agent
---

# Dead Code Removal

`engineering` · produces `removal-record.md` · used by `tech-debt-refactor-agent`

Delete what is no longer used.

## Procedure
1. Identify unreferenced code, flags, endpoints, and configuration.
2. Verify with runtime data that it is genuinely unused, not just statically unreferenced.
3. Check for external consumers before removing an interface.
4. Remove in a reversible commit rather than commenting out.
5. Confirm nothing broke after a full deployment cycle.

## Output contract
`removal-record.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Runtime evidence of non-use
- External consumers checked first
- The output states its confidence grade and names the evidence behind every load-bearing claim.
