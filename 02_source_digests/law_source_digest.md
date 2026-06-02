# Law / Regulation Source Digest - Phase 3/Deficiency Follow-up Draft

This digest summarizes legal and regulatory evidence that is represented in
`03_claim_tables/claim_table_master.csv`.

## Phase 3 updates

- Added `NYDFS_001` as a primary source for the June 8, 2022 NYDFS guidance
  on U.S. dollar-backed stablecoins. It now has a local HTML archive in the
  deficiency download package.
- Added `MICA_004` as the official Regulation (EU) 2023/1114 source. The
  direct EUR-Lex HTML route was blocked by an anti-bot challenge during
  command-line fetch, but an official PDF copy is locally archived for
  reproducibility.
- Added BoE and ESMA deficiency-source entries for UK systemic stablecoin
  consultation material and MiCA/CASP implementation guidance.
- Added claims `CLAIM_036` to `CLAIM_043` covering NYDFS scope, backing,
  redemption, reserve assets, attestation, and MiCA EMT/ART framework basics.
- Added next-phase MiCA ART claims `CLAIM_069` to `CLAIM_071` for reserve of
  assets, ART redemption rights, and the ART interest prohibition. The official
  PDF remains the archived source of record; ESMA's interactive single
  rulebook was used as the readable extraction view for the same articles.

## GENIUS Act and U.S. implementation materials

The archive contains the GENIUS Act public-law text (`GENIUS_006`, Public Law
119-27) and several implementation-related materials, including the OCC NPRM,
Treasury state-level regime principles, and FinCEN/Treasury AML-CFT
materials. Earlier claim-table support included OCC proposed redemption
timing (`CLAIM_019`) and Treasury state-level regime principles
(`CLAIM_020`), which are implementation/proposed-rule artifacts and should
not be conflated with the public-law text.

Page-level extraction of the statutory text now supports seven anchor claims
that should drive the chapter-4 GENIUS Act section:

- Section 3(a) makes it unlawful for any person other than a "permitted
  payment stablecoin issuer" to issue a payment stablecoin in the United
  States; Section 3(c) authorises only narrow Treasury safe harbors
  (`CLAIM_082`).
- Section 3(b) imposes a 3-year transition after enactment, after which a
  digital asset service provider may not offer or sell a payment stablecoin
  to a U.S. person unless the stablecoin is issued by a permitted issuer;
  foreign payment stablecoin issuers may have their tokens distributed in
  the U.S. only if they have the technological capability and commitment to
  comply with lawful orders and any Section 18 reciprocal arrangement
  (`CLAIM_083`).
- Section 4(1)(A) restricts reserves to an exhaustive list of high-quality
  liquid assets: U.S. coins/currency or Fed-account balances, demand
  deposits at insured depository institutions, Treasury bills/notes/bonds
  with remaining or original maturity of 93 days or less, overnight
  repurchase agreements backed by such Treasuries, overnight reverse repos
  with overcollateralisation, registered MMFs invested solely in those
  underlying assets, and similar government-issued assets approved by the
  primary regulator (`CLAIM_084`).
- Sections 4(1)(C)-(D) and 4(3) require monthly reserve composition
  publication on the issuer's website (including average tenor and
  geographic custody) plus monthly examination by a registered public
  accounting firm with CEO/CFO certification under 18 U.S.C. 1350(c)-style
  criminal-penalty exposure for knowingly false certifications
  (`CLAIM_085`).
- Section 4(11) prohibits any permitted or foreign payment stablecoin issuer
  from paying the holder of a payment stablecoin any form of interest or
  yield (cash, tokens, or other consideration) solely in connection with
  holding, use, or retention of the stablecoin (`CLAIM_086`).
- Section 11 establishes that, in any insolvency proceeding of a permitted
  payment stablecoin issuer, customer claims with respect to payment
  stablecoins held by the issuer take priority over the claims of any
  non-customer (`CLAIM_087`).
- Section 18 establishes the foreign-issuer exception and reciprocity path:
  Treasury must determine that the foreign jurisdiction's payment-stablecoin
  regime is comparable to GENIUS, including Section 4(a); the issuer must
  register with the Comptroller; the issuer must hold U.S. financial-
  institution reserves sufficient for U.S. customer liquidity unless a
  reciprocal arrangement permits otherwise; and the issuer's jurisdiction
  must not be comprehensively sanctioned or a primary money-laundering-
  concern jurisdiction (`CLAIM_126`).

OCC NPRM, Treasury state-level principles, and FinCEN/Treasury AML-CFT
materials remain implementation/proposed-rule artifacts and should be cited
separately from the statutory anchors above. CLARITY Act stablecoin-specific
market-structure sections are now extracted separately below and should not be
conflated with GENIUS Act issuer/reserve rules.

## NYDFS

NYDFS guidance now has a registered primary URL source (`NYDFS_001`). It is
directly relevant to GUSD and RLUSD because their reserve reports and product
statements invoke NYDFS-style reserve, redemption, and attestation criteria.

Key extracted claims:

- Scope is limited to U.S. dollar-backed stablecoins issued under DFS
  supervision by DFS-regulated virtual currency entities (`CLAIM_036`).
- Covered stablecoins must be fully backed by reserve assets at least equal to
  outstanding units at the end of each business day (`CLAIM_037`).
- Redemption policies must confer on any lawful holder a right to redeem from
  the issuer at par in a timely fashion, with a default T+2 standard after a
  compliant redemption order (`CLAIM_038`).
- Reserve assets are limited to short-dated U.S. Treasury bills, qualifying
  overnight reverse repos, government money-market funds under DFS-approved
  limits, and deposit accounts under DFS-approved restrictions (`CLAIM_039`).
- Reserve assertions require monthly CPA examinations, and controls require an
  annual CPA attestation report (`CLAIM_040`).

Open point: page-level citation should now be anchored to the local HTML copy
before final report publication.

## CLARITY Act

The archive contains the CLARITY Act reported bill and House Report. These
should be treated as digital-asset market-structure sources rather than purely
stablecoin-specific sources. They are useful for defining the broader legal
perimeter of digital assets, intermediaries, and market activities.

Stablecoin-specific extraction now supports three bounded claims:

- The reported bill defines a "permitted payment stablecoin" as a
  national-currency-denominated digital asset designed for payment or
  settlement, issued by an issuer subject to State or Federal regulatory and
  supervisory authority, and either fixed-value redeemable/repurchasable or
  represented as maintaining stable value; it excludes national currency,
  certain securities, FDIC Act deposits, and Federal Credit Union Act accounts
  (`CLAIM_119`).
- Sec. 301 would exclude digital commodities and permitted payment
  stablecoins from several securities-law definitions across the Securities
  Act of 1933, Securities Exchange Act of 1934, Investment Advisers Act,
  Investment Company Act, and SIPA contexts (`CLAIM_120`).
- Sec. 302 would apply SEC anti-fraud, anti-manipulation and insider-trading
  authority to permitted payment stablecoin transactions only where those
  transactions are brokered, traded, or custodied by a broker or dealer,
  through an alternative trading system, or through a national securities
  exchange; it also creates a treatment rule for permitted payment stablecoin
  brokerage/trading/custody in those venues while preserving a rule of
  construction that other custody is not prohibited by that section
  (`CLAIM_121`).

Research boundary: these CLARITY Act claims are about market-structure
perimeter and intermediary anti-fraud authority. They do **not** establish
reserve composition, issuer eligibility, holder-yield, redemption, insolvency,
or foreign-issuer equivalence rules. Those conclusions should continue to come
from GENIUS Act, MiCA, BoE, NYDFS, and issuer terms.

## MiCA / EBA

The archive includes EBA/ESA consumer/factsheet material, EBA final reporting
ITS for ART/EMT reporting under MiCAR, and an EBA opinion on PSD2-MiCA
interplay. `MICA_004` now registers the official MiCA Regulation (EU)
2023/1114 URL.

Key extracted claims:

- MiCA establishes uniform EU rules for crypto-asset issuers and crypto-asset
  service providers, including transparency/disclosure, authorization and
  supervision, governance, holder/client protection, and market-abuse
  prevention (`CLAIM_041`).
- Article 49 requires e-money token issuers to redeem at any time and at par
  value upon holder request, with redemption conditions stated in the white
  paper (`CLAIM_042`).
- Article 54 requires at least 30% of funds received for EMTs to be deposited
  in separate accounts at credit institutions, with the remainder invested in
  secure low-risk highly liquid same-currency assets (`CLAIM_043`).
- Article 48 requires EMT issuers to be authorised as credit institutions or
  electronic money institutions, to notify and publish an Article 51 white
  paper, and treats EMTs as electronic money subject to the Electronic Money
  Directive unless MiCA states otherwise (`CLAIM_127`).
- Article 50 prohibits EMT issuers and CASPs from granting interest in
  relation to EMTs, broadly including time-linked remuneration, compensation,
  discounts, or equivalent benefits (`CLAIM_128`).
- Article 36 requires ART issuers to maintain a legally and operationally
  segregated reserve of assets that covers referenced-asset risks, addresses
  redemption-liquidity risks, and is at least equal to aggregate holder claims
  (`CLAIM_069`).
- Article 39 gives ART holders a permanent redemption right against the issuer
  and, in certain issuer-failure contexts, in respect of reserve assets; ART
  redemption may be in funds or referenced assets and is generally no-fee
  except under Article 46 (`CLAIM_070`).
- Article 40 prohibits ART issuers and CASPs from granting interest related to
  ARTs, including remuneration or equivalent benefits linked to holding time
  (`CLAIM_071`).

The significant-ART layer and ART recovery/redemption plans are now anchored
in the claim table. Article 45 imposes specific additional obligations on
significant-ART issuers: a remuneration policy that does not create
incentives to relax risk standards, custody by different CASPs on a fair,
reasonable and non-discriminatory basis, a liquidity management policy
ensuring resilient liquidity profile under stress, and a minimum 60%
deposit-in-each-referenced-official-currency floor under EBA RTS
(`CLAIM_094`). Article 46 requires every ART issuer (significant or not)
to draw up and maintain a recovery plan with options including liquidity
fees on redemptions, daily redemption limits, and redemption suspension,
with competent-authority power to temporarily suspend redemptions where
justified by holder interests and financial stability (`CLAIM_095`).
Article 47 requires every ART issuer to maintain a redemption (wind-down)
plan triggered by a competent-authority determination of inability to fulfil
obligations, with mandatory contractual arrangements, procedures, systems,
and a temporary administrator designation to ensure equitable holder
treatment (`CLAIM_096`).

The parallel significant-EMT regime is anchored at MiCA Articles 56-58:
EBA classifies EMTs as significant where at least three of the Article
43(1) criteria are met, supervisory responsibility transfers from the home
Member State competent authority to EBA, and significant EMT issuers are
subject to Article 45(1)-(4)-style obligations plus a six-month independent
audit cadence (Article 58(1) by derogation from Article 36(9))
(`CLAIM_097`). Article 56 also contains the non-euro significant-EMT
derogation: for a significant EMT denominated in a non-euro Member State
official currency, supervision does not transfer to EBA where at least 80% of
holders and transaction volume are concentrated in the home Member State
(`CLAIM_129`).

The EMT disclosure and conduct layer is now extracted. Article 51 requires
EMT white papers to disclose issuer, token, offer/admission, rights and
obligations including redemption conditions, technology, risks, and
environmental impacts; the white paper must be fair, clear and not misleading,
with no material omissions, a no-competent-authority-approval statement, a
management-body responsibility statement, and a non-technical summary that
states at-any-time par redemption and the redemption conditions
(`CLAIM_122`). Article 52 is a liability article, not a marketing article:
issuers and body members are liable to holders for Article 51 infringements
where incomplete, unfair, unclear or misleading information caused loss, and
contractual exclusions or limitations of that liability have no legal effect
(`CLAIM_123`). Article 53, not Article 52, governs EMT marketing
communications: they must be identifiable as marketing, fair, clear, not
misleading, consistent with the white paper, include issuer website/contact
information, include a clear at-any-time par-redemption statement, and cannot
be disseminated before white-paper publication (`CLAIM_124`). Article 55
applies Title III Chapter 6 recovery and redemption plan requirements to EMT
issuers, with six-month notification deadlines after offer to the public or
admission to trading (`CLAIM_125`).

Open point: direct EUR-Lex HTML remains inaccessible from the command-line
fetch path. The official PDF is archived and extraction now uses PyMuPDF
(`fitz`) for column-layout articles where pdfplumber returns only
headings.

## BoE / UK

The archive includes BoE Financial Stability Report and FPC Record
materials, plus the systemic stablecoin regime documents added in the
deficiency follow-up: the 2023 discussion paper (`BOE_003`) and the 2025
consultation (`BOE_004`).

The 2023 discussion paper's preferred backing-asset model is 100% central
bank deposits at the Bank of England, which is intended to eliminate
credit, liquidity and market risk in backing assets and to preserve the
singleness of money with par-value exchange against other sterling money
forms (`CLAIM_088`). Issuers of systemic-payment-system stablecoins are
also required to maintain a recovery and administration plan to fulfil
redemptions in the event of payment-chain failure, and to hold a shortfall
reserve of assets on statutory trust for the benefit of coinholders in
addition to PFMI-style capital (`CLAIM_089`).

The 2025 consultation materially revises the backing-asset rule in
response to industry feedback. The revised proposal requires at least 40%
of backing assets to be held as unremunerated central bank deposits at the
Bank, with up to 60% in short-term sterling-denominated UK government
debt securities. A step-up regime allows systemically important issuers at
launch to hold up to 95% of backing assets in UK government debt
securities as they scale, reducing to 60% as the stablecoin reaches a
scale that justifies tighter risk mitigation (`CLAIM_090`). The 2025
consultation also introduces quantitative holding limits with no GENIUS or
MiCA analogue: a per-coin retail limit of £20,000 for individuals
(cross-referenced to the digital pound consultation's £10,000-£20,000
range) and £10 million for businesses, with potential exemptions for
retail businesses and intermediaries servicing retail customers
(`CLAIM_091`).

For cross-border use cases, the same 2025 consultation states that wide
cross-border retail and/or corporate payment use would be jointly regulated
in the UK by the Bank and FCA and also subject to the home authority's
regime, after HM Treasury recognition of the payment system or service
provider as systemically important (`CLAIM_130`). The consultation also
foregrounds robust legal claim and always-at-par fiat redemption alongside
the 40%/60% backing-asset rule and 95% launch step-up (`CLAIM_131`).

## Foreign-issuer equivalence screen

The live comparison matrix for this item is
`04_matrices/foreign_issuer_equivalence_matrix.csv`. The research conclusion
is deliberately narrower than a legal opinion:

- GENIUS Section 18 is the governing U.S. screen for foreign payment
  stablecoin issuers. It requires Treasury comparability, Comptroller
  registration, U.S. liquidity reserves unless a reciprocal arrangement
  changes that requirement, sanctions / money-laundering screening, and the
  Section 3(b) lawful-order capability commitment (`CLAIM_083`,
  `CLAIM_126`).
- The BoE systemic regime is the closest non-U.S. comparison in supervisory
  intensity because it combines Bank/FCA joint supervision after HMT
  recognition, central-bank-deposit backing, short-term government-debt
  backing, robust legal claim, par fiat redemption, and recovery /
  administration planning (`CLAIM_089` to `CLAIM_091`, `CLAIM_130`,
  `CLAIM_131`). It is still indeterminate for GENIUS Section 18 because
  Treasury has not made a comparability determination and the archived BoE
  sources do not satisfy the U.S. liquidity-reserve, Comptroller-registration,
  or lawful-order requirements.
- MiCA EMT is the closer EU comparator for fiat-currency stablecoins because
  it requires credit-institution or EMI status, par redemption, EMT fund
  safeguarding, no EMT interest, white-paper / marketing disclosure,
  liability, recovery and redemption plans, and significant-EMT supervision
  where applicable (`CLAIM_042`, `CLAIM_043`, `CLAIM_097`,
  `CLAIM_122` to `CLAIM_129`). It still differs from GENIUS in reserve
  architecture and lacks the U.S.-specific Section 18 access mechanics.
- MiCA ART is weaker as a GENIUS payment-stablecoin-equivalence candidate
  because ART redemption may be in funds or referenced assets and recovery
  planning may include liquidity fees, daily redemption caps, or temporary
  suspension (`CLAIM_069` to `CLAIM_071`, `CLAIM_094` to `CLAIM_096`).
- CLARITY is not an equivalence regime; it supplies market-structure
  treatment for permitted payment stablecoins but no reserve, redemption,
  issuer-eligibility, or foreign-access baseline (`CLAIM_119` to
  `CLAIM_121`).

## ESMA / EU supervisory practice

ESMA's January 2025 supervisory briefing for CASP authorisation under
MiCA establishes a risk-based supervisory expectation rather than primary
statute. ESMA's position is that there are no "low-risk" CASPs, and that
CASPs above any of several quantitative or structural thresholds
(>1,000,000 yearly active users in the EU or €3,000,000,000 balance
sheet, >200,000 yearly active users outside the home Member State,
complex group structure spanning EMI/MiFID/CASP frameworks, or
outsourcing of key functions or outsourcing outside the EU) should be
subjected to elevated NCA scrutiny (`CLAIM_092`).

ESMA's February 2025 Guidelines on transfer services for crypto-assets
under MiCA Article 82 require CASPs providing transfer services on
behalf of clients to disclose, pre-contractually, the supported DLT
networks, maximum execution time, estimated time or block confirmations
for irreversibility, charges and fees, rejection conditions, and
liability for unauthorised or incorrectly executed transfers; the
Guidelines also require TOFR (Regulation EU 2023/1113, the EU Travel
Rule equivalent) Article 14 compliance before transfer initiation or
execution (`CLAIM_093`).

## Remaining Legal Research Gaps

- Taiwan enacted stablecoin legislation or sub-rules, once available, should
  be registered separately from CBC policy framing.
- Keep the cross-jurisdiction comparison table synchronized when later
  Taiwan statutory sources are added.
