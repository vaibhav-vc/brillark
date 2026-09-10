"""Integrity tests for the ai-system agent organisation.

These check the things that silently rot: an agent referencing a skill that was renamed,
a reporting line pointing at a deleted agent, a workflow calling an agent that never existed,
a schema that no longer parses. Run with `python3 -m pytest ai-system/tests -q`
or directly with `python3 ai-system/tests/test_system_integrity.py`.

Only the standard library plus PyYAML is required.
"""
from __future__ import annotations

import json
import pathlib
import re
import unittest

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Counts the organisation is contractually required to have. If you deliberately change the
# shape of the org, change these numbers in the same commit and say why in the message.
REQUIRED = {
    "planning_agents": 50,   # the specialist tier that plans and builds the business
    "council_agents": 10,    # the critics
    "heads": 5,              # finance, business, engineering, orchestration, council
    "directors": 1,          # exactly one top-level owner
    "min_skills": 100,       # the floor; the library is far larger
}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_frontmatter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    assert match, f"{path.relative_to(ROOT)} has no YAML frontmatter"
    return yaml.safe_load(match.group(1))


def load_registry() -> list[dict]:
    return yaml.safe_load((ROOT / "agents" / "registry.yaml").read_text())["agents"]


def load_skill_registry() -> list[dict]:
    return yaml.safe_load((ROOT / "skills" / "registry.yaml").read_text())["skills"]


class TestAgents(unittest.TestCase):
    def setUp(self):
        self.agents = load_registry()
        self.ids = {a["id"] for a in self.agents}

    def test_registry_matches_files_on_disk(self):
        on_disk = {p.stem for p in (ROOT / "agents").rglob("*.md")
                   if p.name not in ("AGENT_INDEX.md", "README.md")}
        self.assertEqual(self.ids, on_disk,
                         "agents/registry.yaml and the files in agents/ have drifted apart")

    def test_ids_are_unique(self):
        self.assertEqual(len(self.ids), len(self.agents), "duplicate agent id in registry")

    def test_required_counts(self):
        tiers = {}
        for a in self.agents:
            tiers[a["tier"]] = tiers.get(a["tier"], 0) + 1
        self.assertEqual(tiers.get("specialist"), REQUIRED["planning_agents"])
        self.assertEqual(tiers.get("council"), REQUIRED["council_agents"])
        self.assertEqual(tiers.get("head"), REQUIRED["heads"])
        self.assertEqual(tiers.get("director"), REQUIRED["directors"])

    def test_reporting_lines_resolve(self):
        for a in self.agents:
            if a["tier"] == "director":
                self.assertEqual(a["reports_to"], "human-founder",
                                 "the Director reports to the human, nobody else")
            else:
                self.assertIn(a["reports_to"], self.ids,
                              f"{a['id']} reports to {a['reports_to']}, which does not exist")

    def test_no_reporting_cycles(self):
        for a in self.agents:
            seen, node = {a["id"]}, a
            while node["tier"] != "director":
                parent = node["reports_to"]
                self.assertNotIn(parent, seen, f"reporting cycle involving {a['id']}")
                seen.add(parent)
                node = next(x for x in self.agents if x["id"] == parent)

    def test_every_agent_reaches_the_director(self):
        for a in self.agents:
            hops, node = 0, a
            while node["tier"] != "director" and hops < 10:
                node = next(x for x in self.agents if x["id"] == node["reports_to"])
                hops += 1
            self.assertEqual(node["tier"], "director",
                             f"{a['id']} does not report up to the director")

    def test_frontmatter_matches_registry(self):
        for a in self.agents:
            fm = parse_frontmatter(ROOT / a["path"])
            self.assertEqual(fm["name"], a["id"])
            self.assertEqual(fm["reports_to"], a["reports_to"])
            self.assertEqual(fm["tier"], a["tier"])
            self.assertEqual(sorted(fm["skills"]), sorted(a["skills"]))

    def test_agents_have_required_sections(self):
        required = ["## Mission", "## Charter", "## Operating procedure",
                    "## Memory & context contract", "## Escalation & handoffs",
                    "## Guardrails", "## Definition of done"]
        for a in self.agents:
            body = (ROOT / a["path"]).read_text()
            for section in required:
                self.assertIn(section, body, f"{a['id']} is missing {section}")

    def test_agents_declare_memory_scopes(self):
        for a in self.agents:
            self.assertTrue(a["memory_scopes"], f"{a['id']} declares no memory scopes")

    def test_council_reports_to_council_director(self):
        for a in self.agents:
            if a["tier"] == "council" and a["id"] != "council-director":
                self.assertEqual(a["reports_to"], "council-director")

    def test_profiles_satisfy_the_schema(self):
        schema = json.loads((ROOT / "knowledge-schema" / "agent-profile.schema.json").read_text())
        for a in self.agents:
            for field in schema["required"]:
                self.assertIn(field, a, f"{a['id']} is missing required field {field}")
            self.assertIn(a["tier"], schema["properties"]["tier"]["enum"])
            self.assertIn(a["domain"], schema["properties"]["domain"]["enum"])


class TestSkills(unittest.TestCase):
    def setUp(self):
        self.skills = load_skill_registry()
        self.names = {s["name"] for s in self.skills}
        self.agents = load_registry()

    def test_minimum_library_size(self):
        self.assertGreaterEqual(len(self.skills), REQUIRED["min_skills"])

    def test_registry_matches_files_on_disk(self):
        on_disk = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(self.names, on_disk,
                         "skills/registry.yaml and the directories in skills/ have drifted apart")

    def test_every_agent_skill_reference_resolves(self):
        for a in self.agents:
            for skill in a["skills"]:
                self.assertIn(skill, self.names,
                              f"{a['id']} references skill '{skill}', which does not exist")

    def test_skill_files_have_a_procedure_and_a_quality_bar(self):
        for s in self.skills:
            body = (ROOT / s["path"]).read_text()
            self.assertIn("## Procedure", body, f"{s['name']} has no procedure")
            self.assertIn("## Quality bar", body, f"{s['name']} has no quality bar")
            self.assertIn("## Output contract", body, f"{s['name']} has no output contract")
            steps = re.findall(r"^\d+\. ", body, re.M)
            self.assertGreaterEqual(len(steps), 5, f"{s['name']} has fewer than five steps")

    def test_frontmatter_matches_registry(self):
        for s in self.skills:
            fm = parse_frontmatter(ROOT / s["path"])
            self.assertEqual(fm["name"], s["name"])
            self.assertEqual(fm["category"], s["category"])

    def test_used_by_is_consistent_with_agent_definitions(self):
        actual = {}
        for a in self.agents:
            for skill in a["skills"]:
                actual.setdefault(skill, set()).add(a["id"])
        for s in self.skills:
            self.assertEqual(set(s["used_by"]), actual.get(s["name"], set()),
                             f"used_by for {s['name']} does not match the agent definitions")


class TestWorkflows(unittest.TestCase):
    def setUp(self):
        self.agent_ids = {a["id"] for a in load_registry()}
        self.skill_names = {s["name"] for s in load_skill_registry()}
        self.workflows = {p.name: yaml.safe_load(p.read_text())
                          for p in (ROOT / "workflows").glob("*.yaml")}

    def test_workflows_exist(self):
        self.assertGreaterEqual(len(self.workflows), 10)

    def test_every_step_names_a_real_agent_and_real_skills(self):
        for name, wf in self.workflows.items():
            for step in wf["steps"]:
                self.assertIn(step["agent"], self.agent_ids,
                              f"{name} step '{step['id']}' names unknown agent {step['agent']}")
                for skill in step["skills"]:
                    self.assertIn(skill, self.skill_names,
                                  f"{name} step '{step['id']}' names unknown skill {skill}")

    def test_every_step_has_a_completion_condition(self):
        for name, wf in self.workflows.items():
            for step in wf["steps"]:
                self.assertTrue(step.get("done_when"), f"{name}:{step['id']} has no done_when")
                self.assertTrue(step.get("produces"), f"{name}:{step['id']} produces nothing")

    def test_every_workflow_has_an_owner_and_exit_criteria(self):
        for name, wf in self.workflows.items():
            self.assertIn(wf["owner"], self.agent_ids, f"{name} has an unknown owner")
            self.assertTrue(wf.get("exit_criteria"), f"{name} has no exit criteria")

    def test_material_workflows_include_a_council_review(self):
        """Stage-advancing workflows must route through the Council somewhere."""
        must_review = ["01-business-model-design.yaml", "03-mvp-definition.yaml",
                       "07-upgrade-and-scale.yaml", "12-quarterly-planning.yaml"]
        for name in must_review:
            wf = self.workflows[name]
            agents = {s["agent"] for s in wf["steps"]}
            self.assertTrue(any(a.startswith("council") for a in agents),
                            f"{name} advances a stage without a Council step")


class TestSchemas(unittest.TestCase):
    def test_all_schemas_parse_and_are_self_describing(self):
        files = list((ROOT / "knowledge-schema").glob("*.schema.json"))
        self.assertGreaterEqual(len(files), 10)
        for path in files:
            schema = json.loads(path.read_text())
            self.assertIn("$schema", schema, f"{path.name} declares no $schema")
            self.assertIn("title", schema, f"{path.name} has no title")
            self.assertIn("description", schema, f"{path.name} has no description")
            self.assertEqual(schema["type"], "object")
            for field in schema.get("required", []):
                self.assertIn(field, schema["properties"],
                              f"{path.name} requires '{field}' but never defines it")

    def test_memory_records_require_provenance(self):
        schema = json.loads((ROOT / "knowledge-schema" / "memory-record.schema.json").read_text())
        self.assertIn("provenance", schema["required"],
                      "a memory without provenance cannot be trusted later")

    def test_council_findings_require_a_failure_scenario(self):
        schema = json.loads((ROOT / "knowledge-schema" / "council-verdict.schema.json").read_text())
        finding = schema["properties"]["findings"]["items"]
        self.assertIn("failure_scenario", finding["required"],
                      "a finding without a concrete failure scenario is an adjective, not a finding")


if __name__ == "__main__":
    unittest.main(verbosity=2)
