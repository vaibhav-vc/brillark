# Prompts

Two kinds of file live here.

## `system/`
Layered system prompts. An agent's effective prompt is `00-base-agent.md` plus the one file for its
tier plus its own `agents/**/<id>.md` definition. The base file holds the rules that apply to every
agent, so a change to organisational behaviour is made in one place rather than 83.

| File | Applies to |
|---|---|
| `00-base-agent.md` | every agent, always |
| `01-director.md` | `director` |
| `02-domain-head.md` | the five heads |
| `03-council-critic.md` | the ten Council agents |
| `04-specialist.md` | the 50 specialists |

Executive officers use the base prompt plus their own definition; their charters are function-specific
enough that a shared officer prompt would only repeat the base.

## `templates/`
The fixed shapes of the artifacts that move between agents. If an artifact has a template here, use it:
consistent structure is what lets the orchestration layer validate a handoff without reading prose.
