#!/usr/bin/env python3
"""Print the high-priority external fetch queue."""
from pathlib import Path
import csv
root = Path(__file__).resolve().parents[1]
q = root / '01_sources' / 'external_fetch_queue.csv'
with q.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
for r in rows:
    if r.get('priority') == 'high':
        print(f"{r['id']}: {r['title']} — {r['action_needed']}")
