---
name: structured-logging
category: engineering
description: "Log so that questions can be answered later."
output: "logging-standard.md"
used_by:
  - backend-implementation-agent
---

# Structured Logging

**Category:** `engineering` · **Output artifact:** `logging-standard.md`

## What this skill does
Log so that questions can be answered later.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `backend-implementation-agent`.

## Procedure
1. Log events as structured records with consistent field names.
2. Include the correlation identifier on every record.
3. Log the decision and its inputs, not only the outcome.
4. Never log secrets or personal data; define what is redacted.
5. Set levels deliberately so production noise stays readable.

## Output contract
Write `logging-standard.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** structured-logging
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
- Correlation identifier on every record
- Redaction rules defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
