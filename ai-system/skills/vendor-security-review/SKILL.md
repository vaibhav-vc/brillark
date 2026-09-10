---
name: vendor-security-review
category: engineering
description: "Assess a third party before trusting them with data or access."
output: "vendor-security-review.md"
used_by:
  - ciso-agent
---

# Vendor Security Review

**Category:** `engineering` · **Output artifact:** `vendor-security-review.md`

## What this skill does
Assess a third party before trusting them with data or access.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ciso-agent`.

## Procedure
1. Determine what data and access the vendor would receive.
2. Review their security posture, certifications, and breach history.
3. Check contractual security and breach notification terms.
4. Assess the blast radius of their compromise.
5. Define monitoring and the exit path if their posture degrades.

## Output contract
Write `vendor-security-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** vendor-security-review
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
- Blast radius of compromise assessed
- Breach notification terms verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
