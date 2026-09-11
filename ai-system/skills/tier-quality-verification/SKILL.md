---
name: tier-quality-verification
category: efficiency
description: "Prove a demotion did not cost quality."
output: "tier-verification.md"
used_by:
  - model-router-tuner
---

# Tier Quality Verification

`efficiency` · produces `tier-verification.md` · used by `model-router-tuner`

Prove a demotion did not cost quality.

## Procedure
1. Run the full golden case set at both tiers.
2. Compare per case, not in aggregate.
3. Check the hardest cases specifically; averages hide their failure.
4. Check escalation frequency stayed within the expected range.
5. Revert the demotion if either check fails.

## Output contract
`tier-verification.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Hardest cases checked specifically
- Demotion reverted on any failed check
- The output states its confidence grade and names the evidence behind every load-bearing claim.
