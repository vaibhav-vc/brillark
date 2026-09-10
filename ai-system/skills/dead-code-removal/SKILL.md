---
name: dead-code-removal
category: engineering
description: "Delete what is no longer used."
output: "removal-record.md"
used_by:
  - tech-debt-refactor-agent
---

# Dead Code Removal

**Category:** `engineering` · **Output artifact:** `removal-record.md`

## What this skill does
Delete what is no longer used.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tech-debt-refactor-agent`.

## Procedure
1. Identify unreferenced code, flags, endpoints, and configuration.
2. Verify with runtime data that it is genuinely unused, not just statically unreferenced.
3. Check for external consumers before removing an interface.
4. Remove in a reversible commit rather than commenting out.
5. Confirm nothing broke after a full deployment cycle.

## Output contract
Write `removal-record.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dead-code-removal
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
- Runtime evidence of non-use
- External consumers checked first
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
