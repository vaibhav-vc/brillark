---
name: entity-structure-review
category: legal
description: "Check the corporate structure fits what the business actually does."
output: "entity-review.md"
used_by:
  - general-counsel-agent
---

# Entity Structure Review

**Category:** `legal` · **Output artifact:** `entity-review.md`

## What this skill does
Check the corporate structure fits what the business actually does.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `general-counsel-agent`.

## Procedure
1. Confirm the entity type and jurisdiction match the business model and funding plan.
2. Check whether operations create presence in other jurisdictions.
3. Review whether subsidiaries are needed or merely add cost.
4. Check that governance documents match actual practice.
5. Flag structural changes needing professional advice.

## Output contract
Write `entity-review.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** entity-structure-review
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
- Operational presence assessed per jurisdiction
- Documents checked against actual practice
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
