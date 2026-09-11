#!/usr/bin/env bash
# Scaffold a venture workspace. Nothing in ai-system/ is venture-specific;
# all working output lives under workspace/<venture-id>/.
set -euo pipefail

VENTURE="${1:-}"
if [[ -z "$VENTURE" ]]; then
  echo "usage: bash ai-system/bootstrap/init.sh <venture-id>" >&2
  echo "example: bash ai-system/bootstrap/init.sh acme-corp" >&2
  exit 1
fi
if [[ ! "$VENTURE" =~ ^[a-z0-9-]+$ ]]; then
  echo "error: venture id must be lowercase letters, digits, and hyphens" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SYSTEM="$ROOT/ai-system"
DEST="$ROOT/workspace/$VENTURE"

if [[ -d "$DEST" ]]; then
  echo "error: $DEST already exists — refusing to overwrite an existing venture" >&2
  exit 1
fi

# One directory per skill category, so every skill's output contract has somewhere to land.
CATEGORIES="orchestration memory finance market gtm product engineering design improvement efficiency strategy people data council legal compliance risk"
for c in $CATEGORIES; do
  mkdir -p "$DEST/$c"
done
mkdir -p "$DEST/memory/episodic" "$DEST/memory/semantic" "$DEST/memory/procedural" \
         "$DEST/memory/decisions" "$DEST/memory/entities" "$DEST/council-verdicts" "$DEST/artifacts" \
         "$DEST/telemetry/token-ledger" "$DEST/telemetry/agent-performance" "$DEST/improvement-proposals"

sed "s/<venture-id>/$VENTURE/g" "$SYSTEM/bootstrap/venture.template.yaml" > "$DEST/venture.yaml"

cat > "$DEST/README.md" <<EOF
# $VENTURE

Workspace for the venture \`$VENTURE\`, scaffolded from ai-system/bootstrap.

- \`venture.yaml\` — the intent brief. Fill this in first.
- \`memory/\` — the four memory types plus entities and decisions.
- \`council-verdicts/\` — every verdict, kept permanently including dissent.
- \`artifacts/\` — registered skill outputs.
- \`telemetry/\` — token ledger and agent performance records; the improvement loop reads these.
- \`improvement-proposals/\` — proposed changes to the system, with their trials and authorisation.
- one directory per skill category for working output.

## Next steps

1. Fill in \`venture.yaml\`. Be honest about what you do not know.
2. Run \`workflows/00-intake.yaml\` — the director will restate your intent back to you.
3. Confirm or correct that restatement before anything else is spent.
4. Then \`workflows/01-business-model-design.yaml\`.
EOF

echo "Created $DEST"
echo
echo "Next:"
echo "  1. Edit workspace/$VENTURE/venture.yaml"
echo "  2. Run ai-system/workflows/00-intake.yaml through the director"
echo "  3. Verify the system:  python3 ai-system/tests/test_system_integrity.py"
