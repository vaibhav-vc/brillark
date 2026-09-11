# Agents

113 agents in five tiers. `registry.yaml` is the machine-readable roster; `AGENT_INDEX.md` is the
browsable one. Both are generated — edit the agent files and regenerate, or edit both together.

## Anatomy of an agent definition

Every file has YAML frontmatter (`name`, `tier`, `domain`, `reports_to`, `model`, `skills`,
`memory_scopes`) followed by fixed sections:

| Section | Why it exists |
|---|---|
| Mission | One paragraph. If it needs two, the agent owns too much. |
| Charter | What this agent owns — and by omission, what it does not. |
| Inputs / Outputs | The handoff contract in both directions. |
| Operating procedure | The numbered sequence the agent actually follows. |
| Skills | Named skills in `skills/`. Every reference is test-verified. |
| Memory & context contract | Which scopes it reads, and what it must write back. |
| Return contract | What it hands back to its parent, capped — never its working context. |
| Escalation & handoffs | The exact conditions for going up, and who receives the work. |
| Success measures | How you know this agent is working. |
| Guardrails | The four rules no agent may break. |
| Definition of done | What finished looks like for this agent. |

## Adding an agent

1. Write the definition under the right tier directory.
2. Add it to `registry.yaml` with its skills and memory scopes.
3. Make sure every skill it names exists in `skills/`.
4. Run the tests. They will tell you what you forgot.

Every agent also declares its **model tier**, **task class**, and **context and return budgets**.
These are not decoration: `runtime/` enforces them and the tests check them. A judgement-class agent
may not be demoted to a cheap tier, and an agent may never return more than it may receive.

Note that `tests/test_system_integrity.py` pins the org shape (50 planning, 14 design, 12 improvement
specialists, 10 council, 7 heads, 1 director). Changing it means changing those numbers deliberately,
in the same commit, with the reason in the message — and an org-shape change is not something the
improvement domain may do on its own.
