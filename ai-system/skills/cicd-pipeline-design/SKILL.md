---
name: cicd-pipeline-design
category: engineering
description: "Build a pipeline that makes shipping safe and boring."
output: "pipeline.md"
used_by:
  - infra-devops-agent
---

# Cicd Pipeline Design

`engineering` · produces `pipeline.md` · used by `infra-devops-agent`

Build a pipeline that makes shipping safe and boring.

## Procedure
1. Define the stages and what each gate proves.
2. Make builds reproducible and artifacts immutable.
3. Run fast checks first so failures surface early.
4. Gate on tests, security scanning, and budget checks.
5. Keep total pipeline time short enough that people do not route around it.

## Output contract
`pipeline.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Artifacts immutable and reproducible
- Pipeline fast enough to not be bypassed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
