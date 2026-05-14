#!/usr/bin/env python3
"""Report source registry availability and stale fetch-queue items."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
REGISTRY = REPO_ROOT / "01_sources" / "source_registry.csv"
EXTERNAL_QUEUE = REPO_ROOT / "01_sources" / "external_fetch_queue.csv"
MANUAL_QUEUE = REPO_ROOT / "01_sources" / "manual_download_needed.csv"

ARCHIVED_STATUSES = {
    "downloaded",
    "html_saved",
    "dynamic_html_saved",
    "api_saved",
    "download_script",
}
DEFICIENT_STATUSES = {"missing", "url_only", "manual_needed"}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def resolve_local_path(value: str) -> Path | None:
    if not value:
        return None
    path = Path(value)
    if path.is_absolute():
        return path

    workspace_candidate = WORKSPACE_ROOT / path
    if workspace_candidate.exists():
        return workspace_candidate

    return REPO_ROOT / path


def print_rows(title: str, rows: list[str]) -> None:
    print(f"\n{title}")
    if not rows:
        print("  none")
        return
    for row in rows:
        print(f"  {row}")


def main() -> int:
    registry_rows = read_csv(REGISTRY)
    if not registry_rows:
        print(f"source registry not found or empty: {REGISTRY}")
        return 1

    status_counts = Counter((r.get("status") or "blank").strip() for r in registry_rows)
    print("Source registry status counts")
    for status, count in sorted(status_counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"  {status}: {count}")

    missing_local_files: list[str] = []
    deficient_rows: list[str] = []
    high_priority_attention: list[str] = []

    for row in registry_rows:
        source_id = row.get("id", "")
        status = (row.get("status") or "").strip()
        priority = (row.get("priority") or "").strip()
        title = row.get("title", "")
        local_path = (row.get("local_path") or "").strip()

        resolved = resolve_local_path(local_path)
        if status in ARCHIVED_STATUSES and resolved is not None and not resolved.exists():
            missing_local_files.append(f"{source_id}: {local_path} ({title})")

        if status in DEFICIENT_STATUSES or not local_path:
            deficient_rows.append(f"{source_id}: {status or 'blank'} - {title}")
            if priority == "high":
                high_priority_attention.append(f"{source_id}: {status or 'blank'} - {title}")

    print_rows("Archived rows whose local_path is missing", missing_local_files)
    print_rows("High-priority rows needing attention", high_priority_attention)
    print_rows("All deficient or no-local-path rows", deficient_rows)

    external_rows = read_csv(EXTERNAL_QUEUE)
    manual_rows = read_csv(MANUAL_QUEUE)
    if external_rows or manual_rows:
        print("\nLegacy queue snapshot")
        if external_rows:
            print(f"  external_fetch_queue.csv rows: {len(external_rows)}")
        if manual_rows:
            print(f"  manual_download_needed.csv rows: {len(manual_rows)}")
        print("  note: queues are handoff trackers; source_registry.csv is the current availability source of truth.")

    return 1 if missing_local_files or high_priority_attention else 0


if __name__ == "__main__":
    raise SystemExit(main())
