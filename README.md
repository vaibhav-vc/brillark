# brillark

## `ai-system/`

A multi-agent organisation for planning, building, and upgrading ventures: 83 agents across five
tiers, 363 skills, 14 workflows, 14 knowledge schemas, and a test suite that keeps them consistent.

Start at **[`ai-system/README.md`](ai-system/README.md)**.

```bash
python3 ai-system/tests/test_system_integrity.py   # verify the system is consistent
bash ai-system/bootstrap/init.sh <venture-id>      # scaffold a venture workspace
```

| | |
|---|---|
| Director | 1 — owns stage gates, arbitration, and budget |
| Domain heads | 5 — finance, business, engineering, orchestration, council |
| Executive officers | 17 — including legal, compliance, privacy, IP, and risk |
| Council | 10 critics — attack every material plan before it is funded |
| Specialists | 50 planning agents |
