# Agents

83 agents in five tiers. `registry.yaml` is the machine-readable roster; `AGENT_INDEX.md` is the
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
| Escalation & handoffs | The exact conditions for going up, and who receives the work. |
| Success measures | How you know this agent is working. |
| Guardrails | The four rules no agent may break. |
| Definition of done | What finished looks like for this agent. |

## Adding an agent

1. Write the definition under the right tier directory.
2. Add it to `registry.yaml` with its skills and memory scopes.
3. Make sure every skill it names exists in `skills/`.
4. Run the tests. They will tell you what you forgot.

Note that `tests/test_system_integrity.py` pins the tier counts (50 specialists, 10 council, 5 heads,
1 director). Changing the shape of the organisation means changing those numbers deliberately, in the
same commit, with the reason in the message.
