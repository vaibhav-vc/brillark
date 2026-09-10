---
name: invention-disclosure
category: legal
description: "Capture inventions while the detail still exists."
output: "invention-disclosure.md"
used_by:
  - ip-counsel-agent
---

# Invention Disclosure

**Category:** `legal` · **Output artifact:** `invention-disclosure.md`

## What this skill does
Capture inventions while the detail still exists.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ip-counsel-agent`.

## Procedure
1. Record what the invention does and the problem it solves.
2. Record what makes it non-obvious compared to existing approaches.
3. Record the date of conception and first reduction to practice.
4. Record the contributors accurately; inventorship is a legal question.
5. Route to counsel for filing or trade-secret decision.

## Output contract
Write `invention-disclosure.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** invention-disclosure
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
- Non-obviousness articulated
- Contributors recorded accurately
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
