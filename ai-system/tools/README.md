# Tools

Three executables. Together they turn the definitions into something a runtime can use, consume,
and verify.

| Tool | What it does |
|---|---|
| `loader.py` | The executable contract: resolves model tiers, assembles context in cache order, enforces budgets, validates returns |
| `export.py` | Renders the organisation into JSON, tool definitions, Claude subagents, an MCP manifest, or a bare system prefix |
| `eval.py` | Runs the evaluation cases against any model you supply a callable for |

All three depend only on the standard library plus PyYAML. None imports a provider SDK — that is
deliberate: a system coupled to one vendor's client measures and serves that vendor.

```bash
python3 ai-system/tools/loader.py assemble --agent director --task "..."
python3 ai-system/tools/export.py --format tools
python3 ai-system/tools/eval.py --dry-run
```

`loader.py` is a reference implementation. If you port it, port `tests/test_conformance.py` too —
those tests are the definition of correct behaviour, not a description of this particular file.

See `docs/integration-guide.md`.
