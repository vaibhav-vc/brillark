---
name: security-test-design
category: engineering
description: "Test that the security controls actually work."
output: "security-tests.md"
used_by:
  - security-engineer
---

# Security Test Design

**Category:** `engineering` · **Output artifact:** `security-tests.md`

## What this skill does
Test that the security controls actually work.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `security-engineer`.

## Procedure
1. Derive test cases from the threat model, not from a generic checklist.
2. Test authorisation on every protected path, including the negative cases.
3. Test input handling with hostile payloads.
4. Test that rate limits and lockouts function under real conditions.
5. Automate what can be automated and schedule the rest.

## Output contract
Write `security-tests.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** security-test-design
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
- Cases derived from the threat model
- Negative authorisation cases tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
