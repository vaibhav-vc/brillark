---
name: processor-due-diligence
category: compliance
description: "Check a third party before sending them personal data."
output: "processor-assessment.md"
used_by:
  - data-protection-officer-agent
---

# Processor Due Diligence

**Category:** `compliance` · **Output artifact:** `processor-assessment.md`

## What this skill does
Check a third party before sending them personal data.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-protection-officer-agent`.

## Procedure
1. Establish what data they receive and for what purpose.
2. Verify their security posture and sub-processor chain.
3. Ensure a data processing agreement is in place with adequate terms.
4. Verify the transfer mechanism for any cross-border flow.
5. Record the assessment and set a review date.

## Output contract
Write `processor-assessment.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** processor-due-diligence
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
- Sub-processor chain verified
- Transfer mechanism recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
