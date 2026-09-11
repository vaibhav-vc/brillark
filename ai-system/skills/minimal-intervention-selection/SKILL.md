---
name: minimal-intervention-selection
category: improvement
description: "Choose the smallest change that closes the gap."
output: "intervention-proposal.md"
used_by:
  - capability-gap-scout
---

# Minimal Intervention Selection

`improvement` · produces `intervention-proposal.md` · used by `capability-gap-scout`

Choose the smallest change that closes the gap.

## Procedure
1. Check whether an existing skill can be revised to cover it.
2. If not, check whether one new skill would suffice.
3. Only then consider a new agent, and justify the accountability it adds.
4. Estimate the ongoing cost of each option, not just the build cost.
5. Recommend the smallest option that actually closes the gap.

## Output contract
`intervention-proposal.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Revision considered before addition
- Ongoing cost estimated, not just build cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.
