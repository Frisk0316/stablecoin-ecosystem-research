# GitHub Repository Specification for Codex

## Objective

Convert the first delivery package into a maintainable GitHub repository for the stablecoin ecosystem research project. The repository should support long-term research, source tracking, claim validation, comparison matrices, chapter drafts, and final report generation.

## Target repository name

`stablecoin-ecosystem-research`

## Core principle

No major conclusion should appear in the final report unless it is traceable to a claim in `03_claim_tables/claim_table_master.csv` and a source in `01_sources/source_registry.csv`.

## Recommended repository tree

```text
stablecoin-ecosystem-research/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── .gitignore
├── .gitattributes
│
├── 00_project_management/
│   ├── research_brief.md
│   ├── research_phase1_status.md
│   └── unresolved_open_questions.md
│
├── 01_sources/
│   ├── source_registry.csv
│   ├── source_manifest.csv
│   ├── duplicate_and_superseded_files.csv
│   ├── external_fetch_queue.csv
│   └── manual_download_needed.csv
│
├── 02_source_digests/
│   ├── issuer_source_digest.md
│   ├── law_source_digest.md
│   ├── central_bank_source_digest.md
│   ├── payment_settlement_source_digest.md
│   ├── market_data_source_digest.md
│   └── failure_case_source_digest.md
│
├── 03_claim_tables/
│   ├── claim_table_schema.md
│   └── claim_table_master.csv
│
├── 04_matrices/
│   ├── issuer_comparison_matrix.csv
│   ├── law_regulation_comparison_matrix.csv
│   ├── central_bank_theme_matrix.csv
│   ├── payment_settlement_matrix.csv
│   └── failure_case_matrix.csv
│
├── 05_chapter_drafts/
│   ├── chapter_01_stablecoins_as_onchain_dollar_system.md
│   ├── chapter_02_issuer_comparison.md
│   ├── chapter_03_reserve_assets_and_money_markets.md
│   ├── chapter_04_law_and_regulation.md
│   ├── chapter_05_central_bank_views.md
│   ├── chapter_06_usdpt_and_cross_border_payments.md
│   ├── chapter_07_onchain_data_and_payment_demand.md
│   ├── chapter_08_failure_cases.md
│   └── chapter_09_conclusion.md
│
├── 06_flow_diagrams/
│   ├── stablecoin_issuance_redemption_flow.md
│   ├── reserve_asset_flow.md
│   ├── correspondent_banking_flow.md
│   ├── western_union_traditional_flow.md
│   ├── usdpt_settlement_flow.md
│   └── tokenized_money_system_flow.md
│
├── 07_final_report/
│   ├── executive_summary.md
│   ├── stablecoin_ecosystem_research_report_v0_1.md
│   └── stablecoin_ecosystem_research_report_v0_1.html
│
├── 08_scripts/
│   ├── validate_claim_table.py
│   ├── check_missing_sources.py
│   └── build_source_registry.py
│
├── 09_data_exports/
│   └── README.md
│
└── archive/
    └── phase1_outputs/
```

## Raw source document policy

Do **not** commit all raw PDFs/HTML files by default.

Recommended approach:

1. Keep raw source archive outside Git, for example in Google Drive, OneDrive, local NAS, or a private archive folder.
2. Track raw files through `01_sources/source_registry.csv` using `local_path`, `source_url`, `sha256_12`, `status`, and `notes`.
3. If raw PDFs must be versioned in Git, use Git LFS and keep the repository private.
4. Do not publish copyrighted PDFs unless licensing allows it.

Suggested `.gitignore`:

```gitignore
# Raw documents
raw_sources/
*.pdf
*.zip
*.docx
*.pptx
*.xlsx

# Python
__pycache__/
*.pyc
.venv/
.env

# OS/editor
.DS_Store
Thumbs.db
.vscode/
```

Suggested `.gitattributes` if using Git LFS privately:

```gitattributes
*.pdf filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
*.docx filter=lfs diff=lfs merge=lfs -text
*.pptx filter=lfs diff=lfs merge=lfs -text
*.xlsx filter=lfs diff=lfs merge=lfs -text
```

## AGENTS.md content

Create an `AGENTS.md` file with this content:

```markdown
# Agent Instructions

This repository is a stablecoin ecosystem research project.

## Non-negotiable research rules

1. Do not add a major conclusion to the final report unless it is backed by `03_claim_tables/claim_table_master.csv`.
2. Every claim must have a `source_id`, `page_or_section`, evidence summary, and confidence level.
3. Do not call an attestation or assurance report an audit unless the source explicitly says audit.
4. Do not describe SWIFT as a funds-settlement system. Treat it as a messaging/network layer unless a source says otherwise.
5. Do not equate raw on-chain transfer volume with real payment volume.
6. Distinguish fiat-backed, crypto/RWA-collateralized, algorithmic, and synthetic-dollar stablecoins.
7. Preserve open questions rather than guessing.
8. If a source is dynamic HTML, record access date or local saved copy.

## Workflow

- Update source registry first.
- Then update source digest.
- Then update claim table.
- Then update comparison matrix.
- Then update chapter drafts.
- Final report should only summarize verified claims.
```

## Codex tasks

### Task 1 — Initialize repo

```bash
git init
mkdir -p 00_project_management 01_sources 02_source_digests 03_claim_tables 04_matrices 05_chapter_drafts 06_flow_diagrams 07_final_report 08_scripts 09_data_exports archive/phase1_outputs
```

Copy all files from `stablecoin_delivery_v0_1/` into the repository root.

### Task 2 — Add validation workflow

Create `.github/workflows/validate.yml`:

```yaml
name: Validate Research Tables
on:
  push:
  pull_request:
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python 08_scripts/validate_claim_table.py
      - run: python 08_scripts/check_missing_sources.py
```

### Task 3 — Create branch workflow

Use these branches:

```text
main        stable release only
dev         integration branch
feature/*   module-specific research branches
```

Recommended feature branches:

```text
feature/issuer-page-level-extraction
feature/law-genius-mica-nydfs
feature/central-bank-imf-fed
feature/payment-usdpt-western-union
feature/onchain-data
feature/failure-cases
```

### Task 4 — Add issue templates

Create `.github/ISSUE_TEMPLATE/source_extraction.md`:

```markdown
---
name: Source extraction
about: Extract claims from a source document
labels: source-extraction, needs-page-citation
---

## Source ID

## File / URL

## Extraction target

- [ ] Source digest
- [ ] Claim table rows
- [ ] Matrix updates
- [ ] Open questions

## Required fields

- Page / section:
- Evidence:
- Confidence:
```

### Task 5 — Add report build script later

Do not build a complex static site yet. For v0.1, keep Markdown and HTML side by side. Later, add a report generation script that combines chapter drafts into `07_final_report/stablecoin_ecosystem_research_report.md`.

## Acceptance criteria

The GitHub repo setup is complete when:

1. `README.md` explains the project and folder structure.
2. `AGENTS.md` exists and contains the research rules.
3. `python 08_scripts/validate_claim_table.py` passes or prints actionable errors.
4. `01_sources/source_registry.csv` exists and has stable `source_id` values.
5. `03_claim_tables/claim_table_master.csv` exists and every row has a source ID and page/section.
6. Raw source PDFs are not accidentally committed unless Git LFS/private repo is intentionally used.
7. GitHub Actions runs validation on push and pull request.

## First Codex prompt

Use this prompt for Codex:

```text
You are working in the stablecoin-ecosystem-research repository. Convert the current delivery package into a clean GitHub research repository. Preserve the folder structure, add README.md, AGENTS.md, .gitignore, .gitattributes, and GitHub Actions validation. Do not rewrite research conclusions. Do not commit raw PDFs unless explicitly instructed. Keep source IDs stable. Make sure validate_claim_table.py runs successfully or reports actionable issues.
```
