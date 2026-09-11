---
name: infrastructure-as-code
category: engineering
description: "Define infrastructure so it can be rebuilt exactly."
output: "infrastructure-code"
used_by:
  - infra-devops-agent
---

# Infrastructure As Code

`engineering` · produces `infrastructure-code` · used by `infra-devops-agent`

Define infrastructure so it can be rebuilt exactly.

## Procedure
1. Express every resource in code; nothing created by hand survives.
2. Keep environment differences in configuration, not in divergent code.
3. Store state securely and lock it against concurrent modification.
4. Review infrastructure changes with the same rigour as application code.
5. Prove it by rebuilding an environment from scratch periodically.

## Output contract
`infrastructure-code` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- No manually created resources remain
- Rebuild from scratch demonstrated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
