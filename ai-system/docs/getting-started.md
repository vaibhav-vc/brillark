# Getting started

## 1. Verify the system

```bash
python3 ai-system/tests/test_system_integrity.py
```

25 tests. They check that every agent, skill, workflow, and schema reference resolves. If this fails,
fix it before running anything — an agent pointing at a skill that does not exist will fail silently
and confusingly later.

## 2. Scaffold a venture

```bash
bash ai-system/bootstrap/init.sh acme-corp
python3 ai-system/tests/measure_context_cost.py   # what a run will cost you
```

This creates `workspace/acme-corp/` with a directory per skill category, an empty memory store, and a
`venture.yaml` from the template. Nothing in `ai-system/` is venture-specific; all working output lives
in `workspace/`.

## 3. Write the intent brief

Fill in `workspace/acme-corp/venture.yaml`. Be concrete about the problem and honest about what you
do not know. The `director` will restate it back to you before spending anything — confirm or correct
that restatement, because everything downstream is built on it.

## 4. Run the first workflow

Start with `workflows/00-intake.yaml`, then `01-business-model-design.yaml`. Each step names the agent
that owns it, the skills it uses, and the condition that makes it done.

The order that actually works:

| Stage | Workflow | You get |
|---|---|---|
| Idea | `00-intake` | One owned, contextualised task graph |
| Business model | `01-business-model-design` | An evidence-tagged canvas, pricing, unit economics, Council verdict |
| Validation | `02-market-validation` | Customer evidence, and an honest report of what was disproven |
| MVP | `03-mvp-definition` -> `04-mvp-build` | A scope line that tests the riskiest belief, then the build |
| Launch | `05-mvp-launch` | Real users, instrumented, with rollback available |
| Learn | `06-feedback-and-iterate` | Features judged against their pre-set signals |
| Design | `14-design-delivery` | Flows, states, copy, accessibility, tested with users |
| Upgrade | `07-upgrade-and-scale` | A sequenced expansion behind its prerequisites |
| Improve | `15-self-improvement` | The system measurably better at its own job |
| Efficiency | `16-efficiency-review` | Lower cost per completed task, quality verified unchanged |

`08-council-review` runs whenever a plan is material. `09-memory-consolidation` runs at every stage gate.

## 5. Do not skip the Council

The most common way to waste a quarter is to skip the review because the plan feels obviously right.
`08-council-review` takes one pass and produces a written verdict with owners on every blocker. The
Director may overrule any blocker — in writing, with the reasoning recorded. That record is what makes
the override legitimate rather than a lapse.

## What "done" means at each level

- **Skill run** — the artifact exists, with a summary, evidence table, open questions, and one next action.
- **Task** — every criterion in the definition of done is checkable and met.
- **Workflow** — all exit criteria are satisfied.
- **Stage** — the Director has written a stage-gate decision naming the evidence that moved it.

## Wiring this into an actual agent runtime

The agent files use standard subagent frontmatter, so they can be dropped into a Claude Code
`.claude/agents/` directory or loaded by any orchestrator that reads YAML frontmatter plus markdown.
`agents/registry.yaml` and `skills/registry.yaml` exist so a runtime can enumerate the roster without
parsing 83 markdown files. See `integrations/README.md` for the external system contracts.
