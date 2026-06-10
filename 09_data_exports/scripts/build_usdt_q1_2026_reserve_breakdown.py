"""Export Tether Q1 2026 reserve breakdown from the local USDT_002 PDF.

The source PDF is catalogued in source_registry.csv as USDT_002. This script
parses the management reserve table so the category amounts are available as a
small reproducible CSV for issuer-detail claims.
"""

from __future__ import annotations

import csv
import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import pdfplumber


REPO_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = REPO_ROOT.parent
SOURCE_PDF = (
    WORKSPACE_ROOT
    / "stablecoin_research_docs"
    / "02_tether_usdt"
    / "Tether_USDT_Reserve_Report_Q1_2026.pdf"
)
OUT_DIR = REPO_ROOT / "09_data_exports" / "issuer_details"
BREAKDOWN_CSV = OUT_DIR / "usdt_q1_2026_reserve_breakdown.csv"

PATTERNS = [
    ("1.1", "Cash & Cash Equivalent & Other Short-Term Deposits", "U.S. Treasury Bills", r"U\.S\. Treasury Bills2\s+([\d,]+)"),
    ("1.2", "Cash & Cash Equivalent & Other Short-Term Deposits", "Overnight Reverse Repurchase Agreements", r"Overnight Reverse Repurchase Agreements3\s+([\d,]+)"),
    ("1.3", "Cash & Cash Equivalent & Other Short-Term Deposits", "Term Reverse Repurchase Agreements", r"Term Reverse Repurchase Agreements4\s+([\d,]+)"),
    ("1.4", "Cash & Cash Equivalent & Other Short-Term Deposits", "Cash & Bank Deposits", r"Cash & Bank Deposits5\s+([\d,]+)"),
    ("1.5", "Cash & Cash Equivalent & Other Short-Term Deposits", "Subtotal: Cash Equivalent & Other Short-Term Deposits", r"Subtotal: Cash Equivalent & Other Short-Term Deposits\s+([\d,]+)"),
    ("2", "Other Reserve Assets", "Corporate Bonds", r"2\. Corporate Bonds6\s+([\d,]+)"),
    ("3", "Other Reserve Assets", "Precious Metals", r"3\. Precious Metals7\s+([\d,]+)"),
    ("4", "Other Reserve Assets", "Bitcoin", r"4\. Bitcoin8\s+([\d,]+)"),
    ("5", "Other Reserve Assets", "Public Equities", r"5\. Public Equities9\s+([\d,]+)"),
    ("6", "Other Reserve Assets", "Other Investments", r"6\. Other Investments10\s+([\d,]+)"),
    ("7", "Other Reserve Assets", "Secured Loans", r"7\. Secured Loans11\s+([\d,]+)"),
    ("8", "Total", "Total Assets (1+2+3+4+5+6+7)", r"Total Assets \(1\+2\+3\+4\+5\+6\+7\)\s+([\d,]+)"),
]


def parse_amount(text: str, pattern: str) -> int:
    match = re.search(pattern, text)
    if not match:
        raise RuntimeError(f"Could not find pattern: {pattern}")
    return int(match.group(1).replace(",", ""))


def pct(amount: int, total: int) -> str:
    value = (Decimal(amount) / Decimal(total) * Decimal("100")).quantize(
        Decimal("0.0001"), rounding=ROUND_HALF_UP
    )
    return str(value)


def main() -> None:
    if not SOURCE_PDF.exists():
        raise FileNotFoundError(SOURCE_PDF)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with pdfplumber.open(SOURCE_PDF) as pdf:
        reserve_page_text = pdf.pages[8].extract_text(x_tolerance=1, y_tolerance=3) or ""

    amounts = [(order, section, category, parse_amount(reserve_page_text, pattern)) for order, section, category, pattern in PATTERNS]
    total_assets = dict((category, amount) for _, _, category, amount in amounts)["Total Assets (1+2+3+4+5+6+7)"]

    with BREAKDOWN_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "sort_order",
                "section",
                "category",
                "amount_usd",
                "share_of_total_assets_pct",
                "source_id",
                "source_page",
                "source_note",
            ],
        )
        writer.writeheader()
        for order, section, category, amount in amounts:
            writer.writerow(
                {
                    "sort_order": order,
                    "section": section,
                    "category": category,
                    "amount_usd": amount,
                    "share_of_total_assets_pct": pct(amount, total_assets),
                    "source_id": "USDT_002",
                    "source_page": "Financial Figures and Reserves Report p. 4",
                    "source_note": "Assets at 31 March 2026 reserve breakdown table.",
                }
            )

    print(f"Wrote {BREAKDOWN_CSV.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
