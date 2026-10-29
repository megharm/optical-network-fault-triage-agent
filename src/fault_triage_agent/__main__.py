"""Run: python -m fault_triage_agent"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "synthetic"


def main() -> None:
    alarms = json.loads((DATA_DIR / "alarms.json").read_text())
    for alarm in alarms:
        print(f"{alarm['severity']:<8} {alarm['device']:<12} {alarm['port']:<10} {alarm['type']}")


if __name__ == "__main__":
    main()
