---
name: remedy-design
category: council
description: "Propose a fix alongside every criticism."
output: "remedy-proposal.md"
used_by:
  - council-ethics-and-responsibility
---

# Remedy Design

`council` · produces `remedy-proposal.md` · used by `council-ethics-and-responsibility`

Propose a fix alongside every criticism.

## Procedure
1. State the finding and the specific harm it causes.
2. Propose at least two remedies at different cost levels.
3. Assess what each remedy costs in effort and in product value.
4. Recommend one and state the trade-off accepted.
5. Verify the remedy would actually eliminate the finding.

## Output contract
`remedy-proposal.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- At least two remedy options offered
- Remedy verified against the finding
- The output states its confidence grade and names the evidence behind every load-bearing claim.
