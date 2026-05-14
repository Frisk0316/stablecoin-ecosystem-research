# Known Deficiencies - Phase 3

This list separates confirmed deficiencies from ordinary next-step research
work. A deficiency means the repository currently cannot support a strong
final-report conclusion in that area.

## Source Availability Deficiencies

1. `NYDFS_001` is URL-only. The original NYDFS guidance has been identified
   and partially extracted, but no local archived copy exists yet.
2. `MICA_004` is URL-only. The official MiCA EUR-Lex source has been
   identified and partially extracted, but no local official text/PDF or HTML
   export exists yet.
3. IMF stablecoin sources are absent from the archive.
4. Federal Reserve stablecoin papers and speeches are absent from the archive.
5. Visa Onchain Analytics export is absent; no adjusted stablecoin payment
   volume dataset has been ingested.
6. DeFiLlama stablecoin supply data is absent; no supply / chain-distribution
   export has been ingested.
7. Cambridge CCAF digital money dashboard data is absent.
8. Artemis stablecoin metrics are absent.
9. Western Union / Anchorage USDPT or UDSPT product documents are absent:
   product page, launch release, whitepaper, reserve report, contract
   addresses, and redemption terms.
10. USDP specific monthly reserve report PDF is absent.

## Evidence Extraction Deficiencies

1. Direct redemption rights are not yet extracted for USDC, USDT, PYUSD, USDG,
   RLUSD, GUSD, FDUSD, USDP, USDe, or DAI/USDS.
2. Freeze, blacklist, pause, and suspension powers are not yet systematically
   extracted from product terms or smart-contract documentation.
3. Tether's full Q1 2026 reserve table is not yet extracted from `USDT_002`;
   current composition claims rely partly on issuer release `USDT_006`.
4. GENIUS Act public-law text has not yet been page-level extracted beyond
   OCC and Treasury implementation materials.
5. MiCA ART rules have not yet been extracted separately from EMT rules.
6. CLARITY Act stablecoin-relevant sections have not yet been isolated.
7. BoE systemic stablecoin consultation is not yet available or extracted.
8. DAI/USDS RWA collateral, PSM, oracle, liquidation, governance, and savings
   mechanisms are not yet claim-table complete.
9. USDe vs sUSDe distinction, custodian exposure, exchange exposure, basis
   risk, and reserve fund mechanics are not yet claim-table complete.

## Final Report Deficiencies

1. The final report has not been rewritten after Phase 2 and Phase 3 evidence
   extraction. It should not be treated as final.
2. Major conclusions about stablecoins as payments infrastructure remain
   under-supported until adjusted on-chain/payment data is ingested.
3. Major conclusions about USDPT / UDSPT remain under-supported until primary
   product documentation is available.
4. Major conclusions about direct holder protections remain under-supported
   until issuer terms and legal redemption policies are extracted.
5. Major conclusions about reserve-market impact remain partial until issuer
   reserve composition is normalized across direct T-bills, repo, MMF shares,
   bank deposits, and non-cash assets.

## Operational Deficiencies

1. `check_missing_sources.py` prints the high-priority external queue but does
   not distinguish "fully missing" from "URL-only registered but not locally
   archived." It should be upgraded before the next research handoff.
2. Some earlier Markdown files contained mojibake; issuer and law digests have
   been rebuilt, but other chapter drafts should still be checked for encoding
   artifacts.
3. Raw source files remain outside Git by design. This is correct for repo
   hygiene, but reproducibility depends on maintaining the external archive.
