---
name: ip-assignment-check
category: legal
description: "Verify the company actually owns what it built."
output: "ip-assignment-audit.md"
used_by:
  - general-counsel-agent
---

# Ip Assignment Check

**Category:** `legal` · **Output artifact:** `ip-assignment-audit.md`

## What this skill does
Verify the company actually owns what it built.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `general-counsel-agent`.

## Procedure
1. List every contributor: founders, employees, contractors, and agencies.
2. Verify a signed assignment exists for each.
3. Check work created before incorporation is assigned in.
4. Check open-source and third-party components for ownership limits.
5. Close every gap before any diligence event.

## Output contract
Write `ip-assignment-audit.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** ip-assignment-check
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
- Every contributor covered by a signed assignment
- Pre-incorporation work addressed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
