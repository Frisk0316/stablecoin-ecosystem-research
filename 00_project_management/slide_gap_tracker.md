# Slide Gap Tracker

Last updated: 2026-06-10

Purpose: delivery-facing tracker for the 2026-06-27 reading-group deck. This
file turns unresolved research gaps into slide-level decisions so the deck can
ship without letting open-ended searches block the whole project.

Primary sources of truth:

- `00_project_management/unresolved_open_questions.md`
- `00_project_management/usdpt_product_terms_research_queue.md`
- `03_claim_tables/claim_table_master.csv`
- `01_sources/source_registry.csv`
- `07_final_report/slide_script_v0_3.md`
- `07_final_report/slide_outline_v0_3.md`

## Working Rule

When a slide needs evidence that is not yet in the claim table, choose one of
four actions:

1. Add source and claim if a primary or acceptable source is found.
2. Keep the slide but use safe conditional wording.
3. Move the point to unresolved questions or appendix.
4. Remove or downgrade the claim.

Do not leave a slide in an ambiguous "needs more research" state. A missing
public document is itself a finding if the deck clearly says what cannot yet be
claimed.

## Search Timebox

For each missing evidence item:

| Step | Limit | Stop condition |
| --- | ---: | --- |
| Official / primary source search | 20 minutes | Source found, or official source not found |
| Credible secondary / data-provider search | 10 minutes | Source found, paywalled, unavailable, or low-quality |
| Local archive / registry check | 10 minutes | Existing source mapped, or marked as not archived |

If the timebox expires, update the row status as `Blocked - source unavailable`,
`Manual needed`, `Paywalled / licensed`, or `Safe wording only`. Do not keep
searching inside the slide-building pass.

## Priority Legend

| Priority | Meaning | Delivery handling |
| --- | --- | --- |
| P0 | Blocks or materially changes a main deck conclusion | Must resolve, downgrade, or state as open in the slide |
| P1 | Strengthens quality but current cautious wording is defensible | Keep cautious wording; improve if source appears |
| P2 | Issuer-specific or appendix depth | Do not block deck unless used as a headline claim |
| P3 | Operational hygiene | Handle after content is stable |

## Deck-Level Gaps

| Item | Priority | Status | Current handling | Next action |
| --- | --- | --- | --- | --- |
| v0.3 PDF is older than v0.4 evidence base | P0 | Resolved | v0.4 deck exported to `07_final_report/穩定幣研究 — 讀書會投影片 v0.4.pdf` (2026-06-10) from the synced `slide_script_v0_3.md`. Treat the older `stablecoin_deficiency_sources_package/穩定幣研究 — 讀書會投影片 v0.3.pdf` as superseded. | Re-export via `07_final_report/build_slides_pdf.py` if slide wording changes again. |
| Post-`CLAIM_154` validation rerun | P3 | Resolved | Full Python validation rerun 2026-06-10 passes at `OK: 157 claims validated` (v0.4.1 added `CLAIM_155`-`CLAIM_157`); portal rebuilt at Claims 157 / Sources 150 / Matrices 6. | None; rerun again only if claims/sources change. |
| Evidence portal sync after future claim/source changes | P3 | Standing rule | Any claim/source change must be followed by portal rebuild. | Run `10_evidence_portal/scripts/build_portal.py` after changes. |

## P0 Slide Gaps

| Slide(s) | Topic | Gap | Current evidence | Delivery action | Safe wording / guardrail | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 37-40 | USDPT product layer and workflow | Missing USDPT-specific user terms, fee schedule, reserve attestation, exact token controls, eligible direct redeemer scope, agent balance-sheet treatment, and end-to-end customer/agent/bank workflow. | `CLAIM_051-053`, `CLAIM_132-134`, `CLAIM_140-143`, `CLAIM_150-151`, `CLAIM_155` (Bybit first live exchange); USDPT queue. | Keep slides, but make Slide 39 the explicit limitation slide. Do not upgrade claims unless new `USDPT_###` or `ANCHORAGE_###` sources are registered. | Western Union / Anchorage evidence supports a regulated digital-asset settlement-layer attempt, Solana address, broad reserve categories, planned select-market features, and ADB Client / Non-Client boundaries. It does not prove SWIFT/correspondent/Fedwire/CHIPS replacement, universal holder redemption, exact mint/burn/freeze controls, or agent balance-sheet treatment. | Safe wording only |
| 41-43 | Adjusted stablecoin payment volume | Missing reproducible Visa Onchain Analytics, Artemis adjusted-volume, Cambridge Digital Money Dashboard numerical export, and McKinsey/Artemis archive. | `CLAIM_054`, `CLAIM_055`, `CLAIM_147`, `CLAIM_157` (Visa/Allium ~2.65T→265B); DeFiLlama supply exports; World Bank remittance benchmark. | Keep Slide 43 as missing-data slide. Use supply, remittance-cost benchmark, and the Visa/Allium ~10x adjustment figure only as context. | Raw on-chain transfer volume and supply are not payment demand. The Visa/Allium figure is a published provider order-of-magnitude illustration, not a reproducible export; the project still cannot estimate realised stablecoin payment volume without adjusted exports and methodology reconciliation. | Safe wording only |
| 36 | Taiwan enacted law and sub-rules | Missing enacted VASP Act text, final Legislative Yuan committee/gazette text, FSC sub-rules, CBC/FSC reserve rules, issuer qualifications, redemption timing, disclosure templates, audit cadence, and offshore USD-stablecoin treatment. | `CLAIM_112-118`, `CLAIM_138-139`, `CLAIM_144-146`. | Keep Taiwan slide framed as policy plus legislative-stage update. Do not state enacted-law conclusions. | Taiwan evidence is legislative-stage only through Executive Yuan approval/submission on 2026-04-02 and committee-stage records/news through 2026-06-03. Statutory conclusions wait for enacted text or official FSC/CBC sub-rules. | Safe wording only |

## P1 Slide Gaps

| Slide(s) | Topic | Gap | Current evidence | Delivery action | Safe wording / guardrail | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 44-45 | Failure-case depeg timelines | Missing exact depeg duration, tick-level trough/recovery, liquidity path, provider methodology comparison, and usable Iron Finance IRON/TITAN non-zero price series. | `CLAIM_107-111`, `CLAIM_135-137`, `CLAIM_148-149`, `CLAIM_156` (Iron Finance issuer timeline); CryptoCompare public hourly proxy for USDC/SVB, Terra USTC, and Maker DAI. | Keep public hourly proxy as coarse context. Iron Finance now has the issuer post-mortem timeline; keep exact tick-level claims outside the main deck unless higher-quality data is acquired. | Failure cases support qualitative risk channels and coarse hourly context for selected cases, not exact tick-level metrics. Iron Finance now has an issuer-narrative timeline (`CLAIM_156`) but independent tick-level OHLCV remains unresolved. | Safe wording only |
| 44-45 | Maker / DAI Black Thursday | Missing Maker Foundation / official governance post-mortem and official final event consequence source. | `CLAIM_098-102`, `CLAIM_135-137` from community / analyst sources. | Keep as medium-confidence case study; do not call it primary-official. | Black Thursday is claim-backed via Whiterabbit and Glassnode; a Maker Foundation or official governance source would upgrade confidence. | Improve if source appears |
| 33-36 | Central-bank / international-body extraction depth | Need more granular page-level extraction for IMF/Fed/BIS/ECB/FSB capital-flow, safe-asset, monetary-policy, bank-credit, and dollarisation channels. | `CLAIM_044-050`, `CLAIM_112-118`. | Keep current conditional framing. Deeper extraction is appendix-quality unless it changes a main conclusion. | Central-bank sources support conditional framing, not a universal central-bank consensus or quantitative effect estimate beyond cited claims. | Improve if time allows |

## P2 Issuer-Specific Gaps

| Slide(s) | Issuer / topic | Gap | Delivery action | Guardrail |
| --- | --- | --- | --- | --- |
| 7, 16-18 | USDC | Circle Mint eligibility, region-specific limits, deeper Reserve Fund component weights, chain-specific contract controls. | Keep current Circle Mint gating and risk-factor control framing. | Do not claim any holder can redeem directly with Circle or state component weights not extracted from primary sources. |
| 8, 17-19 | USDT | Maturity ladder, custodian/counterparty split, collateral details, redemption fee/minimum/timing, bank-transfer mechanics, smart-contract controls, USDT/USAT separation. | Keep verified-customer redemption and Q1 2026 reserve-table framing. | Do not describe USDT as pure cash equivalent or claim universal direct redemption. |
| 9-10, 16 | PYUSD / USDP / USDG | PayPal retail-to-Paxos redemption mapping, USDG non-EU workflow, USDG-specific reserve report. | Keep Paxos Customer-only direct redemption framing. | Do not imply PayPal retail users automatically have Paxos direct redemption rights. |
| 12 | RLUSD | Direct redeemer eligibility, smart-contract controls, distributor / Standard Custody relationship. | Keep reserve/custody stronger than redemption-evidence framing. | Do not claim any RLUSD holder can redeem directly or that freeze controls exist without source-backed extraction. |
| 11, 30 | GUSD | Smart-contract controls, NYDFS lawful-holder interaction with Gemini customer-only pathway, reserve-interest claim if used. | Keep Gemini Customer pathway framing. | Do not say NYDFS lawful-holder guidance automatically overrides Gemini platform terms. |
| 13 | FDUSD | FD121/BVI/HK trust or custody relationship, chain-specific obligations, smart-contract controls. | Keep FD121 Account gating and U.S. person exclusion. | Do not claim U.S. individuals are eligible or expand trust/custody structure beyond extracted language. |
| 14, 20, 44 | DAI / USDS | RWA Vault inventory, PSM mechanics, DAI/USDS/sUSDS/stUSDS/SKY contract relationship, governance-vote history. | Keep protocol-collateralised distinction. | Do not treat DAI/USDS as fiat-backed like USDC/Paxos/GUSD or call yield guaranteed. |
| 15, 20, 44 | USDe | Exchange exposure, funding/basis stress, sUSDe APY sustainability, unwind mechanics, current Reserve Fund changes. | Keep synthetic-dollar and risk-mitigation framing. | Do not call USDe fiat-backed, risk-free, or say OES eliminates exchange risk. |
| 37-40 | USDPT issuer comparison | Reserve trust, USDPT reserve report, attestation cadence, token metadata, direct redemption, freeze/sanctions controls, holder yield. | Covered by P0 USDPT row; update issuer matrix only when sources exist. | Do not compare USDPT issuer terms to USDC/USDT/Paxos/GUSD/FDUSD/RLUSD as if parity is established. |
| 22-32 | Foreign-issuer equivalence | Future Treasury/OCC/Federal Register comparability or reciprocal-arrangement determinations. | Keep as screened, not adjudicated. | Do not say BoE or MiCA is officially equivalent to GENIUS. |

## P3 Operational Gaps

| Item | Gap | Delivery action | Status |
| --- | --- | --- | --- |
| Manual / URL-only rows | `MCKINSEY_ARTEMIS_001` is `manual_needed`; `FAILURE_001-005`, `FAILURE_007-008`, `USDPT_010`, `USDPT_011`, and `TAIWAN_VASP_001-005` are `url_only`. `FAILURE_006`, `USDPT_012`, `VISA_ALLIUM_001` archived to local HTML 2026-06-11. | Archive remaining local copies if obtained; update `source_registry.csv` and rerun missing-source checks. | Partially archived |
| Fresh deck export | v0.4 PDF now exported: `07_final_report/穩定幣研究 — 讀書會投影片 v0.4.pdf` (63 pages, generated 2026-06-10 by headless Edge). | Reproducible workflow committed at `07_final_report/build_slides_pdf.py`; rerun after any slide-script change. PPT export still optional if an editable deck is needed. | Resolved (PDF); PPT optional |
| Historical deficiency files | Older phase files contain superseded gaps. | Use this tracker plus `unresolved_open_questions.md` as live backlog. | Controlled |

## Pre-Export Checklist

Before making the final PDF/PPT:

- Confirm every P0 row is either resolved or explicitly framed as open in the
  relevant slide.
- Confirm no slide says USDPT replaces SWIFT, correspondent banking, Fedwire,
  or CHIPS.
- Confirm no slide equates raw transfer volume or supply with payment demand.
- Confirm Taiwan wording says legislative-stage unless enacted text is
  registered and extracted.
- Confirm failure-case charts or metrics are labelled as coarse hourly proxy
  unless better data is added.
- Rerun validation and portal scripts if claims, sources, matrices, or report
  text changed.

## Closing Protocol

To close a row:

1. Register the source in `01_sources/source_registry.csv`.
2. Add or update claim rows in `03_claim_tables/claim_table_master.csv`.
3. Update the relevant digest, matrix, chapter, slide, and evidence portal.
4. Change this tracker row from `Open`, `Safe wording only`, or
   `Improve if source appears` to `Closed`, with the closing claim IDs.

