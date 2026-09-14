"""A JSON Schema validator covering the subset the knowledge schemas actually use.

The schemas were written as draft 2020-12 and nothing validated against them, because the system
holds itself to the standard library plus PyYAML and `jsonschema` is neither. So the schemas said
things like "Required for blockers" in a `description` -- prose no machine read -- and an artifact
that ignored them passed every check in the repository.

This is deliberately small. It supports what the schemas use and refuses what it does not
understand, so an unsupported keyword fails loudly instead of silently passing.
"""
from __future__ import annotations

import json
import pathlib
import re

SUPPORTED = {
    "$schema", "$id", "title", "description", "type", "required", "properties", "items",
    "enum", "const", "pattern", "minLength", "maxLength", "minItems", "maxItems", "minimum",
    "maximum", "additionalProperties", "allOf", "anyOf", "oneOf", "not", "if", "then", "else",
    "contains", "format", "default", "examples", "uniqueItems", "patternProperties",
}

TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool,
    "number": (int, float), "integer": int, "null": type(None),
}


def _type_ok(value, expected: str) -> bool:
    if expected == "integer" and isinstance(value, bool):
        return False
    if expected == "number" and isinstance(value, bool):
        return False
    return isinstance(value, TYPES[expected])


def validate(instance, schema: dict, path: str = "") -> list[str]:
    """Return a list of human-readable problems. Empty means valid."""
    errors: list[str] = []
    unknown = set(schema) - SUPPORTED
    if unknown:
        return [f"{path or '<root>'}: schema uses keywords this validator does not support: "
                f"{sorted(unknown)} — extend validate.py rather than trusting the result"]

    if "type" in schema:
        expected = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(instance, t) for t in expected):
            return [f"{path or '<root>'}: expected {'/'.join(expected)}, got "
                    f"{type(instance).__name__}"]

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} is not one of {schema['enum']}")
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: must be {schema['const']!r}")

    if isinstance(instance, str):
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match {schema['pattern']}")
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: needs at least {schema['minLength']} characters, has "
                          f"{len(instance)}" + (f" — {schema['description']}"
                                                if "description" in schema else ""))
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: longer than {schema['maxLength']} characters")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} is below {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: {instance} is above {schema['maximum']}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: needs at least {schema['minItems']} item(s), has {len(instance)}")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: more than {schema['maxItems']} items")
        if "uniqueItems" in schema and schema["uniqueItems"]:
            seen = [json.dumps(i, sort_keys=True) for i in instance]
            if len(set(seen)) != len(seen):
                errors.append(f"{path}: items must be unique")
        if "items" in schema:
            for i, item in enumerate(instance):
                errors += validate(item, schema["items"], f"{path}[{i}]")
        if "contains" in schema and not any(
                not validate(i, schema["contains"], path) for i in instance):
            errors.append(f"{path}: no item satisfies 'contains'")

    if isinstance(instance, dict):
        for field in schema.get("required", []):
            if field not in instance:
                errors.append(f"{path or '<root>'}: missing required field '{field}'")
        props = schema.get("properties", {})
        for key, value in instance.items():
            sub = f"{path}.{key}" if path else key
            if key in props:
                errors += validate(value, props[key], sub)
            elif schema.get("additionalProperties") is False:
                errors.append(f"{sub}: not allowed (additionalProperties is false)")
            elif isinstance(schema.get("additionalProperties"), dict):
                errors += validate(value, schema["additionalProperties"], sub)

    for sub in schema.get("allOf", []):
        errors += validate(instance, sub, path)
    if "anyOf" in schema and not any(not validate(instance, s, path) for s in schema["anyOf"]):
        errors.append(f"{path or '<root>'}: matches none of the anyOf alternatives")
    if "oneOf" in schema:
        matched = sum(1 for s in schema["oneOf"] if not validate(instance, s, path))
        if matched != 1:
            errors.append(f"{path or '<root>'}: must match exactly one oneOf branch, matched {matched}")
    if "not" in schema and not validate(instance, schema["not"], path):
        errors.append(f"{path or '<root>'}: matches a forbidden shape"
                      + (f" — {schema['description']}" if "description" in schema else ""))
    if "if" in schema:
        branch = "then" if not validate(instance, schema["if"], path) else "else"
        if branch in schema:
            errors += validate(instance, schema[branch], path)
    return errors


def load(root: pathlib.Path, name: str) -> dict:
    return json.loads((root / "knowledge-schema" / f"{name}.schema.json").read_text())


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Validate a JSON document against a knowledge schema.")
    ap.add_argument("--schema", required=True, help="schema name, e.g. council-verdict")
    ap.add_argument("--file", required=True, help="JSON file to validate")
    args = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parent.parent
    problems = validate(json.loads(pathlib.Path(args.file).read_text()), load(root, args.schema))
    for p in problems:
        print(f"  - {p}")
    print("valid" if not problems else f"{len(problems)} problem(s)")
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
