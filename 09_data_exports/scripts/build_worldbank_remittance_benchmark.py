"""Build World Bank remittance-cost benchmark exports.

This script downloads the World Bank WDI indicator
SI.RMT.COST.IB.ZS ("Average transaction cost of sending remittances to a
specific country (%)"), caches the raw API response, and writes reproducible
CSV outputs for off-chain remittance-cost benchmark context.

It is not an adjusted stablecoin payment-volume export.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "09_data_exports" / "remittance_benchmark"
RAW_PATH = OUT_DIR / "worldbank_si_rmt_cost_ib_zs_raw.json"
FULL_CSV_PATH = OUT_DIR / "worldbank_remittance_cost_by_country_year.csv"
LATEST_CSV_PATH = OUT_DIR / "worldbank_remittance_cost_latest_by_country.csv"

API_URL = (
    "https://api.worldbank.org/v2/country/all/indicator/SI.RMT.COST.IB.ZS"
    "?format=json&per_page=20000"
)


def fetch_payload() -> tuple[dict, list[dict]]:
    with urlopen(API_URL, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if not isinstance(payload, list) or len(payload) != 2:
        raise RuntimeError("Unexpected World Bank API response shape")
    metadata, rows = payload
    if not isinstance(metadata, dict) or not isinstance(rows, list):
        raise RuntimeError("Unexpected World Bank API metadata or rows")
    return metadata, rows


def normalise_rows(rows: list[dict]) -> list[dict]:
    normalised: list[dict] = []
    for row in rows:
        value = row.get("value")
        normalised.append(
            {
                "country_id": (row.get("country") or {}).get("id", ""),
                "country_name": (row.get("country") or {}).get("value", ""),
                "countryiso3code": row.get("countryiso3code", ""),
                "year": row.get("date", ""),
                "indicator_id": (row.get("indicator") or {}).get("id", ""),
                "indicator_name": (row.get("indicator") or {}).get("value", ""),
                "value_percent": "" if value is None else value,
                "unit": row.get("unit", ""),
                "obs_status": row.get("obs_status", ""),
                "decimal": row.get("decimal", ""),
            }
        )
    normalised.sort(key=lambda r: (r["countryiso3code"], r["year"]))
    return normalised


def latest_non_null(rows: list[dict]) -> list[dict]:
    latest_by_country: dict[str, dict] = {}
    for row in rows:
        if row["value_percent"] == "":
            continue
        key = row["countryiso3code"] or row["country_id"]
        current = latest_by_country.get(key)
        if current is None or int(row["year"]) > int(current["year"]):
            latest_by_country[key] = row
    return sorted(latest_by_country.values(), key=lambda r: r["countryiso3code"])


def write_csv(path: Path, rows: list[dict]) -> None:
    fieldnames = [
        "country_id",
        "country_name",
        "countryiso3code",
        "year",
        "indicator_id",
        "indicator_name",
        "value_percent",
        "unit",
        "obs_status",
        "decimal",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata, raw_rows = fetch_payload()
    RAW_PATH.write_text(
        json.dumps({"metadata": metadata, "rows": raw_rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    rows = normalise_rows(raw_rows)
    latest = latest_non_null(rows)
    write_csv(FULL_CSV_PATH, rows)
    write_csv(LATEST_CSV_PATH, latest)

    print(f"World Bank metadata: lastupdated={metadata.get('lastupdated')} total={metadata.get('total')}")
    print(f"Wrote {len(rows)} rows to {FULL_CSV_PATH}")
    print(f"Wrote {len(latest)} latest non-null rows to {LATEST_CSV_PATH}")
    print(f"Raw API cache: {RAW_PATH}")


if __name__ == "__main__":
    main()
