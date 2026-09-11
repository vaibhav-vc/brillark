# laundro

Workspace for the venture `laundro`, scaffolded from ai-system/bootstrap.

- `venture.yaml` — the intent brief. Fill this in first.
- `memory/` — the four memory types plus entities and decisions.
- `council-verdicts/` — every verdict, kept permanently including dissent.
- `artifacts/` — registered skill outputs.
- `telemetry/` — token ledger and agent performance records; the improvement loop reads these.
- `improvement-proposals/` — proposed changes to the system, with their trials and authorisation.
- one directory per skill category for working output.

## Next steps

1. Fill in `venture.yaml`. Be honest about what you do not know.
2. Run `workflows/00-intake.yaml` — the director will restate your intent back to you.
3. Confirm or correct that restatement before anything else is spent.
4. Then `workflows/01-business-model-design.yaml`.
