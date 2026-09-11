---
name: conformance-auditing
category: design
description: "Audit a shipped surface against the conformance target."
output: "conformance-audit.md"
used_by:
  - accessibility-designer
---

# Conformance Auditing

**Category:** `design` · **Output artifact:** `conformance-audit.md`

## What this skill does
Audit a shipped surface against the conformance target.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `accessibility-designer`.

## Procedure
1. Audit against the specific criteria at the target level, not a general impression.
2. Combine automated checks with manual and assistive technology testing.
3. Record each failure with the criterion, the location, and the evidence.
4. Rate severity by user impact, not by how easy it is to fix.
5. Produce a remediation plan with owners and dates.

## Output contract
Write `conformance-audit.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** conformance-auditing
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
- Manual testing combined with automated checks
- Each failure tied to a specific criterion
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
