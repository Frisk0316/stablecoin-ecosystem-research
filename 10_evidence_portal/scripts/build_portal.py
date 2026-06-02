from __future__ import annotations

import csv
import html
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PORTAL_ROOT = REPO_ROOT / "10_evidence_portal"
SITE_ROOT = PORTAL_ROOT / "site"
DATA_ROOT = SITE_ROOT / "data"

CLAIM_TABLE = REPO_ROOT / "03_claim_tables" / "claim_table_master.csv"
SOURCE_REGISTRY = REPO_ROOT / "01_sources" / "source_registry.csv"
MATRIX_DIR = REPO_ROOT / "04_matrices"
REPORT_CANDIDATES = [
    REPO_ROOT / "07_final_report" / "stablecoin_academic_report_v1_0.md",
    REPO_ROOT / "07_final_report" / "archive" / "v0_2" / "stablecoin_ecosystem_research_report_v0_2.md",
]

CLAIM_RE = re.compile(r"\bCLAIM_\d{3}\b")

PAGE_CONFIG = {
    "index.html": {
        "title": "Executive Summary",
        "sections": ["Abstract", "Executive Summary"],
        "description": "Thesis, main findings, and evidence-backed conclusions.",
    },
    "issuer-comparison.html": {
        "title": "Issuer Comparison",
        "sections": [
            "2. Taxonomy Of Stablecoins",
            "3. Issuer And Redemption Structure",
            "Chapter 1 - Stablecoins As On-Chain Dollar Infrastructure",
            "Chapter 2 - Issuer Comparison",
        ],
        "description": "Issuer design, redemption rights, reserve structures, and stablecoin types.",
    },
    "regulation.html": {
        "title": "Regulation",
        "sections": ["5. Regulatory Comparison", "Chapter 4 - Law And Regulation"],
        "description": "GENIUS Act, MiCA, NYDFS, BoE, and EU supervisory rules.",
    },
    "central-bank-views.html": {
        "title": "Central Bank Views",
        "sections": [
            "6. Central Bank And International Institution Views",
            "Chapter 5 - Central-Bank And International Institution Views",
        ],
        "description": "BIS, ECB, Fed, IMF, FSB, and Taiwan CBC policy perspectives.",
    },
    "payment-settlement.html": {
        "title": "Payment And Settlement",
        "sections": ["7. Stablecoins In Payment And Settlement", "Chapter 6 - USDPT And Cross-Border Payments"],
        "description": "Correspondent banking, SWIFT messaging, settlement rails, Western Union, and USDPT.",
    },
    "onchain-data.html": {
        "title": "On-chain Data",
        "sections": ["8. On-Chain Data And Payment Demand", "Chapter 7 - On-Chain Data And Payment Demand"],
        "description": "Supply data, transfer-volume limits, and reproducible exports.",
    },
    "failure-cases.html": {
        "title": "Failure Cases",
        "sections": ["9. Failure Cases And Stress Scenarios", "Chapter 8 - Failure Cases"],
        "description": "Terra, Iron Finance, USDC/SVB, Tether/Bitfinex, DAI/USDS, and USDe stress channels.",
    },
    "methodology.html": {
        "title": "Methodology",
        "sections": ["Methodology", "Appendix C - Methodology"],
        "description": "Traceability rules, confidence levels, source handling, and unresolved limits.",
    },
}

TOPIC_GROUPS = {
    "issuer-comparison.html": [
        ("USDC", "topic-issuer-usdc.html", ["USDC"]),
        ("USDT", "topic-issuer-usdt.html", ["USDT", "Tether"]),
        ("PYUSD / USDP / USDG", "topic-issuer-paxos-family.html", ["PYUSD", "USDP", "USDG", "Paxos"]),
        ("RLUSD", "topic-issuer-rlusd.html", ["RLUSD", "Ripple"]),
        ("FDUSD", "topic-issuer-fdusd.html", ["FDUSD", "FD121"]),
        ("GUSD", "topic-issuer-gusd.html", ["GUSD", "Gemini"]),
        ("DAI / USDS", "topic-issuer-dai-usds.html", ["DAI", "USDS", "Maker", "Sky"]),
        ("USDe", "topic-issuer-usde.html", ["USDe", "Ethena"]),
    ],
    "regulation.html": [
        ("GENIUS Act", "topic-reg-genius.html", ["GENIUS"]),
        ("MiCA", "topic-reg-mica.html", ["MiCA", "EMT", "ART"]),
        ("NYDFS", "topic-reg-nydfs.html", ["NYDFS"]),
        ("BoE", "topic-reg-boe.html", ["BoE", "Bank of England"]),
        ("ESMA / EBA", "topic-reg-esma-eba.html", ["ESMA", "EBA"]),
    ],
    "central-bank-views.html": [
        ("BIS", "topic-cb-bis.html", ["BIS"]),
        ("ECB", "topic-cb-ecb.html", ["ECB"]),
        ("Fed", "topic-cb-fed.html", ["Fed", "Federal Reserve"]),
        ("IMF", "topic-cb-imf.html", ["IMF"]),
        ("FSB", "topic-cb-fsb.html", ["FSB"]),
        ("Taiwan CBC", "topic-cb-taiwan-cbc.html", ["Taiwan", "CBC", "Central Bank of the Republic of China"]),
    ],
    "payment-settlement.html": [
        ("Correspondent Banking", "topic-pay-correspondent-banking.html", ["Correspondent", "BIS_004"]),
        ("Fedwire", "topic-pay-fedwire.html", ["Fedwire"]),
        ("Western Union", "topic-pay-western-union.html", ["Western Union"]),
        ("USDPT", "topic-pay-usdpt.html", ["USDPT", "Anchorage", "Fireblocks"]),
    ],
    "onchain-data.html": [
        ("DeFiLlama", "topic-data-defillama.html", ["DeFiLlama", "DEFILLAMA"]),
        ("Visa / Artemis", "topic-data-visa-artemis.html", ["Visa", "Artemis"]),
        ("Cambridge", "topic-data-cambridge.html", ["Cambridge"]),
    ],
    "failure-cases.html": [
        ("Terra UST", "topic-fail-terra.html", ["Terra", "UST", "LUNA"]),
        ("Iron Finance", "topic-fail-iron.html", ["Iron", "TITAN"]),
        ("USDC / SVB", "topic-fail-usdc-svb.html", ["SVB", "Silicon Valley Bank"]),
        ("USDT Reserve Controversy", "topic-fail-usdt-nyag.html", ["NYAG", "Bitfinex", "Tether"]),
        ("DAI / USDS Stress", "topic-fail-dai-usds.html", ["DAI", "USDS", "Maker"]),
        ("USDe Stress", "topic-fail-usde.html", ["USDe", "Ethena"]),
    ],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def load_report() -> tuple[Path, str]:
    for path in REPORT_CANDIDATES:
        if path.exists():
            return path, path.read_text(encoding="utf-8-sig")
    raise FileNotFoundError("No report markdown file found.")


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return slug or "section"


def extract_sections(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = "Front Matter"
    sections[current] = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append(line)
    return {name: "\n".join(lines).strip() for name, lines in sections.items()}


def split_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    in_table = False
    for line in markdown.splitlines():
        stripped = line.strip()
        is_table = stripped.startswith("|") and stripped.endswith("|")
        if not stripped and current:
            blocks.append("\n".join(current).strip())
            current = []
            in_table = False
            continue
        if is_table:
            if current and not in_table:
                blocks.append("\n".join(current).strip())
                current = []
            in_table = True
            current.append(line)
        else:
            in_table = False
            current.append(line)
    if current:
        blocks.append("\n".join(current).strip())
    return [block for block in blocks if block]


def source_href(source: dict[str, str]) -> str:
    url = (source.get("url") or "").strip()
    if url:
        return url
    local_path = (source.get("local_path") or "").strip().replace("\\", "/")
    if local_path:
        return "../../../" + local_path
    return ""


def matrix_hits(claim: dict[str, str], matrices: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    claim_id = claim.get("claim_id", "")
    source_id = claim.get("source_id", "")
    claim_text = claim.get("claim", "")
    tokens = [claim_id, source_id]
    for term in re.findall(r"\b[A-Z]{2,8}\b", claim_text):
        if term not in {"THE", "AND", "USD"}:
            tokens.append(term)

    hits: list[dict[str, str]] = []
    for matrix_name, rows in matrices.items():
        for idx, row in enumerate(rows, start=2):
            haystack = " ".join(str(value) for value in row.values())
            if any(token and token in haystack for token in tokens):
                label = row.get("stablecoin") or row.get("framework") or row.get("source") or row.get("topic") or row.get("case") or f"row {idx}"
                hits.append({"matrix": matrix_name, "row": str(idx), "label": label})
                break
    return hits[:4]


def markdown_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = CLAIM_RE.sub(lambda m: f'<a class="claim-chip" href="claim-explorer.html#claim-{m.group(0)}">{m.group(0)}</a>', escaped)
    return escaped


def render_block(block: str, claims_by_id: dict[str, dict[str, str]], sources_by_id: dict[str, dict[str, str]], matrices: dict[str, list[dict[str, str]]]) -> str:
    if block.startswith("### "):
        return f'<h3 id="{slugify(block[4:])}">{markdown_inline(block[4:])}</h3>'
    if block.startswith("#### "):
        return f'<h4 id="{slugify(block[5:])}">{markdown_inline(block[5:])}</h4>'
    if block.startswith("|") and "\n|" in block:
        rows = [line for line in block.splitlines() if line.strip().startswith("|")]
        table_html = ["<div class=\"table-wrap\"><table>"]
        for idx, row in enumerate(rows):
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            if idx == 1 and all(set(cell) <= {"-", ":"} for cell in cells):
                continue
            tag = "th" if idx == 0 else "td"
            table_html.append("<tr>" + "".join(f"<{tag}>{markdown_inline(cell)}</{tag}>" for cell in cells) + "</tr>")
        table_html.append("</table></div>")
        return "\n".join(table_html)

    claim_ids = sorted(set(CLAIM_RE.findall(block)))
    conclusion = markdown_inline(" ".join(line.strip() for line in block.splitlines()))
    if not claim_ids:
        return f'<article class="prose-block"><p>{conclusion}</p></article>'

    cards = []
    for claim_id in claim_ids:
        claim = claims_by_id.get(claim_id)
        if not claim:
            cards.append(f'<div class="evidence-card missing"><strong>{claim_id}</strong><p>Claim not found in claim table.</p></div>')
            continue
        source = sources_by_id.get(claim.get("source_id", ""), {})
        href = source_href(source)
        link_html = f'<a href="{html.escape(href)}">Open source</a>' if href else "<span>No source link recorded</span>"
        hits = matrix_hits(claim, matrices)
        if hits:
            hit_html = "".join(
                f'<span class="matrix-pill">{html.escape(hit["matrix"])} r{html.escape(hit["row"])}: {html.escape(hit["label"])}</span>'
                for hit in hits
            )
        else:
            hit_html = '<span class="muted">No related matrix row auto-detected.</span>'
        cards.append(
            f'''
            <div class="evidence-card" id="claim-{html.escape(claim_id)}">
              <div class="evidence-topline">
                <strong>{html.escape(claim_id)}</strong>
                <span class="confidence confidence-{html.escape((claim.get("confidence") or "unknown").lower())}">{html.escape(claim.get("confidence") or "unknown")}</span>
              </div>
              <p class="claim-text">{markdown_inline(claim.get("claim", ""))}</p>
              <dl>
                <dt>source_id</dt><dd>{html.escape(claim.get("source_id", ""))}</dd>
                <dt>document</dt><dd>{html.escape(source.get("title", "Source not found"))}</dd>
                <dt>publisher</dt><dd>{html.escape(source.get("publisher", ""))}</dd>
                <dt>page_or_section</dt><dd>{html.escape(claim.get("page_or_section", ""))}</dd>
                <dt>evidence</dt><dd>{html.escape(claim.get("evidence", ""))}</dd>
                <dt>matrix</dt><dd class="matrix-list">{hit_html}</dd>
                <dt>source</dt><dd>{link_html}</dd>
              </dl>
            </div>
            '''
        )
    return f'''
    <article class="evidence-block">
      <div class="conclusion">
        <div class="eyebrow">Conclusion</div>
        <p>{conclusion}</p>
      </div>
      <div class="evidence-stack">
        {"".join(cards)}
      </div>
    </article>
    '''


def render_section_content(section_names: list[str], sections: dict[str, str], claims_by_id: dict[str, dict[str, str]], sources_by_id: dict[str, dict[str, str]], matrices: dict[str, list[dict[str, str]]]) -> str:
    html_parts: list[str] = []
    used = False
    for section_name in section_names:
        body = sections.get(section_name)
        if not body:
            continue
        used = True
        html_parts.append(f'<section class="report-section"><h2 id="{slugify(section_name)}">{html.escape(section_name)}</h2>')
        for block in split_blocks(body):
            html_parts.append(render_block(block, claims_by_id, sources_by_id, matrices))
        html_parts.append("</section>")
    if not used:
        html_parts.append('<p class="muted">No matching section found in the selected report markdown.</p>')
    return "\n".join(html_parts)


def nav_html(active: str) -> str:
    items = [
        ("index.html", "Executive Summary"),
        ("issuer-comparison.html", "Issuer Comparison"),
        ("regulation.html", "Regulation"),
        ("central-bank-views.html", "Central Bank Views"),
        ("payment-settlement.html", "Payment And Settlement"),
        ("onchain-data.html", "On-chain Data"),
        ("failure-cases.html", "Failure Cases"),
        ("source-registry.html", "Source Registry"),
        ("claim-explorer.html", "Claim Explorer"),
        ("methodology.html", "Methodology"),
    ]
    return "\n".join(
        f'<a class="{"active" if href == active else ""}" href="{href}">{label}</a>'
        for href, label in items
    )


def topic_links(active: str) -> str:
    topics = TOPIC_GROUPS.get(active)
    if not topics:
        return ""
    links = "".join(f'<a href="{href}">{html.escape(label)}</a>' for label, href, _ in topics)
    return f'<section class="topic-strip"><p class="eyebrow">Topic Drill-down</p><div>{links}</div></section>'


def shell(title: str, active: str, description: str, body: str, report_name: str) -> str:
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Stablecoin Evidence Portal</title>
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <aside class="sidebar">
    <a class="brand" href="index.html">
      <span class="brand-mark"></span>
      <span>Stablecoin Evidence Portal</span>
    </a>
    <nav>{nav_html(active)}</nav>
  </aside>
  <main>
    <header class="page-header">
      <div>
        <p class="eyebrow">Claim-backed research interface</p>
        <h1>{html.escape(title)}</h1>
        <p>{html.escape(description)}</p>
        <p class="source-note">Generated from <code>{html.escape(report_name)}</code>, claim table, source registry, and matrices.</p>
      </div>
      <div class="evidence-map" aria-hidden="true">
        <span></span><span></span><span></span><span></span><span></span>
      </div>
    </header>
    {topic_links(active)}
    {body}
  </main>
  <script src="assets/portal.js"></script>
</body>
</html>
'''


def claim_search_text(claim: dict[str, str], sources_by_id: dict[str, dict[str, str]]) -> str:
    source = sources_by_id.get(claim.get("source_id", ""), {})
    return " ".join(
        [
            claim.get("claim_id", ""),
            claim.get("claim", ""),
            claim.get("source_id", ""),
            claim.get("page_or_section", ""),
            claim.get("evidence", ""),
            claim.get("notes", ""),
            " ".join(source.values()),
        ]
    ).lower()


def source_search_text(source: dict[str, str]) -> str:
    return " ".join(source.values()).lower()


def matches_terms(text: str, terms: list[str]) -> bool:
    return any(term.lower() in text for term in terms)


def build_topic_page(
    label: str,
    filename: str,
    terms: list[str],
    claims: list[dict[str, str]],
    sources: list[dict[str, str]],
    sources_by_id: dict[str, dict[str, str]],
    matrices: dict[str, list[dict[str, str]]],
    report_name: str,
) -> str:
    matched_claims = [claim for claim in claims if matches_terms(claim_search_text(claim, sources_by_id), terms)]
    matched_sources = [source for source in sources if matches_terms(source_search_text(source), terms)]
    claim_cards = []
    for claim in matched_claims:
        claim_id = claim.get("claim_id", "")
        source = sources_by_id.get(claim.get("source_id", ""), {})
        href = source_href(source)
        link_html = f'<a href="{html.escape(href)}">Open source</a>' if href else "<span>No source link recorded</span>"
        hits = matrix_hits(claim, matrices)
        hit_html = "".join(
            f'<span class="matrix-pill">{html.escape(hit["matrix"])} r{html.escape(hit["row"])}: {html.escape(hit["label"])}</span>'
            for hit in hits
        ) or '<span class="muted">No matrix hit auto-detected.</span>'
        claim_cards.append(
            f'''
            <article class="explorer-card" id="claim-{html.escape(claim_id)}">
              <div class="evidence-topline">
                <strong>{html.escape(claim_id)}</strong>
                <span class="confidence confidence-{html.escape((claim.get("confidence") or "unknown").lower())}">{html.escape(claim.get("confidence") or "unknown")}</span>
              </div>
              <p>{markdown_inline(claim.get("claim", ""))}</p>
              <dl>
                <dt>source_id</dt><dd>{html.escape(claim.get("source_id", ""))}</dd>
                <dt>document</dt><dd>{html.escape(source.get("title", ""))}</dd>
                <dt>page_or_section</dt><dd>{html.escape(claim.get("page_or_section", ""))}</dd>
                <dt>evidence</dt><dd>{html.escape(claim.get("evidence", ""))}</dd>
                <dt>matrix</dt><dd class="matrix-list">{hit_html}</dd>
                <dt>source</dt><dd>{link_html}</dd>
              </dl>
            </article>
            '''
        )
    source_rows = []
    for source in matched_sources:
        href = source_href(source)
        link_html = f'<a href="{html.escape(href)}">Open</a>' if href else ""
        source_rows.append(
            f'''
            <tr>
              <td><code>{html.escape(source.get("id", ""))}</code></td>
              <td>{html.escape(source.get("category", ""))}</td>
              <td>{html.escape(source.get("publisher", ""))}</td>
              <td>{html.escape(source.get("title", ""))}</td>
              <td>{html.escape(source.get("status", ""))}</td>
              <td>{link_html}</td>
            </tr>
            '''
        )
    source_table = ""
    if source_rows:
        source_table = f'''
        <h2>Related Sources</h2>
        <div class="table-wrap">
          <table>
            <thead><tr><th>source_id</th><th>category</th><th>publisher</th><th>title</th><th>status</th><th>link</th></tr></thead>
            <tbody>{"".join(source_rows)}</tbody>
          </table>
        </div>
        '''
    body = f'''
    <section class="tool-panel">
      <p><a href="claim-explorer.html">Claim Explorer</a> / topic</p>
      <p class="muted">Matched by topic terms: {html.escape(", ".join(terms))}</p>
      <p><strong>{len(matched_claims)}</strong> claims and <strong>{len(matched_sources)}</strong> sources matched.</p>
    </section>
    <section class="explorer-grid">
      {"".join(claim_cards) if claim_cards else '<p class="muted">No matched claims yet. This topic remains an extraction gap.</p>'}
    </section>
    {source_table}
    '''
    return shell(label, filename, f"Filtered evidence page for {label}.", body, report_name)


def build_claim_explorer(claims: list[dict[str, str]], sources_by_id: dict[str, dict[str, str]], matrices: dict[str, list[dict[str, str]]], report_name: str) -> str:
    cards = []
    for claim in claims:
        claim_id = claim.get("claim_id", "")
        source = sources_by_id.get(claim.get("source_id", ""), {})
        href = source_href(source)
        link_html = f'<a href="{html.escape(href)}">Open source</a>' if href else "<span>No source link recorded</span>"
        hits = matrix_hits(claim, matrices)
        hit_html = "".join(
            f'<span class="matrix-pill">{html.escape(hit["matrix"])} r{html.escape(hit["row"])}: {html.escape(hit["label"])}</span>'
            for hit in hits
        ) or '<span class="muted">No matrix hit auto-detected.</span>'
        search_text = " ".join([claim_id, claim.get("claim", ""), claim.get("source_id", ""), source.get("title", ""), claim.get("confidence", "")])
        cards.append(
            f'''
            <article class="explorer-card" id="claim-{html.escape(claim_id)}" data-search="{html.escape(search_text.lower())}">
              <div class="evidence-topline">
                <strong>{html.escape(claim_id)}</strong>
                <span class="confidence confidence-{html.escape((claim.get("confidence") or "unknown").lower())}">{html.escape(claim.get("confidence") or "unknown")}</span>
              </div>
              <p>{markdown_inline(claim.get("claim", ""))}</p>
              <dl>
                <dt>source_id</dt><dd>{html.escape(claim.get("source_id", ""))}</dd>
                <dt>document</dt><dd>{html.escape(source.get("title", ""))}</dd>
                <dt>page_or_section</dt><dd>{html.escape(claim.get("page_or_section", ""))}</dd>
                <dt>evidence</dt><dd>{html.escape(claim.get("evidence", ""))}</dd>
                <dt>matrix</dt><dd class="matrix-list">{hit_html}</dd>
                <dt>source</dt><dd>{link_html}</dd>
              </dl>
            </article>
            '''
        )
    body = f'''
    <section class="tool-panel">
      <label for="claim-search">Search claims, sources, issuers, regulators, or evidence text</label>
      <input id="claim-search" class="search-input" type="search" placeholder="Try CLAIM_084, USDC, MiCA, redemption, reserve...">
      <p class="muted"><span id="claim-count">{len(claims)}</span> claims shown.</p>
    </section>
    <section class="explorer-grid" id="claim-grid">
      {"".join(cards)}
    </section>
    '''
    return shell("Claim Explorer", "claim-explorer.html", "Search every validated claim and inspect its source trail.", body, report_name)


def build_source_registry(sources: list[dict[str, str]], report_name: str) -> str:
    rows = []
    for source in sources:
        href = source_href(source)
        link_html = f'<a href="{html.escape(href)}">Open</a>' if href else ""
        search_text = " ".join(source.values()).lower()
        rows.append(
            f'''
            <tr data-search="{html.escape(search_text)}">
              <td><code>{html.escape(source.get("id", ""))}</code></td>
              <td>{html.escape(source.get("category", ""))}</td>
              <td>{html.escape(source.get("publisher", ""))}</td>
              <td>{html.escape(source.get("title", ""))}</td>
              <td>{html.escape(source.get("status", ""))}</td>
              <td>{html.escape(source.get("priority", ""))}</td>
              <td>{link_html}</td>
            </tr>
            '''
        )
    body = f'''
    <section class="tool-panel">
      <label for="source-search">Search source registry</label>
      <input id="source-search" class="search-input" type="search" placeholder="Try GENIUS, Circle, BIS, USDPT, failure_case...">
      <p class="muted"><span id="source-count">{len(sources)}</span> sources shown.</p>
    </section>
    <div class="table-wrap registry-table">
      <table>
        <thead>
          <tr><th>source_id</th><th>category</th><th>publisher</th><th>title</th><th>status</th><th>priority</th><th>link</th></tr>
        </thead>
        <tbody id="source-table">
          {"".join(rows)}
        </tbody>
      </table>
    </div>
    '''
    return shell("Source Registry", "source-registry.html", "Source status, publisher, title, priority, and document links.", body, report_name)


def write_assets() -> None:
    css = r'''
:root {
  --bg: #f6f7f4;
  --panel: #ffffff;
  --ink: #17211b;
  --muted: #68736d;
  --line: #dce2dd;
  --green: #1b7654;
  --teal: #126c73;
  --gold: #a36b10;
  --red: #b44735;
  --blue: #315d9b;
  --shadow: 0 14px 34px rgba(23, 33, 27, 0.08);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.55;
}
a { color: var(--teal); text-decoration-thickness: 1px; text-underline-offset: 3px; }
code { background: #edf2ee; border: 1px solid var(--line); border-radius: 4px; padding: 0.08rem 0.24rem; font-size: 0.9em; }
.sidebar {
  position: fixed;
  inset: 0 auto 0 0;
  width: 286px;
  padding: 24px 18px;
  background: #101914;
  color: white;
  overflow-y: auto;
}
.brand {
  display: grid;
  grid-template-columns: 34px 1fr;
  align-items: center;
  gap: 10px;
  color: white;
  text-decoration: none;
  font-weight: 760;
  line-height: 1.18;
  margin-bottom: 24px;
}
.brand-mark {
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.2)),
    linear-gradient(135deg, var(--green), var(--gold));
  display: inline-block;
}
nav { display: grid; gap: 4px; }
nav a {
  color: #d7e2da;
  text-decoration: none;
  padding: 9px 10px;
  border-radius: 7px;
  font-size: 0.94rem;
}
nav a:hover, nav a.active { background: rgba(255,255,255,0.1); color: #fff; }
main {
  margin-left: 286px;
  padding: 30px clamp(20px, 4vw, 56px) 70px;
  max-width: 1440px;
}
.page-header {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
  gap: 28px;
  align-items: stretch;
  margin-bottom: 28px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 24px;
}
.page-header h1 {
  font-size: clamp(2rem, 4vw, 4.2rem);
  margin: 0 0 10px;
  line-height: 1.02;
  letter-spacing: 0;
}
.page-header p { max-width: 850px; color: var(--muted); font-size: 1.04rem; }
.source-note { font-size: 0.92rem; }
.eyebrow {
  color: var(--green);
  font-size: 0.78rem;
  font-weight: 760;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
.evidence-map {
  min-height: 210px;
  border: 1px solid var(--line);
  background:
    radial-gradient(circle at 20% 30%, rgba(27,118,84,0.18), transparent 18%),
    radial-gradient(circle at 74% 22%, rgba(49,93,155,0.16), transparent 16%),
    radial-gradient(circle at 58% 76%, rgba(163,107,16,0.18), transparent 18%),
    linear-gradient(135deg, #ffffff, #eef3f0);
  border-radius: 8px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}
.evidence-map::before,
.evidence-map::after {
  content: "";
  position: absolute;
  inset: 44px 42px;
  border-top: 2px solid rgba(18,108,115,0.28);
  transform: rotate(23deg);
}
.evidence-map::after {
  inset: 84px 34px;
  transform: rotate(-18deg);
  border-color: rgba(163,107,16,0.28);
}
.evidence-map span {
  position: absolute;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--panel);
  border: 3px solid var(--green);
  box-shadow: 0 0 0 5px rgba(27,118,84,0.08);
}
.evidence-map span:nth-child(1) { left: 18%; top: 26%; }
.evidence-map span:nth-child(2) { left: 70%; top: 18%; border-color: var(--blue); }
.evidence-map span:nth-child(3) { left: 52%; top: 70%; border-color: var(--gold); }
.evidence-map span:nth-child(4) { left: 82%; top: 64%; border-color: var(--red); }
.evidence-map span:nth-child(5) { left: 30%; top: 78%; border-color: var(--teal); }
.report-section { margin: 34px 0; }
.topic-strip {
  background: #ffffff;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px 16px;
  margin: 0 0 22px;
  box-shadow: var(--shadow);
}
.topic-strip p { margin: 0 0 9px; }
.topic-strip div {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.topic-strip a {
  display: inline-flex;
  align-items: center;
  min-height: 32px;
  border: 1px solid #cbd7d0;
  border-radius: 6px;
  padding: 4px 9px;
  background: #f7faf8;
  text-decoration: none;
  font-weight: 650;
}
.report-section h2 { font-size: 1.55rem; margin: 34px 0 14px; }
.report-section h3 { font-size: 1.1rem; margin: 26px 0 10px; }
.prose-block,
.evidence-block,
.tool-panel,
.explorer-card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
}
.prose-block { padding: 18px 20px; margin: 14px 0; }
.evidence-block {
  display: grid;
  grid-template-columns: minmax(280px, 0.85fr) minmax(320px, 1.15fr);
  gap: 18px;
  padding: 18px;
  margin: 16px 0;
}
.conclusion p { font-size: 1rem; margin: 8px 0 0; }
.evidence-stack { display: grid; gap: 12px; }
.evidence-card {
  border: 1px solid #d9e4df;
  border-left: 4px solid var(--green);
  border-radius: 7px;
  padding: 13px 14px;
  background: #fbfdfb;
}
.evidence-card.missing { border-left-color: var(--red); }
.evidence-topline {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  margin-bottom: 8px;
}
.claim-chip {
  display: inline-block;
  color: #0f4c4d;
  background: #e7f4ee;
  border: 1px solid #c4e4d6;
  text-decoration: none;
  border-radius: 4px;
  padding: 0 0.24rem;
  font-size: 0.88em;
  white-space: nowrap;
}
.claim-text { color: #26332c; margin: 0 0 10px; }
dl {
  display: grid;
  grid-template-columns: 112px minmax(0, 1fr);
  gap: 6px 12px;
  margin: 0;
  font-size: 0.9rem;
}
dt { color: var(--muted); font-weight: 700; }
dd { margin: 0; min-width: 0; overflow-wrap: anywhere; }
.confidence {
  border-radius: 999px;
  padding: 2px 8px;
  font-size: 0.78rem;
  font-weight: 760;
  text-transform: uppercase;
}
.confidence-high { color: #0e5535; background: #def2e7; }
.confidence-medium { color: #744800; background: #fff1cf; }
.confidence-low { color: #8e2b1d; background: #ffe4dd; }
.confidence-unknown { color: #49524d; background: #edf0ee; }
.matrix-list { display: flex; flex-wrap: wrap; gap: 5px; }
.matrix-pill {
  display: inline-flex;
  border: 1px solid var(--line);
  background: #f3f6f4;
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 0.82rem;
}
.muted { color: var(--muted); }
.tool-panel { padding: 18px 20px; margin-bottom: 18px; }
.tool-panel label { display: block; font-weight: 760; margin-bottom: 8px; }
.search-input {
  width: 100%;
  height: 44px;
  border: 1px solid #cbd7d0;
  border-radius: 7px;
  padding: 0 12px;
  font: inherit;
  background: #fff;
}
.explorer-grid { display: grid; gap: 14px; }
.explorer-card { padding: 16px; }
.table-wrap {
  overflow-x: auto;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
}
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
th, td { border-bottom: 1px solid var(--line); padding: 10px 12px; text-align: left; vertical-align: top; }
th { background: #eef3f0; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; }
tr:last-child td { border-bottom: 0; }
.hidden { display: none !important; }
@media (max-width: 980px) {
  .sidebar { position: static; width: auto; }
  main { margin-left: 0; }
  .page-header { grid-template-columns: 1fr; }
  .evidence-block { grid-template-columns: 1fr; }
  .evidence-map { min-height: 160px; }
}
'''
    js = r'''
function setupCardSearch(inputId, selector, countId) {
  const input = document.getElementById(inputId);
  if (!input) return;
  const items = Array.from(document.querySelectorAll(selector));
  const count = document.getElementById(countId);
  function apply() {
    const q = input.value.trim().toLowerCase();
    let shown = 0;
    for (const item of items) {
      const haystack = item.dataset.search || item.textContent.toLowerCase();
      const match = !q || haystack.includes(q);
      item.classList.toggle("hidden", !match);
      if (match) shown += 1;
    }
    if (count) count.textContent = String(shown);
  }
  input.addEventListener("input", apply);
  apply();
}
setupCardSearch("claim-search", ".explorer-card", "claim-count");
setupCardSearch("source-search", "#source-table tr", "source-count");
'''
    write_text(SITE_ROOT / "assets" / "styles.css", css)
    write_text(SITE_ROOT / "assets" / "portal.js", js)


def main() -> None:
    if SITE_ROOT.exists():
        shutil.rmtree(SITE_ROOT)
    SITE_ROOT.mkdir(parents=True)
    DATA_ROOT.mkdir(parents=True)

    claims = read_csv(CLAIM_TABLE)
    sources = read_csv(SOURCE_REGISTRY)
    matrices = {path.name: read_csv(path) for path in sorted(MATRIX_DIR.glob("*.csv"))}
    claims_by_id = {row["claim_id"]: row for row in claims}
    sources_by_id = {row["id"]: row for row in sources}

    report_path, markdown = load_report()
    sections = extract_sections(markdown)

    write_text(DATA_ROOT / "claims.json", json.dumps(claims, ensure_ascii=False, indent=2))
    write_text(DATA_ROOT / "sources.json", json.dumps(sources, ensure_ascii=False, indent=2))
    write_text(DATA_ROOT / "matrices.json", json.dumps(matrices, ensure_ascii=False, indent=2))

    write_assets()

    for filename, config in PAGE_CONFIG.items():
        body = render_section_content(config["sections"], sections, claims_by_id, sources_by_id, matrices)
        write_text(SITE_ROOT / filename, shell(config["title"], filename, config["description"], body, report_path.name))

    for group_filename, topics in TOPIC_GROUPS.items():
        for label, topic_filename, terms in topics:
            write_text(
                SITE_ROOT / topic_filename,
                build_topic_page(label, topic_filename, terms, claims, sources, sources_by_id, matrices, report_path.name),
            )

    write_text(SITE_ROOT / "claim-explorer.html", build_claim_explorer(claims, sources_by_id, matrices, report_path.name))
    write_text(SITE_ROOT / "source-registry.html", build_source_registry(sources, report_path.name))

    print(f"Built Evidence Portal at {SITE_ROOT}")
    print(f"Report source: {report_path.relative_to(REPO_ROOT)}")
    print(f"Claims: {len(claims)} | Sources: {len(sources)} | Matrices: {len(matrices)}")


if __name__ == "__main__":
    main()
