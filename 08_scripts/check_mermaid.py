#!/usr/bin/env python3
"""Light structural check on Mermaid blocks in flow diagram markdown files."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLOW_DIR = ROOT / "06_flow_diagrams"


def check_block(label: str, block: str) -> bool:
    lines = block.splitlines()
    subs = sum(1 for l in lines if l.strip().startswith("subgraph"))
    ends = sum(1 for l in lines if l.strip() == "end")
    nodes = re.findall(r"\b([A-Za-z][A-Za-z0-9_]*)\s*\[", block)
    arrows = re.findall(r"(-->|-\.-?>|---)", block)
    ok = subs == ends
    print(f"  {label}")
    print(f"    lines: {len(lines)}")
    print(f"    subgraphs: {subs}, ends: {ends}  -> balanced: {ok}")
    print(f"    unique node ids: {len(set(nodes))}")
    print(f"    arrow tokens: {len(arrows)}")
    return ok


def main() -> int:
    overall = True
    for path in sorted(FLOW_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", text, re.DOTALL)
        print(f"{path.name}: {len(blocks)} mermaid block(s)")
        for i, blk in enumerate(blocks, 1):
            if not check_block(f"block {i}", blk):
                overall = False
        print()
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
