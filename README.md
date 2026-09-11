# brillark

## `ai-system/`

A multi-agent organisation for planning, building, and upgrading ventures: 138 agents across ten
domains, 629 skills, 19 workflows, 22 schemas, and 88 tests that keep them consistent.

Model-agnostic: agents declare a capability tier, never a vendor's model name. A reference loader,
a multi-format exporter, and an eval harness make it usable from any runtime.

Built to be cheap to run — a routed agent run loads about **3,155 tokens**, not the 278,000 the full
library would cost. About 88x cheaper, verified by a benchmark that runs in CI.

Start at **[`ai-system/README.md`](ai-system/README.md)**.

```bash
bash ai-system/tests/run_all.sh                    # everything: integrity, conformance, benchmark
python3 ai-system/tools/loader.py domains          # see the organisation from the outside
python3 ai-system/tools/export.py                  # render it for your runtime
bash ai-system/bootstrap/init.sh <venture-id>      # scaffold a venture workspace
```

| Tier | Count | |
|---|---|---|
| Director | 1 | Stage gates, arbitration, budget |
| Domain heads | 9 | Finance, business, engineering, design, hardware, research, orchestration, improvement, council |
| Executive officers | 21 | Including Chief Design, Chief Hardware, Chief Learning, Chief Research Officer |
| Council | 10 | Critics who attack every material plan before it is funded |
| Specialists | 97 | 50 planning · 15 hardware (3D + PCB) · 14 design · 12 improvement · 6 research |

Key reading: [org chart](ai-system/docs/org-chart.md) ·
[token efficiency](ai-system/docs/token-efficiency.md) ·
[self-improvement](ai-system/docs/self-improvement.md) ·
[design practice](ai-system/docs/design-practice.md) ·
[hardware practice](ai-system/docs/hardware-practice.md) ·
[research practice](ai-system/docs/research-practice.md) ·
[integration guide](ai-system/docs/integration-guide.md) ·
[memory model](ai-system/docs/memory-model.md)
