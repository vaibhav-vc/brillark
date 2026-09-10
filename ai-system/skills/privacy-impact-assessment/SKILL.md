---
name: privacy-impact-assessment
category: compliance
description: "Assess high-risk processing before it starts."
output: "dpia.md"
used_by:
  - data-protection-officer-agent
---

# Privacy Impact Assessment

**Category:** `compliance` · **Output artifact:** `dpia.md`

## What this skill does
Assess high-risk processing before it starts.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-protection-officer-agent`.

## Procedure
1. Describe the processing, its purpose, and its necessity.
2. Identify the personal data involved and the lawful basis.
3. Assess risks to individuals, not just to the company.
4. Define mitigations and the residual risk after them.
5. Record the decision and consult before proceeding where required.

## Output contract
Write `dpia.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** privacy-impact-assessment
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
- Risk assessed to individuals
- Residual risk stated after mitigation
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
