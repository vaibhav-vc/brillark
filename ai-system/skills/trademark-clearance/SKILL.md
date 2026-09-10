---
name: trademark-clearance
category: legal
description: "Check a name can actually be used before committing to it."
output: "clearance-memo.md"
used_by:
  - ip-counsel-agent
---

# Trademark Clearance

**Category:** `legal` · **Output artifact:** `clearance-memo.md`

## What this skill does
Check a name can actually be used before committing to it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ip-counsel-agent`.

## Procedure
1. Search registers in every market where the mark will be used.
2. Search common-law and unregistered use, including domains and app stores.
3. Assess similarity in the relevant classes, not just identical matches.
4. Assess the risk of opposition from adjacent marks.
5. Escalate to counsel before launch, not after.

## Output contract
Write `clearance-memo.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** trademark-clearance
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
- Unregistered use searched too
- Cleared before public launch
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
