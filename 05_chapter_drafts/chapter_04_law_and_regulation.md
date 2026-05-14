# Chapter 4 - Law and Regulation

Use `04_matrices/law_regulation_comparison_matrix.csv` as the working table
and `03_claim_tables/claim_table_master.csv` as the traceability layer.

## Phase 3 extraction notes

NYDFS guidance is now captured as `NYDFS_001`. Its scope is narrower than a
general stablecoin law: it applies only to U.S. dollar-backed stablecoins
issued under DFS supervision by DFS-regulated virtual currency entities
(`CLAIM_036`). For covered issuers, the guidance requires full daily backing
(`CLAIM_037`), lawful-holder at-par redemption in a timely fashion with a
default T+2 standard after a compliant redemption order (`CLAIM_038`),
specified reserve asset categories and custody restrictions (`CLAIM_039`),
and monthly CPA examinations plus annual controls attestations (`CLAIM_040`).

MiCA is now captured as `MICA_004`. It establishes uniform EU requirements
for crypto-asset issuers and crypto-asset service providers, including
transparency/disclosure, authorization and supervision, governance, holder and
client protection, and market-abuse prevention (`CLAIM_041`). For e-money
tokens, Article 49 supports at-any-time, par-value holder redemption and
white-paper disclosure of redemption conditions (`CLAIM_042`). Article 54
supports the EMT reserve/fund treatment: at least 30% in separate credit
institution accounts and the remainder in secure, low-risk, highly liquid
same-currency assets (`CLAIM_043`).

The next-phase MiCA extraction now separates ARTs from EMTs. Article 36
requires ART issuers to maintain a legally and operationally segregated
reserve of assets that covers referenced-asset risks, addresses redemption
liquidity risks, and is at least equal to aggregate holder claims
(`CLAIM_069`). Article 39 gives ART holders a permanent redemption right
against the issuer and, in certain issuer-failure contexts, in respect of
reserve assets; redemption may be in funds or referenced assets and is
generally no-fee except under Article 46 (`CLAIM_070`). Article 40 prohibits
ART issuers and CASPs from granting interest or holding-time-linked equivalent
benefits in relation to ARTs (`CLAIM_071`).

The significant-ART layer adds Article 45 obligations on top of the
Articles 36/39/40 core: a remuneration policy that does not create
incentives to relax risk standards, custody by different CASPs on a fair,
reasonable and non-discriminatory (FRAND) basis, and a liquidity management
policy and procedures ensuring resilient liquidity profile under stress.
EBA regulatory technical standards under Article 45(7) set the minimum
deposit-in-each-referenced-official-currency floor at no less than 60% of
the amount referenced in each official currency (`CLAIM_094`). Articles 46
and 47 require every ART issuer (significant or not) to maintain (a) a
recovery plan with options including liquidity fees on redemptions, daily
redemption caps, and redemption suspension, plus a competent-authority
power to temporarily suspend redemptions where justified by holder
interests and financial stability (`CLAIM_095`); and (b) a redemption
(wind-down) plan triggered by a competent-authority determination of
issuer inability to fulfil obligations, including insolvency, resolution,
or withdrawal of authorisation, with a temporary administrator designation
to ensure equitable holder treatment (`CLAIM_096`). The parallel
significant-EMT regime at Articles 56-58 transfers supervisory
responsibility to EBA, imposes Article 45(1)-(4)-style additional
obligations, and shortens the independent audit cadence to six months
under Article 58(1) by derogation from Article 36(9) (`CLAIM_097`).

The Bank of England's systemic stablecoin regime adds a third comparative
baseline. The 2023 discussion paper's preferred backing-asset model is
100% central bank deposits at the Bank of England, intended to eliminate
credit, liquidity and market risk in backing assets and to preserve the
singleness of money (`CLAIM_088`); the same paper requires issuers to
maintain a recovery and administration plan and to hold a shortfall
reserve on statutory trust for coinholders (`CLAIM_089`). The 2025
consultation revises the backing-asset rule: at least 40% of backing
assets must be held as unremunerated central bank deposits, up to 60% in
short-term sterling-denominated UK government debt securities, and a
step-up regime allows systemic-at-launch issuers to hold up to 95% UK
government debt securities and to scale down to 60% as the stablecoin
grows (`CLAIM_090`). The 2025 consultation also imposes quantitative
holding limits with no GENIUS or MiCA analogue: £20,000 per-coin retail
limit per individual and £10 million for businesses (`CLAIM_091`).

ESMA's January 2025 supervisory briefing for CASP authorisation under MiCA
states there are no low-risk CASPs and prescribes elevated NCA scrutiny
for CASPs above quantitative or structural thresholds (>1M EU yearly
active users or €3B balance sheet; >200k yearly active users outside the
home Member State; complex group structure spanning EMI/MiFID/CASP
frameworks; outsourcing of key functions or outsourcing outside the EU)
(`CLAIM_092`). ESMA's February 2025 Guidelines on transfer services for
crypto-assets under MiCA Article 82 require CASPs to provide
pre-contractual disclosure of DLT networks, execution times, estimated
irreversibility timing, fees, rejection conditions, and liability, and
require Travel-Rule-equivalent (TOFR Article 14) compliance before
transfer execution (`CLAIM_093`).

The GENIUS Act public-law text (`GENIUS_006`, Public Law 119-27) now anchors
the U.S. federal payment stablecoin baseline at the statutory layer, separate
from OCC/Treasury implementation materials. Six statutory anchors define the
regime:

- Issuer limitation: only "permitted payment stablecoin issuers" may issue
  payment stablecoins in the United States; Treasury safe harbors are
  narrowly bounded (Sec. 3(a), Sec. 3(c)) (`CLAIM_082`).
- Distribution transition and foreign issuer treatment: a 3-year transition
  after enactment makes it unlawful for a digital asset service provider to
  offer or sell a payment stablecoin in the United States unless issued by
  a permitted issuer; foreign payment stablecoin issuers may have their
  tokens distributed in the U.S. only if they have the technological
  capability and commitment to comply with lawful orders and Section 18
  reciprocal arrangements (Sec. 3(b)) (`CLAIM_083`).
- Reserve composition: reserves are restricted to an exhaustively
  enumerated list of high-quality liquid assets, with a 93-day cap on
  Treasury maturity, overnight terms for repos/reverse repos with
  overcollateralisation, registered MMFs invested solely in those
  underlying assets, and a primary-regulator approval gateway for any
  other similarly liquid government-issued asset (Sec. 4(1)(A))
  (`CLAIM_084`).
- Monthly disclosure and examination: permitted issuers must publish
  monthly reserve composition (including average tenor and geographic
  custody of each reserve category) and have the previous month-end report
  examined by a registered public accounting firm; CEO/CFO certification
  is subject to 18 U.S.C. 1350(c)-style criminal-penalty exposure for
  knowingly false certifications (Sec. 4(1)(C)-(D), 4(3)) (`CLAIM_085`).
- Holder yield prohibition: no permitted or foreign payment stablecoin
  issuer may pay the holder of a payment stablecoin any form of interest
  or yield (cash, tokens, or other consideration) solely in connection
  with holding, use, or retention of the stablecoin (Sec. 4(11))
  (`CLAIM_086`). This is the federal-statutory equivalent of MiCA ART
  Article 40 (`CLAIM_071`) and complements the issuer-terms no-holder-yield
  language at USDC (`CLAIM_059`), USDe (`CLAIM_066`), and the Paxos family
  (`CLAIM_074`).
- Insolvency customer priority: in any insolvency proceeding of a
  permitted payment stablecoin issuer, customer claims with respect to
  payment stablecoins held by the issuer take priority over the claims of
  any non-customer, subject only to other customers' claims with respect
  to the same stablecoins (Sec. 11) (`CLAIM_087`).

OCC GENIUS Act NPRM (`GENIUS_004`), Treasury state-level regime principles
(`GENIUS_005`), and FinCEN/Treasury AML-CFT materials (`GENIUS_001`,
`GENIUS_002`, `GENIUS_003`) remain proposed/implementation artifacts. The
OCC proposed redemption timing claim (`CLAIM_019`) and Treasury state-level
similarity principle claim (`CLAIM_020`) should be labelled as proposed or
implementation materials and not conflated with the GENIUS Act statutory
text above.

## Key comparison dimensions

- Definition of payment stablecoin / EMT / ART / GSC
- Permitted issuer
- Reserve assets
- Redemption rights
- Insolvency and asset segregation
- Interest/yield restrictions
- AML/CFT and sanctions
- Foreign issuer treatment

## Cross-jurisdiction comparison

The five regimes anchored above can be compared along six dimensions. Each
cell is supported by one or more `CLAIM_XXX` cites; cells marked "n/a"
indicate the regime does not impose a corresponding rule, not that the
question is unanswered.

| Dimension | GENIUS Act (US federal) | MiCA ART (EU) | MiCA EMT (EU) | BoE systemic (UK) | NYDFS guidance (NY) |
| --- | --- | --- | --- | --- | --- |
| Eligible issuer | Permitted payment stablecoin issuer only; Treasury limited safe harbors (`CLAIM_082`); 3-year transition gate for digital asset service providers (`CLAIM_083`) | Authorised ART issuer; significant-ART regime supervised by EBA (`CLAIM_094`) | Credit institution or e-money institution only (MiCA Article 48); significant-EMT regime supervised by EBA (`CLAIM_097`) | Recognised systemic stablecoin issuer under FSMA 2023, jointly regulated by Bank and FCA (`CLAIM_088`, `CLAIM_090`) | DFS-regulated virtual currency entity issuing under DFS supervision (`CLAIM_036`) |
| Reserve composition | Exhaustive HQLA list: Fed-account balances, insured deposits, ≤93-day Treasuries, overnight repos / reverse repos, registered MMFs invested solely in those assets, similar approved government-issued assets (`CLAIM_084`) | Reserve of assets at least equal to aggregate holder claims, segregated; significant-ART issuers have ≥60% minimum deposits in each referenced official currency under EBA RTS (`CLAIM_069`, `CLAIM_094`) | At least 30% of funds in separate credit-institution accounts plus remainder in secure, low-risk, highly liquid same-currency assets (`CLAIM_043`) | At least 40% unremunerated BoE central bank deposits + up to 60% short-term sterling-denominated UK government debt; step-up regime up to 95% UK gilts at launch (`CLAIM_090`) | Short-dated U.S. Treasury bills, qualifying overnight reverse repos, U.S.-government MMF shares under DFS limits, deposit accounts under DFS restrictions (`CLAIM_039`) |
| Redemption right | Issuer must be obligated to convert/redeem/repurchase for fixed monetary value (Sec. 2 definition); rehypothecation prohibited except for narrow purposes (`CLAIM_084` framing) | Permanent redemption right against the issuer; redemption in funds or referenced assets; generally no-fee except under Article 46 (`CLAIM_070`); recovery plan may impose liquidity fees, daily caps, or temporary suspension under competent authority (`CLAIM_095`) | At-any-time, par-value redemption from the issuer (`CLAIM_042`) | Par-value redemption + safeguarding regime to ensure backing assets available to satisfy redemption requests; redemption fees prohibited or cost-reflective only (BOE_003) | Lawful-holder at-par redemption in a timely fashion with default T+2 after a compliant redemption order (`CLAIM_038`) |
| Insolvency / wind-down | Customer-priority rule: customer claims for held payment stablecoins take priority over non-customer claims in any insolvency proceeding (Sec. 11, `CLAIM_087`) | ART redemption (wind-down) plan with temporary administrator designation triggered by competent authority determination of inability to fulfil obligations (`CLAIM_096`); ART recovery plan separately required (`CLAIM_095`) | Inherits EU credit-institution / EMI resolution framework via Article 48; significant-EMT issuers subject to Article 45-style obligations including six-month independent audits (`CLAIM_097`) | Recovery and administration plan plus shortfall reserve on statutory trust for the benefit of coinholders, in addition to PFMI capital (`CLAIM_089`) | Reserve assertion subject to monthly CPA examinations + annual controls attestation under DFS letter (`CLAIM_040`) |
| Holder yield / interest | No permitted or foreign payment stablecoin issuer may pay holders any form of interest or yield solely in connection with holding, use, or retention (Sec. 4(11), `CLAIM_086`) | ART issuers and CASPs prohibited from granting interest or holding-time-linked equivalent benefits (Article 40, `CLAIM_071`) | n/a directly at EMT statutory level (Article 49 par-value redemption stands separately); EMI prudential framework applies under Article 48 | Backing-asset CBD component is unremunerated; remunerated assets allowed only in the up-to-60% UK government debt sleeve (`CLAIM_090`) | n/a directly in the 2022 guidance; permitted reserve composition is the operative constraint (`CLAIM_039`) |
| Significant-token threshold | n/a (no formal significant-token tier) | EBA classification when at least three of the Article 43(1) criteria are met; Article 45 additional obligations and EBA supervision (`CLAIM_094`) | EBA classification when at least three of the Article 43(1) criteria are met; Article 58(1) imposes Article 45(1)-(4)-style obligations plus six-monthly independent audits (`CLAIM_097`) | HMT recognises systemic status on Bank recommendation under FSMA 2023; per-coin holding limits of £20,000 retail and £10 million business (`CLAIM_091`) | n/a |

The table is descriptive of the rules anchored to date and is not a
judgement of regulatory equivalence. Several cross-jurisdiction questions
remain open: GENIUS Act foreign-issuer treatment (Sec. 3(b)(2), Sec. 18)
versus MiCA ART/EMT cross-border passporting; whether the BoE up-to-95%
UK-gilt step-up regime would be recognised as substantially similar to
GENIUS Act Sec. 4(1)(A) for foreign-issuer reciprocity; and how
significant-EMT issuers issuing in a non-euro Member State currency
interact with the Article 56(4) derogation when 80% of holders /
transaction volume are concentrated in the home Member State.

## Remaining work

- Isolate any stablecoin-specific sections in the CLARITY Act; do not infer
  stablecoin conclusions from market-structure provisions.
- MiCA EMT-side Articles 51 (white paper), 52 (marketing communications),
  and 55 (additional issuer obligations) page-level extraction.
- Cross-jurisdiction equivalence analysis (what counts as "substantially
  similar" for foreign-issuer treatment under each regime).
