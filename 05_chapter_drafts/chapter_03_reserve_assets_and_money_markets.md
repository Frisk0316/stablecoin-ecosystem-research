# Chapter 3 - Reserve Assets and Dollar Money Markets

Working thesis: stablecoin growth can affect short-term safe-asset markets
because issuers hold cash, bank deposits, Treasury bills, repo/reverse repo,
and money market fund exposures. The claim table is the control layer for
which issuer-level reserve statements can be used in the final report.

## Evidence added in Phase 2

USDC reserve evidence now includes bank deposits, deposits at systemically
important institutions, overnight reverse Treasury repo, sub-3-month
Treasuries, and the Circle Reserve Fund (`CLAIM_026`, `CLAIM_027`). This
supports the view that USDC is materially linked to bank liquidity, Treasury
bills, repo, and government money market fund infrastructure.

USDT evidence now distinguishes assurance scope from reserve composition. The
Q1 2026 reserve report supports point-in-time assurance and reserve surplus
claims (`CLAIM_002`, `CLAIM_003`). Tether's May 1, 2026 official release adds
medium-confidence composition claims: about US$141bn of direct and indirect
U.S. Treasury bill exposure, about US$20bn of physical gold, and about US$7bn
of Bitcoin (`CLAIM_028`, `CLAIM_029`). This means USDT should not be modeled
as a pure Treasury-bill cash substitute; the reserve-backed category includes
non-cash and non-Treasury exposures.

GUSD reserve evidence now identifies deposits at FDIC-insured banks, money
market funds invested only in U.S. Treasury obligations, and U.S. Treasury
obligations (`CLAIM_034`). RLUSD product-page evidence identifies U.S. dollar
deposits, U.S. Treasuries, cash equivalents, segregated accounts, and BNY
primary custody (`CLAIM_032`, `CLAIM_033`).

Next-phase terms extraction adds two reserve-income guardrails. Circle terms
state that USDC holders are not entitled to reserve interest/returns and that
USDC itself does not generate holder yield (`CLAIM_059`). Ethena terms make a
similar no-holder-yield point for USDe, but in a different product category:
USDe is a synthetic-dollar asset, only whitelisted Mint Users can redeem
directly with Ethena BVI, and USDe must be separated from sUSDe/staking yield
(`CLAIM_065`, `CLAIM_066`, `CLAIM_067`).

MiCA extraction adds a legal reserve comparator. For ARTs, Article 36 requires
the reserve of assets to address redemption-liquidity risk, be legally and
operationally segregated, and be at least equal to aggregate holder claims
(`CLAIM_069`). Article 39 then ties that reserve structure to a permanent
holder redemption right (`CLAIM_070`), while Article 40 prohibits
holding-time-linked interest or equivalent benefits (`CLAIM_071`).

Paxos terms now anchor a unified reserve-composition rule for the
Paxos-issued USD Stablecoins (USDP, PYUSD, USDG): reserves are restricted
to FDIC-insured fiat deposits, U.S. government-guaranteed debt instruments
(direct or repo), and money-market funds composed of such instruments,
under Paxos Trust / Paxos Digital / PIE-specific cash management
programmes (`CLAIM_075`). GUSD reserves are held across three account
categories: FDIC-insured bank omnibus accounts, money-market accounts
holding MMFs invested in U.S. government securities, and Treasury accounts
holding U.S. Treasury Obligations, managed to a 1:1 ratio (`CLAIM_078`).

GENIUS Act Sec. 4(1)(A) now provides the statutory baseline for U.S.
permitted payment stablecoin reserves: U.S. coins/currency or Fed-account
balances, demand deposits at insured depository institutions, Treasury
bills/notes/bonds with remaining or original maturity of 93 days or less,
overnight repos backed by such Treasuries, overnight reverse repos
collateralised by such Treasuries with overcollateralisation, registered
MMFs invested solely in those underlying assets, and similar liquid
government-issued assets approved by the primary regulator (`CLAIM_084`).
Sec. 4(11) prohibits permitted and foreign payment stablecoin issuers
from paying holders any form of interest or yield solely in connection
with holding, use, or retention (`CLAIM_086`).

BoE's 2025 systemic stablecoin consultation provides a contrasting UK
reserve rule: at least 40% of backing assets must be held as unremunerated
central bank deposits at the Bank of England, up to 60% may be held in
short-term sterling-denominated UK government debt securities, and a
step-up regime allows systemic-at-launch issuers to hold up to 95% UK
government debt securities as they scale (`CLAIM_090`). This is the
strictest reserve-composition rule among GENIUS, MiCA, and BoE, and is
the only one to mandate a central-bank-deposit floor.

Crypto/RWA-collateralised stablecoins must not be modelled as participating
in the same dollar money-market channel as fiat-backed stablecoins. The
MakerDAO MCD Protocol generates Dai/USDS through overcollateralisation by
governance-approved collateral deposited into Maker Vaults; reserves are
not held in T-bills, MMF shares, or bank deposits except where specific
RWA Vaults are governance-approved (`CLAIM_098`). Synthetic-dollar
stablecoins like USDe operate at 1:1 collateralisation via short
perpetual hedges with off-exchange custody of backing assets and a
stablecoin-plus-ETH Reserve Fund (`CLAIM_103`, `CLAIM_104`, `CLAIM_106`).
Neither category should be aggregated with fiat-backed issuer reserves
when estimating stablecoin-driven T-bill demand.

## Core sources

- BIS WP 1270 on stablecoins and safe-asset prices.
- ECB WP 3174 on the global safe-asset channel.
- Issuer reserve reports, attestations, transparency pages, and product terms.

## Open questions

- Which issuers hold direct T-bills versus MMF shares versus repo exposure?
- How much reserve liquidity is held in uninsured bank deposits?
- How quickly could redemptions force asset liquidation?
- Can Tether's Q1 2026 full reserve table be extracted from `USDT_002` to
  reconcile issuer-release composition figures?
- Which product terms define the legally enforceable direct redemption right,
  and how do they differ from broad issuer transparency statements?
- How should reserve-income capture by issuers be compared with explicit
  no-interest/no-yield rules in issuer terms and MiCA?
