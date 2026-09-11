# ai-system — a multi-agent organisation for building ventures

130 agents, 590 skills, 18 workflows, 21 schemas, and a test suite that keeps them consistent.

The system takes a founder's intent and runs it through the path a competent company would: design a
business model, validate it against real customers, design the experience, scope an MVP to the
smallest thing that tests the riskiest belief, build it, launch it, learn from it, upgrade it — with
every material plan attacked by a standing Council before money is spent on it, and a self-improvement
loop that makes the next cycle better than the last.

**It is built to be cheap to run.** A routed agent run loads about **3,155 tokens**, not the 278,000
the full library would cost — about 88x cheaper. The organisation has grown from 83 agents to 130 and
the cost of a run has fallen by a third, because cost is driven by what gets loaded, not by what
exists. See [`docs/token-efficiency.md`](docs/token-efficiency.md), and run the benchmark yourself.

## The organisation

```
                                human founder
                                      |
                                  director                  <- 1, single accountable owner
                                      |
  +--------+--------+--------+--------+--------+--------+--------+--------+
  |        |        |        |        |        |        |        |        |
finance business  eng    design  hardware  orch   improvement  council
 (13)    (15)     (15)    (15)     (16)    (11)      (13)        (11)

  executive officers (20): CEO CFO CMO CTO COO CPO CSO CRO CDO CISO CHRO,
  Chief Design Officer, Chief Hardware Officer, Chief Learning Officer,
  General Counsel, Chief Compliance, Chief Risk, DPO, IP Counsel, Corporate Secretary
```

Full chart and decision rights: **[`docs/org-chart.md`](docs/org-chart.md)**.

| Tier | Count | For |
|---|---|---|
| Director | 1 | Stage gates, arbitration, budget. The only agent reporting to the human. |
| Domain heads | 8 | Finance, business, engineering, design, hardware, orchestration, improvement, council. |
| Executive officers | 20 | Company-wide functions, including design, hardware, learning, legal, privacy, IP, risk. |
| Council | 10 | Structured critics. Attack every material plan before it is funded. |
| Specialists | 91 | 50 planning · 15 hardware · 14 design · 12 improvement. |

## What makes it work

**Progressive disclosure.** Three tiers: discovery (a domain index, then one domain's agent cards —
about 770 tokens), activation (the one charter and the skills it declares), execution (context
fetched just-in-time). Shared boilerplate — the output contract, the guardrails, the category
anti-patterns — lives once in the cacheable prefix instead of being repeated 590 times.

**Context isolation.** Every agent runs in its own context and returns at most its
`return_budget_tokens` — the decision, the artifact paths, a confidence grade. Never its working
context.

**Model tiering.** 3 agents on `haiku` for mechanical work, 77 on
`sonnet` for analysis, 50 on `opus` for judgement. Every assignment needs quality
evidence; judgement work is never demoted to save money.

**Structural rules.** A memory record cannot exist without provenance. A decision cannot omit its
accepted costs. A Council finding cannot be an adjective. A design spec cannot omit its error state.
These are enforced by schema, not by convention.

**It improves itself, within limits.** The improvement domain measures, diagnoses, trials against
held-out cases, sweeps for regressions, adopts one change at a time, and verifies the next cycle. It
may edit prompts and skill steps automatically. It may **never** change guardrails, schemas, the org
shape, or its own evaluation criteria — those need the human founder. See
[`docs/self-improvement.md`](docs/self-improvement.md).

## Layout

| Directory | Contents |
|---|---|
| `agents/` | 130 charters, `registry.yaml`, and the tier-1 `index/` used for routing |
| `skills/` | 590 skills, one directory each, plus the sharded tier-1 `index/` |
| `runtime/` | Context budgets, model routing, and the loader specification |
| `prompts/` | Layered system prompts and the artifact templates that move between agents |
| `workflows/` | 18 workflow definitions, from intake to hardware development |
| `knowledge-schema/` | 20 JSON Schemas: memory, decisions, verdicts, returns, proposals, design specs |
| `integrations/` | Contracts for the external systems the organisation reads and writes |
| `tests/` | Integrity tests, plus the context-cost measurement |
| `bootstrap/` | Scaffold a venture and verify the wiring |
| `docs/` | Org chart, memory model, token efficiency, self-improvement, design practice |

## Start here

```bash
python3 ai-system/tests/test_system_integrity.py    # 46 tests: does everything still line up?
python3 ai-system/tests/benchmark.py                # regression gate against a committed baseline
python3 ai-system/tests/benchmark.py --repeat 25    # confirm the measurement is deterministic
python3 ai-system/tests/measure_context_cost.py     # what does a run actually cost?
bash ai-system/bootstrap/init.sh acme-corp          # scaffold a venture workspace
```

All three run in CI on every push — see `.github/workflows/ai-system.yml`.

1. **[`docs/getting-started.md`](docs/getting-started.md)** — run your first venture through it.
2. **[`docs/org-chart.md`](docs/org-chart.md)** — who reports to whom, who decides what.
3. **[`docs/token-efficiency.md`](docs/token-efficiency.md)** — why it is cheap, and how to keep it cheap.
4. **[`docs/memory-model.md`](docs/memory-model.md)** — how context and memory actually work.
5. **[`docs/self-improvement.md`](docs/self-improvement.md)** — the loop, and its boundary.
6. **[`docs/hardware-practice.md`](docs/hardware-practice.md)** — 3D, PCB, and why tooling is different.
7. **[`docs/design-practice.md`](docs/design-practice.md)** — the design domain's rules.

## Deliberate constraints

- **One owner** per task, artifact, risk, and metric. Two owners means none.
- **Evidence carries a grade** — `measured`, `sourced`, `benchmarked`, `estimated`, `guessed`. A
  guess may never be load-bearing at a stage gate.
- **The Council attacks but never decides.** The Director decides, and overruling a blocker must be
  written down.
- **Accessibility is a build requirement.** A surface that fails its conformance target is a defect.
- **Legal advice stops at the boundary.** Anything needing a licensed attorney is escalated out of
  the system, never answered inside it.
- **Efficiency never buys quality.** No saving ships without a quality check on the golden cases.
- **Never cut a tool on an unfrozen design.** The most expensive mistake in hardware, always made
  under schedule pressure.
