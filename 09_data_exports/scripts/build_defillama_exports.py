#!/usr/bin/env python3
"""Build reproducible CSV exports from archived DeFiLlama stablecoin JSON.

This script intentionally uses local archived JSON only. It does not fetch
live dashboard data and it does not infer payment demand from supply.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = REPO_ROOT.parent
SOURCE_DIR = WORKSPACE_ROOT / "stablecoin_deficiency_sources_package" / "deficiency_downloads" / "market_data"
OUTPUT_DIR = REPO_ROOT / "09_data_exports" / "stablecoin_supply"
SUPPLY_JSON = SOURCE_DIR / "defillama_stablecoins_includePrices.json"
CHAIN_JSON = SOURCE_DIR / "defillama_stablecoinchains.json"


def get_pegged_usd(value: object) -> float | None:
    if isinstance(value, dict):
        amount = value.get("peggedUSD")
        if isinstance(amount, (int, float)):
            return float(amount)
    if isinstance(value, (int, float)):
        return float(value)
    return None


def write_supply_snapshot(data: dict) -> Path:
    path = OUTPUT_DIR / "defillama_stablecoin_supply_snapshot.csv"
    rows = []
    for asset in data.get("peggedAssets", []):
        rows.append(
            {
                "source_id": "DEFILLAMA_001",
                "asset_id": asset.get("id", ""),
                "name": asset.get("name", ""),
                "symbol": asset.get("symbol", ""),
                "peg_type": asset.get("pegType", ""),
                "peg_mechanism": asset.get("pegMechanism", ""),
                "circulating_usd": get_pegged_usd(asset.get("circulating")),
                "circulating_prev_day_usd": get_pegged_usd(asset.get("circulatingPrevDay")),
                "circulating_prev_week_usd": get_pegged_usd(asset.get("circulatingPrevWeek")),
                "circulating_prev_month_usd": get_pegged_usd(asset.get("circulatingPrevMonth")),
            }
        )

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_chain_distribution(data: dict) -> Path:
    path = OUTPUT_DIR / "defillama_stablecoin_chain_distribution.csv"
    rows = []
    chains = data.get("chains", []) if isinstance(data, dict) else data
    for chain in chains:
        rows.append(
            {
                "source_id": "DEFILLAMA_002",
                "chain": chain.get("name", ""),
                "token_symbol": chain.get("tokenSymbol", ""),
                "gecko_id": chain.get("gecko_id", ""),
                "total_circulating_usd": get_pegged_usd(chain.get("totalCirculatingUSD")),
            }
        )

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_manifest(outputs: list[Path]) -> Path:
    path = REPO_ROOT / "09_data_exports" / "data_manifest.csv"
    rows = [
        {
            "dataset": "defillama_stablecoin_supply_snapshot",
            "output_path": "09_data_exports/stablecoin_supply/defillama_stablecoin_supply_snapshot.csv",
            "source_ids": "DEFILLAMA_001",
            "input_path": str(SUPPLY_JSON.relative_to(WORKSPACE_ROOT)).replace("\\", "/"),
            "method": "Local JSON to CSV; one row per pegged asset; values are supply/market-cap style data, not payment volume.",
            "limitations": "Snapshot date follows archived JSON fetch date in source registry; not adjusted transfer volume.",
        },
        {
            "dataset": "defillama_stablecoin_chain_distribution",
            "output_path": "09_data_exports/stablecoin_supply/defillama_stablecoin_chain_distribution.csv",
            "source_ids": "DEFILLAMA_002",
            "input_path": str(CHAIN_JSON.relative_to(WORKSPACE_ROOT)).replace("\\", "/"),
            "method": "Local JSON to CSV; one row per chain.",
            "limitations": "Chain distribution is supply context only; not payment demand.",
        },
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with SUPPLY_JSON.open(encoding="utf-8-sig") as f:
        supply_data = json.load(f)
    with CHAIN_JSON.open(encoding="utf-8-sig") as f:
        chain_data = json.load(f)

    outputs = [write_supply_snapshot(supply_data), write_chain_distribution(chain_data)]
    manifest = write_manifest(outputs)
    print("Wrote:")
    for output in outputs:
        print(f"  {output.relative_to(REPO_ROOT)}")
    print(f"  {manifest.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
