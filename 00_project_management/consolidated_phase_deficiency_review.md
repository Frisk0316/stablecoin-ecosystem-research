# Stablecoin Research Consolidated Deficiency Review

Last updated: 2026-05-14 (v0.2 interim close)

Purpose: this document consolidates the explicit deficiencies, unresolved
questions, and phase-level gaps. The v0.2 interim pass closed Paxos-family
direct redemption, GUSD platform-versus-lawful-holder distinction, USDP
monthly reserve report status, GENIUS Act statutory anchors, and the
issuer-matrix data-quality regressions left over from earlier mojibake
recovery. USDPT product/workflow gaps and adjusted-volume market-data gaps
are now deliberately deferred to v0.3 per user scope decision.

Next-agent handoff: see `00_project_management/claude_code_handoff.md` for
the Claude Code v0.3 task list, validation commands, and research
guardrails. See `CHANGELOG.md` for the v0.2 delta and
`00_project_management/unresolved_open_questions.md` for the live v0.3
backlog.

## How to Read This Review

Status labels:

- `missing`: source or evidence is not currently available in the local
  archive or claim table.
- `url_only`: an official URL has been identified and registered, but no local
  archived copy exists yet.
- `archived`: a local copy exists, but claim-level extraction may still be
  incomplete.
- `partial`: some claim-table evidence exists, but extraction is not complete
  enough for a strong final-report conclusion.
- `operational`: workflow, validation, encoding, or reproducibility issue.

Priority labels:

- `high`: blocks major final-report conclusions.
- `medium`: important for completeness, but not always blocking.
- `low`: cleanup or later refinement.

## Executive Summary

The repository has completed initial source intake, issuer evidence extraction,
and a first law/regulation extraction pass. The strongest current artifacts are:

- `03_claim_tables/claim_table_master.csv`
- `04_matrices/issuer_comparison_matrix.csv`
- `04_matrices/law_regulation_comparison_matrix.csv`
- `02_source_digests/issuer_source_digest.md`
- `02_source_digests/law_source_digest.md`

2026-05-14 follow-up: the new deficiency download package has been registered
in `01_sources/source_registry.csv`, and selected high-priority items have been
propagated into `CLAIM_044` to `CLAIM_057`, central-bank/payment/issuer/law
matrices, and the working digests. This review now distinguishes three
different states: source missing, source locally archived but not fully
extracted, and claim-table supported.

Next-phase issuer/legal follow-up has added `CLAIM_058` to `CLAIM_071`,
covering direct redemption and eligibility terms for USDC, USDT, FDUSD, USDe,
and USDG, plus MiCA ART reserve/redemption/no-interest provisions.

The project should still not treat the final report as complete. The main
blocking gaps are now:

1. Market/on-chain data has been partially ingested, but adjusted exports and
   methodology reconciliation remain under-supported.
2. USDPT / UDSPT launch evidence is partially supported, but product terms,
   reserve reports, contract addresses, and end-to-end workflow documents are
   still missing.
3. Direct holder redemption rights and suspension/freeze powers are now partly
   extracted for USDC, USDT, Paxos/USDG, RLUSD, FDUSD, and USDe, but GUSD,
   USDP, PYUSD-specific Paxos flow, DAI/USDS, and USDPT remain incomplete.
4. IMF and Federal Reserve sources are now locally registered and partially
   extracted, but need page-level extraction and Taiwan-specific synthesis.
5. Several key legal sources are now locally archived, but GENIUS, CLARITY,
   BoE, ESMA, MiCA significant-token rules, and MiCA recovery/redemption-plan
   details remain incomplete.

## Phase 1 Deficiencies

Source file:

- `00_project_management/research_phase1_status.md`

Phase 1 completed the first intake and created the initial source registry,
issuer matrix, claim table, issuer digest, and open-question list. The
remaining Phase 1 gaps are mostly handoff items into later phases.

| Deficiency | Status | Priority | Notes |
| --- | --- | --- | --- |
| Issuer redemption rights and reserve composition were not yet extracted at page level. | partial | high | Phase 2 started this, but direct redemption rights remain incomplete. |
| Law matrix for GENIUS, CLARITY, MiCA, BoE, and NYDFS was not yet complete. | partial | high | Phase 3 added NYDFS and MiCA EMT claims, but GENIUS, CLARITY, BoE, ART, and ESMA remain incomplete. |
| Central-bank theme matrix lacked IMF and Fed sources. | partial | high | IMF and Fed source sets are now registered and partially extracted into `CLAIM_044` to `CLAIM_050`; page-level extraction remains. |
| USDPT settlement analysis lacked primary product evidence. | partial | high | Launch/product and infrastructure evidence now support `CLAIM_051` to `CLAIM_053`; terms, reserve report, contract addresses, and redemption terms remain absent. |
| External fetch queue remained unresolved. | partial | high | New deficiency downloads reduced the queue, but adjusted datasets and manual-needed items remain. |

## Phase 2 Deficiencies

Source files:

- `00_project_management/research_phase2_status.md`
- `00_project_management/unresolved_open_questions.md`
- `02_source_digests/issuer_source_digest.md`
- `05_chapter_drafts/chapter_02_issuer_comparison.md`
- `05_chapter_drafts/chapter_03_reserve_assets_and_money_markets.md`

Phase 2 strengthened issuer evidence and added `CLAIM_026` to `CLAIM_035`.
However, it left several high-impact issuer questions unresolved.

| Deficiency | Status | Priority | Notes |
| --- | --- | --- | --- |
| Direct redemption rights are not systematically extracted for USDC, USDT, PYUSD, USDG, RLUSD, GUSD, FDUSD, USDP, USDe, or DAI/USDS. | partial | high | USDC, USDT, USDG EU route, FDUSD, and USDe direct redemption eligibility now have claims (`CLAIM_058`, `CLAIM_060`, `CLAIM_062`, `CLAIM_065`, `CLAIM_068`); PYUSD/USDP/GUSD/DAI remain incomplete. |
| Freeze, blacklist, pause, suspension, and wallet/network restriction powers are not systematically extracted. | partial | high | Paxos, Ripple, and FDUSD/FD121 restriction claims have been added (`CLAIM_056`, `CLAIM_057`, `CLAIM_063`, `CLAIM_064`), but issuer-wide extraction remains incomplete. |
| Tether full Q1 2026 reserve table from `USDT_002` is not fully extracted. | partial | high | Current composition claims rely partly on `USDT_006`, an issuer release. |
| `USDT_006` is URL-only. | archived | medium | Official Tether URL is registered and a local HTML copy now exists in the deficiency download package. |
| Paxos direct redemption rights for PYUSD remain unresolved. | missing | high | PayPal platform eligibility evidence does not settle Paxos redemption terms. |
| USDP monthly reserve report PDF is absent. | missing | medium | Product/transparency pages exist, but a concrete report PDF is still needed. |
| USDG terms are missing. | missing | medium | Needed for direct redeemer scope, suspension conditions, and wallet/network limits. |
| RLUSD user terms are missing. | partial | high | Ripple user terms now support `CLAIM_057`; direct redeemer eligibility and contract-level controls remain unresolved. |
| GUSD/Gemini terms require further extraction. | partial | high | Product page supports Gemini-customer redemption; broader lawful-holder rights require NYDFS/Gemini terms analysis. |
| FDUSD terms are missing. | archived | medium | Terms are now archived but still need claim-level extraction for eligible redeemers, suspension mechanics, and issuer/custody structure. |
| DAI/USDS extraction is not claim-table complete. | partial | medium | RWA collateral, PSM, savings/yield mechanics, governance, oracle, and liquidation mechanics remain incomplete. |
| USDe extraction is not claim-table complete. | partial | medium | USDe vs sUSDe, custodian exposure, exchange exposure, basis risk, and reserve fund mechanics remain incomplete. |

## Phase 3 Deficiencies

Source files:

- `00_project_management/research_phase3_status.md`
- `00_project_management/known_deficiencies_phase3.md`
- `02_source_digests/law_source_digest.md`
- `05_chapter_drafts/chapter_04_law_and_regulation.md`

Phase 3 added `NYDFS_001`, `MICA_004`, and `CLAIM_036` to `CLAIM_043`.
Regulatory evidence is stronger, but the law chapter still has several
source and extraction gaps.

| Deficiency | Status | Priority | Notes |
| --- | --- | --- | --- |
| `NYDFS_001` is URL-only. | archived | high | The official NYDFS guidance URL is registered, partially extracted, and locally archived as HTML. |
| `MICA_004` is URL-only. | archived | high | Official EUR-Lex HTML fetch hit a challenge page, but an official PDF is locally archived and partially extracted. |
| GENIUS Act public-law text has not been page-level extracted beyond OCC/Treasury implementation materials. | partial | high | Need to separate statutory text from proposed rules and implementation guidance. |
| MiCA ART rules have not been separately extracted from EMT rules. | partial | medium | ART reserve, redemption, and no-interest rules are now extracted (`CLAIM_069` to `CLAIM_071`); significant-token and recovery/redemption-plan details remain. |
| CLARITY Act stablecoin-relevant sections have not been isolated. | partial | medium | Avoid overstating stablecoin conclusions from market-structure provisions. |
| BoE systemic stablecoin consultation is missing. | archived | medium | BoE systemic stablecoin regime materials are now registered; page-level extraction remains. |
| ESMA MiCA overview / CASP guidance is missing. | archived | medium | ESMA materials are now registered; CASP and market-infrastructure extraction remains. |

## Source Availability Deficiencies

Source files:

- `01_sources/external_fetch_queue.csv`
- `01_sources/manual_download_needed.csv`
- `01_sources/source_registry.csv`

| Source / Dataset | Status | Priority | Review Note |
| --- | --- | --- | --- |
| NYDFS stablecoin guidance | archived | high | Registered as `NYDFS_001`; local HTML copy now exists. |
| MiCA Regulation (EU) 2023/1114 official text | archived | high | Registered as `MICA_004`; official PDF now exists locally, direct HTML remains challenge-blocked. |
| Tether Q1 2026 issuer release | archived | medium | Registered as `USDT_006`; local HTML copy now exists. |
| IMF stablecoin papers | partial | high | Registered and partially extracted into `CLAIM_049` and `CLAIM_050`; further page extraction needed. |
| Federal Reserve stablecoin papers/speeches | partial | high | Registered and partially extracted into `CLAIM_044` to `CLAIM_048`; further page extraction needed. |
| Visa Onchain Analytics stablecoin export | partial | high | Dashboard shell archived; reproducible adjusted export still needed. |
| DeFiLlama stablecoin supply data | archived | high | API snapshots archived; useful for supply, not adjusted payment-volume evidence by itself. |
| Cambridge CCAF digital money dashboard data | archived | medium | Dashboard/about pages archived; extraction pending. |
| Artemis stablecoin metrics | partial | medium | Report/docs archived and `CLAIM_054` added; data export/methodology reconciliation pending. |
| Western Union / Anchorage USDPT or UDSPT documents | partial | high | Launch and infrastructure evidence supports `CLAIM_051` to `CLAIM_053`; terms/reserve/contract/workflow documents missing. |
| USDP monthly reserve report PDF | missing | medium | Needed for Pax Dollar reserve-composition evidence. |
| BoE systemic stablecoin consultation | missing | medium | Needed for UK systemic stablecoin analysis. |
| ESMA MiCA overview / CASP guidance | missing | medium | Needed for EU CASP and market-infrastructure context. |

Important note: `external_fetch_queue.csv` and `manual_download_needed.csv`
are now partly stale. NYDFS, MiCA, Tether, Fed, IMF, BoE, ESMA, DeFiLlama,
Cambridge, Artemis, and USDPT/WU materials have moved forward, but several
items remain deficient because they need exports, terms, page-level extraction,
or manual download.

## Market Data and Payment-Demand Deficiencies

Source files:

- `02_source_digests/market_data_source_digest.md`
- `02_source_digests/payment_settlement_source_digest.md`
- `05_chapter_drafts/chapter_06_usdpt_and_cross_border_payments.md`
- `05_chapter_drafts/chapter_07_onchain_data_and_payment_demand.md`

| Deficiency | Status | Priority | Notes |
| --- | --- | --- | --- |
| Adjusted stablecoin payment-volume data is not ingested. | partial | high | Sources are registered, but the final report must not equate raw on-chain transfer volume with real payment volume. |
| Visa Onchain Analytics export is missing. | partial | high | Dashboard shell archived; adjusted-volume export/methodology still needed. |
| DeFiLlama supply and chain-distribution data is missing. | archived | high | API snapshots are archived for supply context, but not payment demand. |
| Cambridge and Artemis datasets are missing. | partial | medium | Cambridge pages and Artemis docs are archived; reproducible exports remain incomplete. |
| USDPT / UDSPT workflow is not documented from primary sources. | partial | high | Product/launch and infrastructure evidence exists, but do not infer Western Union agent cash-out, SWIFT replacement, or correspondent-banking displacement without workflow documents. |

## Final Report Deficiencies

Source files:

- `07_final_report/stablecoin_ecosystem_research_report_v0_1.md`
- `07_final_report/executive_summary.md`
- `00_project_management/known_deficiencies_phase3.md`

| Deficiency | Status | Priority | Notes |
| --- | --- | --- | --- |
| Final report has not been rewritten after Phase 2 and Phase 3 evidence extraction. | partial | high | Treat current final-report files as pre-update drafts. |
| Payment-infrastructure conclusions remain under-supported. | partial | high | Requires adjusted on-chain/payment datasets. |
| USDPT / UDSPT conclusions remain under-supported. | missing | high | Requires primary product documentation. |
| Direct holder-protection conclusions remain under-supported. | partial | high | Requires issuer terms and legal redemption policies. |
| Reserve-market impact conclusions remain partial. | partial | medium | Requires normalized reserve composition across T-bills, repo, MMF shares, deposits, and non-cash assets. |

## Operational Deficiencies

Source file:

- `00_project_management/known_deficiencies_phase3.md`

| Deficiency | Status | Priority | Notes |
| --- | --- | --- | --- |
| `check_missing_sources.py` does not distinguish fully missing sources from URL-only registered sources. | operational | medium | Being upgraded in the deficiency follow-up to report archived, manual-needed, URL-only, and missing-local-file states. |
| Some earlier Markdown files may contain mojibake. | operational | medium | Issuer and law digests have been rebuilt; other chapter drafts should still be checked. |
| Raw source files remain outside Git by design. | operational | low | Correct for repo hygiene, but reproducibility depends on maintaining the external archive. |

## Recommended Next Phase

The next phase should prioritize evidence that blocks multiple chapters:

1. Upgrade `check_missing_sources.py` to report source-registry states and
   stale queue items.
2. Continue issuer terms extraction for direct redemption, eligible redeemers,
   suspension, freeze, blacklist, and pause powers, focusing next on GUSD,
   USDP/PYUSD-specific Paxos flows, DAI/USDS, and USDPT.
3. Ingest adjusted market/on-chain exports, especially Visa adjusted-volume
   data and comparable Artemis/Cambridge methodology notes.
4. Complete page-level IMF and Federal Reserve extraction and Taiwan-specific
   synthesis.
5. Fetch remaining USDPT / UDSPT product terms, reserve reports, contract
   addresses, and workflow documents before making settlement-displacement
   claims.
6. Complete GENIUS, CLARITY, BoE, ESMA, MiCA significant-token, and
   recovery/redemption-plan extraction.

## File Map for Review

Primary deficiency files:

- `00_project_management/known_deficiencies_phase3.md`
- `00_project_management/unresolved_open_questions.md`
- `00_project_management/research_phase1_status.md`
- `00_project_management/research_phase2_status.md`
- `00_project_management/research_phase3_status.md`

Source queue and registry files:

- `01_sources/external_fetch_queue.csv`
- `01_sources/manual_download_needed.csv`
- `01_sources/source_registry.csv`

Digest files with explicit open points:

- `02_source_digests/issuer_source_digest.md`
- `02_source_digests/law_source_digest.md`
- `02_source_digests/central_bank_source_digest.md`
- `02_source_digests/payment_settlement_source_digest.md`
- `02_source_digests/market_data_source_digest.md`

Chapter drafts with explicit open points:

- `05_chapter_drafts/chapter_02_issuer_comparison.md`
- `05_chapter_drafts/chapter_03_reserve_assets_and_money_markets.md`
- `05_chapter_drafts/chapter_04_law_and_regulation.md`
- `05_chapter_drafts/chapter_06_usdpt_and_cross_border_payments.md`
- `05_chapter_drafts/chapter_07_onchain_data_and_payment_demand.md`

Archive-only historical references:

- `archive/phase1_outputs/research_phase1_status.md`
- `archive/phase1_outputs/issuer_open_questions.md`
- `archive/phase1_outputs/issuer_source_digest_draft.md`
