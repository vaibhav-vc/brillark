---
name: message-testing
category: gtm
description: "Find out whether a message works before paying to distribute it."
output: "message-test.md"
used_by:
  - cmo-agent
  - positioning-messaging-agent
---

# Message Testing

**Category:** `gtm` · **Output artifact:** `message-test.md`

## What this skill does
Find out whether a message works before paying to distribute it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cmo-agent`, `positioning-messaging-agent`.

## Procedure
1. Prepare at least two genuinely different messages, not variations.
2. Test with people who match the ICP, not with colleagues.
3. Measure comprehension and relevance before measuring preference.
4. Ask what they think it does and who it is for — misunderstanding is the main failure.
5. Choose on evidence and record why the loser lost.

## Output contract
Write `message-test.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** message-testing
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
- Comprehension tested before preference
- Tested with ICP-matching participants
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
