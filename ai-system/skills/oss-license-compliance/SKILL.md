---
name: oss-license-compliance
category: legal
description: "Make sure dependency licences are compatible with the business model."
output: "license-report.md"
used_by:
  - ip-counsel-agent
---

# Oss License Compliance

**Category:** `legal` · **Output artifact:** `license-report.md`

## What this skill does
Make sure dependency licences are compatible with the business model.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ip-counsel-agent`.

## Procedure
1. Generate the full dependency tree, including transitive dependencies.
2. Identify the licence of each and its obligations.
3. Flag copyleft licences in anything distributed to customers.
4. Verify attribution and notice requirements are met.
5. Establish a gate so new dependencies are checked before merge.

## Output contract
Write `license-report.md` into `workspace/<venture-id>/legal/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** oss-license-compliance
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
- Transitive dependencies included
- Merge gate established for new dependencies
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `legal` category
- Answering a question that needs a licensed attorney with a confident internal opinion.
- Reviewing the clauses that are easy to read and skipping the liability terms.
- Clearing a name after launch instead of before.
