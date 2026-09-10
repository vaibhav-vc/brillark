# ai-system — a multi-agent organisation for building ventures

83 agents, 363 skills, 14 workflows, 14 schemas, and a test suite that keeps them consistent.

The system takes a founder's intent and runs it through the same path a competent company would:
design a business model, validate it against real customers, scope an MVP to the smallest thing that
tests the riskiest belief, build it, launch it, learn from it, and upgrade it — with every material
plan attacked by a standing Council of critics before money is spent on it.

## The organisation

```
                          human founder
                                |
                            director                 <- 1, single accountable owner
                                |
        +---------------+-------+-------+---------------+
        |               |               |               |
   finance-head   business-head   engineering-head  orchestration-head   council-director
      (12)            (14)             (14)              (10)                (10 critics)
                                                                          <- 50 specialists total

        executive officers (17): CEO, CFO, CMO, CTO, COO, CPO, CSO, CRO, CDO,
        CISO, CHRO, General Counsel, Chief Compliance, Chief Risk,
        Data Protection Officer, IP Counsel, Corporate Secretary
```

Full chart, decision rights, and the constraints that hold it together: **[`docs/org-chart.md`](docs/org-chart.md)**.

| Tier | Count | What it is for |
|---|---|---|
| Director | 1 | Owns stage gates, arbitration, and the budget. The only agent reporting to the human. |
| Domain heads | 5 | Finance, business, engineering, orchestration, council. Own their domain's output. |
| Executive officers | 17 | Company-wide functions, including legal, compliance, privacy, IP, and risk. |
| Council | 10 | Structured critics. Attack every material plan before it is funded. |
| Specialists | 50 | The planning agents that do the work. |

## Layout

| Directory | What is in it |
|---|---|
| `agents/` | 83 agent definitions plus `registry.yaml` and `AGENT_INDEX.md` |
| `skills/` | 363 skills, one directory each, plus `registry.yaml` and `SKILL_INDEX.md` |
| `prompts/` | Layered system prompts and the artifact templates that move between agents |
| `workflows/` | 14 executable workflow definitions, from intake to fundraise |
| `knowledge-schema/` | 14 JSON Schemas: memory, entities, decisions, verdicts, tasks, handoffs |
| `integrations/` | Contracts for the external systems the organisation reads and writes |
| `tests/` | Integrity tests that fail when the parts drift apart |
| `bootstrap/` | Start a new venture and check the system is wired correctly |
| `docs/` | Org chart, memory model, stage gates, council protocol, conventions, glossary |

## Start here

1. **[`docs/getting-started.md`](docs/getting-started.md)** — run your first venture through the system.
2. **[`docs/org-chart.md`](docs/org-chart.md)** — who reports to whom and who decides what.
3. **[`docs/memory-model.md`](docs/memory-model.md)** — how context and memory actually work.
4. **[`docs/stage-gates.md`](docs/stage-gates.md)** — the seven stages and what each requires to exit.

```bash
bash ai-system/bootstrap/init.sh acme-corp     # scaffold a venture workspace
python3 ai-system/tests/test_system_integrity.py   # verify the system is consistent
```

## The design decisions worth knowing

- **One owner per thing.** Tasks, artifacts, risks, and metrics each have exactly one accountable agent.
- **Evidence carries a grade.** Every claim is `measured`, `sourced`, `benchmarked`, `estimated`, or
  `guessed`. A guess may never be load-bearing at a stage gate.
- **The Council attacks but never decides.** It issues verdicts; the Director decides. Overruling a
  blocker is allowed and must be written down.
- **Memory is a system, not a folder.** Four memory types, provenance on every write, contradictions
  resolved by supersession, and stale context quarantined rather than silently trusted.
- **Legal advice stops at the boundary.** The legal agents spot issues and draft; anything needing a
  licensed attorney is escalated out of the system rather than answered inside it.
- **The whole thing is testable.** `tests/test_system_integrity.py` fails if an agent references a
  skill that does not exist, a reporting line dangles, or a workflow names a missing agent.
