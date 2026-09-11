---
name: asset-library-management
category: design
description: "Keep brand and product assets available in the formats people need."
output: "asset-library.md"
used_by:
  - brand-identity-designer
---

# Asset Library Management

**Category:** `design` · **Output artifact:** `asset-library.md`

## What this skill does
Keep brand and product assets available in the formats people need.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-identity-designer`.

## Procedure
1. Provide each asset in the formats and resolutions actually used.
2. Name files predictably so the right one is chosen.
3. Version assets and mark the current one clearly.
4. Remove superseded assets so they stop appearing in production.
5. Track where assets are used so a change can be propagated.

## Output contract
Write `asset-library.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** asset-library-management
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
- Formats match real usage
- Superseded assets removed, not just marked
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
