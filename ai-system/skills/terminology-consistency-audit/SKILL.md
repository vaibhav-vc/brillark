---
name: terminology-consistency-audit
category: gtm
description: "Make sure one concept has one name everywhere."
output: "terminology-audit.md"
used_by:
  - positioning-messaging-agent
---

# Terminology Consistency Audit

**Category:** `gtm` · **Output artifact:** `terminology-audit.md`

## What this skill does
Make sure one concept has one name everywhere.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `positioning-messaging-agent`.

## Procedure
1. Inventory the terms used across product, docs, site, and sales material.
2. Find concepts with multiple names and names with multiple meanings.
3. Choose the canonical term using customer language.
4. Update every surface and record the decision in the glossary.
5. Re-audit after each major release.

## Output contract
Write `terminology-audit.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** terminology-consistency-audit
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
- One canonical term per concept
- Customer language preferred over internal
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
