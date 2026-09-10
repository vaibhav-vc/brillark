---
name: infrastructure-as-code
category: engineering
description: "Define infrastructure so it can be rebuilt exactly."
output: "infrastructure-code"
used_by:
  - infra-devops-agent
---

# Infrastructure As Code

**Category:** `engineering` · **Output artifact:** `infrastructure-code`

## What this skill does
Define infrastructure so it can be rebuilt exactly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `infra-devops-agent`.

## Procedure
1. Express every resource in code; nothing created by hand survives.
2. Keep environment differences in configuration, not in divergent code.
3. Store state securely and lock it against concurrent modification.
4. Review infrastructure changes with the same rigour as application code.
5. Prove it by rebuilding an environment from scratch periodically.

## Output contract
Write `infrastructure-code` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** infrastructure-as-code
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
- No manually created resources remain
- Rebuild from scratch demonstrated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
