---
name: security-review
category: engineering
description: "Review a change for security consequences before it ships."
output: "security-review.md"
used_by:
  - ciso-agent
---

# Security Review

**Category:** `engineering` · **Output artifact:** `security-review.md`

## What this skill does
Review a change for security consequences before it ships.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ciso-agent`.

## Procedure
1. Check what new data, surface, or privilege the change introduces.
2. Review authentication, authorisation, and input handling on new paths.
3. Check dependencies added and their provenance.
4. Verify secrets and configuration are handled correctly.
5. Block on unmitigated critical findings; record any accepted risk.

## Output contract
Write `security-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** security-review
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
- New surface explicitly identified
- Critical findings block the release
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
