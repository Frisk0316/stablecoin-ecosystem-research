#!/usr/bin/env python3
"""Validate the master claim table.
Usage: python 08_scripts/validate_claim_table.py
"""
from pathlib import Path
import csv, sys
root = Path(__file__).resolve().parents[1]
claim_path = root / '03_claim_tables' / 'claim_table_master.csv'
source_path = root / '01_sources' / 'source_registry.csv'
errors = []
with source_path.open(encoding='utf-8-sig', newline='') as f:
    source_ids = {r['id'] for r in csv.DictReader(f)}
with claim_path.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
required = ['claim_id','claim','source_id','page_or_section','evidence','confidence']
for i, r in enumerate(rows, start=2):
    for col in required:
        if not r.get(col, '').strip():
            errors.append(f'Row {i}: missing {col}')
    conf = r.get('confidence','').strip().lower()
    if conf not in {'high','medium','low'}:
        errors.append(f'Row {i}: invalid confidence {conf!r}')
    sid = r.get('source_id','').strip()
    if sid and sid not in source_ids and not sid.endswith('_PENDING') and sid != 'RESEARCH_BRIEF':
        errors.append(f'Row {i}: source_id not found in registry: {sid}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(rows)} claims validated.')
