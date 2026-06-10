"""Build public hourly price timelines for selected failure cases.

The script uses CryptoCompare's public histohour endpoint to create a
reproducible proxy timeline for old depeg/stress windows. These outputs are
useful for coarse, public, hourly OHLCV context. They are not a substitute for
paid exchange-level or tick-level feeds such as Kaiko or Coin Metrics.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "09_data_exports" / "failure_case_timelines"
RAW_PATH = OUT_DIR / "cryptocompare_failure_case_histohour_raw.json"
PRICES_CSV_PATH = OUT_DIR / "cryptocompare_failure_case_hourly_prices.csv"
SUMMARY_CSV_PATH = OUT_DIR / "cryptocompare_failure_case_summary.csv"

API_BASE = "https://min-api.cryptocompare.com/data/v2/histohour"

CASES = [
    {
        "case_id": "usdc_svb_2023",
        "case_name": "USDC / Silicon Valley Bank depeg",
        "symbol": "USDC",
        "from_utc": "2023-03-09T00:00:00Z",
        "to_utc": "2023-03-14T00:00:00Z",
        "context_claims": "CLAIM_108; CLAIM_109",
    },
    {
        "case_id": "terra_ust_2022",
        "case_name": "Terra UST collapse",
        "symbol": "USTC",
        "from_utc": "2022-05-07T00:00:00Z",
        "to_utc": "2022-05-15T00:00:00Z",
        "context_claims": "CLAIM_107",
    },
    {
        "case_id": "iron_finance_iron_2021",
        "case_name": "Iron Finance IRON depeg",
        "symbol": "IRON",
        "from_utc": "2021-06-15T00:00:00Z",
        "to_utc": "2021-06-21T00:00:00Z",
        "context_claims": "CLAIM_111",
    },
    {
        "case_id": "iron_finance_titan_2021",
        "case_name": "Iron Finance TITAN collapse",
        "symbol": "TITAN",
        "from_utc": "2021-06-15T00:00:00Z",
        "to_utc": "2021-06-21T00:00:00Z",
        "context_claims": "CLAIM_111",
    },
    {
        "case_id": "maker_dai_black_thursday_2020",
        "case_name": "MakerDAO Black Thursday DAI stress",
        "symbol": "DAI",
        "from_utc": "2020-03-10T00:00:00Z",
        "to_utc": "2020-03-16T00:00:00Z",
        "context_claims": "CLAIM_135; CLAIM_136; CLAIM_137",
    },
]


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def ts(dt: datetime) -> int:
    return int(dt.timestamp())


def iso(ts_value: int) -> str:
    return datetime.fromtimestamp(ts_value, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def fetch_case(case: dict) -> dict:
    start = parse_utc(case["from_utc"])
    end = parse_utc(case["to_utc"])
    hours = int((end - start).total_seconds() // 3600)
    params = {
        "fsym": case["symbol"],
        "tsym": "USD",
        "limit": hours,
        "toTs": ts(end),
    }
    url = f"{API_BASE}?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": "stablecoin-research/1.0"})
    with urlopen(request, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if payload.get("Response") != "Success":
        raise RuntimeError(f"CryptoCompare error for {case['case_id']}: {payload.get('Message')}")
    rows = payload.get("Data", {}).get("Data", [])
    if not rows:
        raise RuntimeError(f"CryptoCompare returned no rows for {case['case_id']}")
    return {"request_url": url, "case": case, "payload": payload}


def flatten(raw_cases: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for raw_case in raw_cases:
        case = raw_case["case"]
        for row in raw_case["payload"]["Data"]["Data"]:
            rows.append(
                {
                    "case_id": case["case_id"],
                    "case_name": case["case_name"],
                    "symbol": case["symbol"],
                    "tsym": "USD",
                    "time": row.get("time"),
                    "utc": iso(int(row.get("time"))),
                    "open": row.get("open"),
                    "high": row.get("high"),
                    "low": row.get("low"),
                    "close": row.get("close"),
                    "volumefrom": row.get("volumefrom"),
                    "volumeto": row.get("volumeto"),
                    "conversionType": row.get("conversionType"),
                    "conversionSymbol": row.get("conversionSymbol"),
                    "context_claims": case["context_claims"],
                }
            )
    return rows


def first_below(rows: list[dict], threshold: float) -> str:
    for row in rows:
        if float(row["close"]) < threshold:
            return row["utc"]
    return ""


def first_close_at_or_above_after_min(rows: list[dict], threshold: float, min_time: int) -> str:
    for row in rows:
        if int(row["time"]) > min_time and float(row["close"]) >= threshold:
            return row["utc"]
    return ""


def summarise(rows: list[dict]) -> list[dict]:
    by_case: dict[str, list[dict]] = {}
    for row in rows:
        by_case.setdefault(row["case_id"], []).append(row)

    summaries: list[dict] = []
    for case_id, case_rows in by_case.items():
        case_rows.sort(key=lambda row: int(row["time"]))
        first = case_rows[0]
        last = case_rows[-1]
        min_close = min(case_rows, key=lambda row: float(row["close"]))
        min_low = min(case_rows, key=lambda row: float(row["low"]))
        max_high = max(case_rows, key=lambda row: float(row["high"]))
        nonzero_close_count = sum(1 for row in case_rows if float(row["close"]) != 0.0)
        usable_hourly_proxy = "yes" if nonzero_close_count > 0 else "no"
        summaries.append(
            {
                "case_id": case_id,
                "case_name": first["case_name"],
                "symbol": first["symbol"],
                "row_count": len(case_rows),
                "start_utc": first["utc"],
                "end_utc": last["utc"],
                "first_close": first["close"],
                "last_close": last["close"],
                "min_close": min_close["close"],
                "min_close_utc": min_close["utc"],
                "min_low": min_low["low"],
                "min_low_utc": min_low["utc"],
                "max_high": max_high["high"],
                "max_high_utc": max_high["utc"],
                "nonzero_close_count": nonzero_close_count,
                "usable_hourly_proxy": usable_hourly_proxy,
                "first_close_below_0_99_utc": first_below(case_rows, 0.99),
                "first_close_below_0_95_utc": first_below(case_rows, 0.95),
                "first_close_below_0_90_utc": first_below(case_rows, 0.90),
                "first_close_at_or_above_0_99_after_min_utc": first_close_at_or_above_after_min(
                    case_rows, 0.99, int(min_close["time"])
                ),
                "context_claims": first["context_claims"],
            }
        )
    return sorted(summaries, key=lambda row: row["case_id"])


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_cases = [fetch_case(case) for case in CASES]
    RAW_PATH.write_text(json.dumps(raw_cases, ensure_ascii=False, indent=2), encoding="utf-8")

    rows = flatten(raw_cases)
    summaries = summarise(rows)
    write_csv(PRICES_CSV_PATH, rows)
    write_csv(SUMMARY_CSV_PATH, summaries)

    print(f"Wrote {len(rows)} hourly rows to {PRICES_CSV_PATH}")
    print(f"Wrote {len(summaries)} summary rows to {SUMMARY_CSV_PATH}")
    print(f"Raw CryptoCompare cache: {RAW_PATH}")


if __name__ == "__main__":
    main()
