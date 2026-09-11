"""Export the organisation into formats other runtimes can consume directly.

The markdown is the source of truth, but no runtime should have to parse 720 files to use it.
This produces a `dist/` bundle with the same organisation in several shapes, plus checksums so a
consumer can tell whether their copy is current.

    python3 ai-system/tools/export.py                      # everything, into ai-system/dist/
    python3 ai-system/tools/export.py --format json        # one format
    python3 ai-system/tools/export.py --out /tmp/bundle
    python3 ai-system/tools/export.py --check              # is dist/ current? (CI uses this)

Formats
  json       agents.json, skills.json — the whole organisation, charters inlined
  tools      tool-definitions.json — one JSON-Schema tool per agent, for any function-calling API
  claude     claude-agents/ — subagent markdown with frontmatter
  mcp        mcp-manifest.json — an MCP server description exposing agents as tools
  prompts    system-prefix.txt — the assembled cacheable prefix, ready to send
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import shutil
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTRACT_VERSION = "1.0.0"
FORMATS = ["json", "tools", "claude", "mcp", "prompts"]


def load():
    agents = yaml.safe_load((ROOT / "agents" / "registry.yaml").read_text())["agents"]
    skills = yaml.safe_load((ROOT / "skills" / "registry.yaml").read_text())["skills"]
    return agents, skills


def body_after_frontmatter(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---\n", 3)
        if end != -1:
            return text[end + 5:].lstrip()
    return text


def export_json(agents, skills, out: pathlib.Path):
    skill_by_name = {s["name"]: s for s in skills}
    payload = []
    for a in agents:
        entry = dict(a)
        entry["charter"] = body_after_frontmatter(ROOT / a["path"])
        entry["skill_detail"] = [
            {"name": n,
             "category": skill_by_name[n]["category"],
             "description": skill_by_name[n]["description"],
             "output": skill_by_name[n]["output"],
             "procedure": body_after_frontmatter(ROOT / skill_by_name[n]["path"])}
            for n in a["skills"] if n in skill_by_name]
        payload.append(entry)
    (out / "agents.json").write_text(json.dumps(payload, indent=2, sort_keys=True))

    sk = []
    for s in skills:
        entry = dict(s)
        entry["procedure"] = body_after_frontmatter(ROOT / s["path"])
        sk.append(entry)
    (out / "skills.json").write_text(json.dumps(sk, indent=2, sort_keys=True))
    return ["agents.json", "skills.json"]


def export_tools(agents, skills, out: pathlib.Path):
    """One tool definition per agent. Plain JSON Schema — usable by any function-calling API."""
    skill_by_name = {s["name"]: s for s in skills}
    tools = []
    for a in agents:
        toolkit = "; ".join(
            f"{n}: {skill_by_name[n]['description']}" for n in a["skills"] if n in skill_by_name)
        tools.append({
            "name": a["id"].replace("-", "_"),
            "description": (
                f"{a['capability']} "
                f"[{a['tier']} in the {a['domain']} domain, reports to {a['reports_to']}] "
                f"Skills — {toolkit}"),
            "input_schema": {
                "type": "object",
                "required": ["task", "definition_of_done"],
                "properties": {
                    "task": {"type": "string",
                             "description": "What this agent must produce, and the decision it supports."},
                    "definition_of_done": {
                        "type": "array", "items": {"type": "string"}, "minItems": 1,
                        "description": "Checkable completion conditions, agreed before work starts."},
                    "context_artifacts": {
                        "type": "array", "items": {"type": "string"},
                        "description": "Artifact paths, not contents. The agent fetches what it needs."},
                    "accepted_assumptions": {"type": "array", "items": {"type": "string"}},
                    "open_questions": {
                        "type": "array", "items": {"type": "string"},
                        "description": "Carried forward, never trimmed for tidiness."},
                },
                "additionalProperties": False,
            },
            "x_ai_system": {
                "task_class": a["task_class"],
                "context_budget_tokens": a["context_budget_tokens"],
                "return_budget_tokens": a["return_budget_tokens"],
                "escalates_to_task_class": a["escalates_to_model"],
                "returns": "knowledge-schema/agent-return.schema.json",
            },
        })
    (out / "tool-definitions.json").write_text(json.dumps(
        {"contract_version": CONTRACT_VERSION, "count": len(tools), "tools": tools},
        indent=2, sort_keys=True))
    return ["tool-definitions.json"]


def export_claude(agents, skills, out: pathlib.Path):
    """Claude Code subagent files: frontmatter plus the charter, with skills inlined so each file
    is self-contained and can be dropped into .claude/agents/."""
    skill_by_name = {s["name"]: s for s in skills}
    target = out / "claude-agents"
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for a in agents:
        inlined = "\n\n".join(
            f"### Skill: {n}\n\n{body_after_frontmatter(ROOT / skill_by_name[n]['path'])}"
            for n in a["skills"] if n in skill_by_name)
        front = {
            "name": a["id"],
            "description": a["capability"],
            "model": a["model"],
        }
        text = ("---\n" + yaml.safe_dump(front, sort_keys=False, allow_unicode=True) + "---\n\n"
                + body_after_frontmatter(ROOT / a["path"])
                + "\n\n---\n\n## Skill procedures\n\n" + inlined + "\n")
        (target / f"{a['id']}.md").write_text(text)
    return [f"claude-agents/ ({len(agents)} files)"]


def export_mcp(agents, skills, out: pathlib.Path):
    tools_path = out / "tool-definitions.json"
    tools = json.loads(tools_path.read_text())["tools"] if tools_path.exists() else []
    manifest = {
        "name": "ai-system",
        "version": CONTRACT_VERSION,
        "description": (
            f"A {len(agents)}-agent organisation for planning, designing, building, and improving "
            f"ventures. Each tool is one accountable agent with a charter, declared skills, a "
            f"context budget, and a capped return contract."),
        "capabilities": {"tools": {}},
        "tools": [{"name": t["name"], "description": t["description"],
                   "inputSchema": t["input_schema"]} for t in tools],
        "x_contract": {
            "loading": "runtime/loader-spec.md",
            "budgets": "runtime/context-budget.yaml",
            "model_profiles": "runtime/model-profiles.yaml",
            "return_schema": "knowledge-schema/agent-return.schema.json",
        },
    }
    (out / "mcp-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))
    return ["mcp-manifest.json"]


def export_prompts(agents, skills, out: pathlib.Path):
    """The cacheable prefix, assembled. Send this once per session."""
    pieces = []
    for rel in ("prompts/system/00-base-agent.md",
                "prompts/system/05-token-discipline.md",
                "skills/OUTPUT_CONTRACT.md"):
        pieces.append((ROOT / rel).read_text())
    (out / "system-prefix.txt").write_text("\n\n".join(pieces))
    return ["system-prefix.txt"]


EXPORTERS = {"json": export_json, "tools": export_tools, "claude": export_claude,
             "mcp": export_mcp, "prompts": export_prompts}


def checksum(out: pathlib.Path) -> dict:
    sums = {}
    for path in sorted(out.rglob("*")):
        if path.is_file() and path.name != "manifest.json":
            sums[str(path.relative_to(out))] = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    return sums


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--format", choices=FORMATS, action="append",
                    help="repeatable; default is all formats")
    ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if the bundle is not current (for CI)")
    args = ap.parse_args()

    formats = args.format or FORMATS
    # 'mcp' reads the tool definitions, so 'tools' must run first.
    formats = [f for f in FORMATS if f in formats]
    out = pathlib.Path(args.out)

    if args.check:
        manifest_path = out / "manifest.json"
        if not manifest_path.exists():
            print("dist/ has never been generated. Run: python3 ai-system/tools/export.py",
                  file=sys.stderr)
            return 1
        previous = json.loads(manifest_path.read_text())
        agents, skills = load()
        for fn in (EXPORTERS[f] for f in formats):
            fn(agents, skills, out)
        current = checksum(out)
        if current != previous.get("checksums"):
            changed = sorted(set(current) ^ set(previous.get("checksums", {}))) or [
                k for k in current if current[k] != previous["checksums"].get(k)]
            print("dist/ is stale — regenerate it with: python3 ai-system/tools/export.py",
                  file=sys.stderr)
            print(f"  differing: {changed[:10]}", file=sys.stderr)
            return 1
        print("dist/ is current")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    agents, skills = load()
    written = []
    for name in formats:
        written += EXPORTERS[name](agents, skills, out)

    manifest = {
        "contract_version": CONTRACT_VERSION,
        "agents": len(agents),
        "skills": len(skills),
        "formats": formats,
        "files": written,
        "source_of_truth": "the markdown in ai-system/ — this bundle is generated, never edited",
        "checksums": checksum(out),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True))

    print(f"exported {len(agents)} agents and {len(skills)} skills to {out}")
    for item in written:
        print(f"  {item}")
    print(f"  manifest.json (contract {CONTRACT_VERSION})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
