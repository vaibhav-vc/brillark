---
name: legal-risk-register
category: legal
description: "Track legal exposure in one place."
output: "legal-risk-register.md"
used_by:
  - general-counsel-agent
---

# Legal Risk Register

**Category:** `legal` · **Output artifact:** `legal-risk-register.md`

## What this skill does
Track legal exposure in one place.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `general-counsel-agent`.

## Procedure
1. Record each exposure with the activity that creates it.
2. Rate likelihood and potential consequence.
3. Record the current mitigation and its owner.
4. Distinguish exposures we can manage from those needing counsel.
5. Review when entering a new market or launching a new capability.

## Output contract
Write `legal-risk-register.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** legal-risk-register
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
- Exposure tied to a specific activity
- Counsel-grade items separated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
