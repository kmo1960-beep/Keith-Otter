"""Placeholder JSON generator for research agents.

This script is intended to be populated by research agents. It produces a
structured JSON file that downstream automation (see
``.github/workflows/auto-commit-json.yml``) commits back to the repository.

Agents should extend :func:`generate_data` to populate the ``data`` list with
whatever research output they produce. The surrounding scaffolding — the
timestamp, source tag, run reason, and file writing — is ready to use as-is.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_PATH = Path("output/research_data.json")


def generate_data():
    """Build the research payload and write it to ``output/research_data.json``.

    Returns the payload dict so callers/tests can inspect the result.
    """
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "research_agent",
        "run_reason": os.environ.get("RUN_REASON", "manual"),
        # Research agents should populate this list with their findings.
        "data": [],
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")

    return payload


if __name__ == "__main__":
    result = generate_data()
    print(f"Wrote {len(result['data'])} record(s) to {OUTPUT_PATH}")
