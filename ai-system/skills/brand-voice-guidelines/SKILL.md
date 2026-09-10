---
name: brand-voice-guidelines
category: gtm
description: "Define how the company sounds, with examples."
output: "voice-guidelines.md"
used_by:
  - brand-narrative-agent
---

# Brand Voice Guidelines

**Category:** `gtm` · **Output artifact:** `voice-guidelines.md`

## What this skill does
Define how the company sounds, with examples.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-narrative-agent`.

## Procedure
1. State the personality in three adjectives and what each rules out.
2. Give side-by-side examples of what we say and what we never say.
3. Define the rules for jargon, humour, and claims.
4. Cover the hard cases: outages, price rises, and bad news.
5. Make it short enough to be used rather than filed.

## Output contract
Write `voice-guidelines.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** brand-voice-guidelines
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
- Side-by-side examples included
- Hard cases covered
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
