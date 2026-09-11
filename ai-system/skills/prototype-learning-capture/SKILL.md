---
name: prototype-learning-capture
category: hardware
description: "Turn the build into evidence rather than anecdote."
output: "build-learnings.md"
used_by:
  - prototyping-fabrication-agent
---

# Prototype Learning Capture

`hardware` · produces `build-learnings.md` · used by `prototyping-fabrication-agent`

Turn the build into evidence rather than anecdote.

## Procedure
1. Record what the build was meant to answer and what it actually showed.
2. Separate findings caused by the prototype process from real design findings.
3. Quantify where possible rather than describing impressions.
4. Route each finding to the discipline that owns it.
5. Update the design and the next build's questions from the findings.

## Output contract
`build-learnings.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Process artefacts separated from real design findings
- Findings routed to the owning discipline
- The output states its confidence grade and names the evidence behind every load-bearing claim.
