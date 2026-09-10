---
name: technical-due-diligence
category: strategy
description: "Keep the technical story ready for anyone who will examine it."
output: "tech-diligence-pack.md"
used_by:
  - cto-agent
---

# Technical Due Diligence

**Category:** `strategy` · **Output artifact:** `tech-diligence-pack.md`

## What this skill does
Keep the technical story ready for anyone who will examine it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cto-agent`.

## Procedure
1. Assemble architecture, security posture, and dependency inventory.
2. Document known technical debt and the plan for it — hiding it fails diligence.
3. Verify IP ownership and licence compliance.
4. Prepare scaling evidence: what has been tested and to what level.
5. Keep it current so a raise or a deal never waits on engineering.

## Output contract
Write `tech-diligence-pack.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** technical-due-diligence
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
- Known debt disclosed with a plan
- IP and licence position verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
