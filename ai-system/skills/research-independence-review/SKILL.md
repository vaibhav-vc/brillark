---
name: research-independence-review
category: research
description: "Check the finding was not shaped by what someone wanted."
output: "independence-review.md"
used_by:
  - chief-research-officer-agent
  - research-head
---

# Research Independence Review

`research` · produces `independence-review.md` · used by `chief-research-officer-agent`, `research-head`

Check the finding was not shaped by what someone wanted.

## Procedure
1. Check whether the question was framed to produce a preferred answer.
2. Check whether disconfirming sources were sought with equal effort.
3. Check whether the conclusion overstates what the evidence supports.
4. Check whether unwelcome findings were softened between draft and final.
5. Report pressure on the research function rather than absorbing it.

## Output contract
`independence-review.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Disconfirming search effort verified
- Softening between draft and final detected
- The output states its confidence grade and names the evidence behind every load-bearing claim.
