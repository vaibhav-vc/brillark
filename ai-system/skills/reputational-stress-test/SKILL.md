---
name: reputational-stress-test
category: council
description: "Test whether the plan survives public scrutiny."
output: "reputation-test.md"
used_by:
  - council-ethics-and-responsibility
---

# Reputational Stress Test

**Category:** `council` · **Output artifact:** `reputation-test.md`

## What this skill does
Test whether the plan survives public scrutiny.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-ethics-and-responsibility`.

## Procedure
1. Write the most damaging accurate headline this plan could produce.
2. Assess whether we could respond honestly and adequately.
3. Identify which stakeholders would be most damaged by the disclosure.
4. Distinguish 'embarrassing' from 'indefensible' — only one requires a change.
5. Recommend the change or record the accepted exposure.

## Output contract
Write `reputation-test.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** reputational-stress-test
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
- Headline is accurate, not exaggerated
- Indefensible distinguished from embarrassing
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
