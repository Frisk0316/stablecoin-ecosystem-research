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

The EMT-side issuer, disclosure and conduct layer is now also claim-backed.
Article 48 requires EMT issuers to be credit institutions or electronic money
institutions, to notify and publish the Article 51 white paper, and treats
EMTs as electronic money under the Electronic Money Directive unless MiCA says
otherwise (`CLAIM_127`). Article 50 prohibits EMT issuers and CASPs from
granting interest in relation to EMTs, including time-linked remuneration,
compensation, discounts, or equivalent benefits (`CLAIM_128`). Article
51 requires EMT white papers to include issuer, token, offer/admission,
rights and obligations including redemption conditions, underlying technology,
risks, and environmental-impact information; the white paper must be fair,
clear, not misleading and free of material omissions, with a first-page
no-competent-authority-approval statement, management-body responsibility
statement, and a summary that states holders' at-any-time par redemption right
and redemption conditions (`CLAIM_122`). Article 52 is a white-paper liability
rule, not the marketing-communications rule: the issuer and management bodies
are liable for loss caused by incomplete, unfair, unclear or misleading Article
51 information, and contractual exclusions or limitations of that liability
have no legal effect (`CLAIM_123`). Article 53, not Article 52, requires EMT
marketing communications to be clearly identifiable, fair, clear, not
misleading, consistent with the white paper, to state the issuer website and
contact information, to include an at-any-time par-redemption statement, and
not to be disseminated before white-paper publication (`CLAIM_124`). Article
55 applies Title III Chapter 6 recovery and redemption plan requirements to EMT
issuers, with six-month notification deadlines after offer to the public or
admission to trading (`CLAIM_125`). Article 56's significant-EMT regime also
contains a non-euro derogation: where a significant EMT is denominated in a
non-euro Member State official currency and at least 80% of holders and
transaction volume are concentrated in the home Member State, supervision does
not transfer to EBA (`CLAIM_129`).

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

For cross-border payment use, the BoE 2025 consultation states that wide
cross-border retail and/or corporate stablecoin use would be jointly regulated
in the UK by the Bank and FCA and also subject to the home authority's regime
after HMT recognition (`CLAIM_130`). The consultation's core policy objective
is that systemic stablecoins purporting to be money provide robust legal
claim and always-at-par fiat redemption, alongside the backing-asset rule
above (`CLAIM_131`).

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
from OCC/Treasury implementation materials. Seven statutory anchors define the
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
- Foreign issuer exception and reciprocity: Section 18 allows foreign payment
  stablecoin issuers to fall outside the Section 3 prohibitions only if
  Treasury determines the foreign regime is comparable to GENIUS, including
  Section 4(a); the issuer registers with the Comptroller; the issuer holds
  U.S. financial-institution reserves sufficient for U.S. customer liquidity
  unless a reciprocal arrangement permits otherwise; and the issuer's
  jurisdiction is not comprehensively sanctioned or a primary money-
  laundering-concern jurisdiction (`CLAIM_126`).

OCC GENIUS Act NPRM (`GENIUS_004`), Treasury state-level regime principles
(`GENIUS_005`), and FinCEN/Treasury AML-CFT materials (`GENIUS_001`,
`GENIUS_002`, `GENIUS_003`) remain proposed/implementation artifacts. The
OCC proposed redemption timing claim (`CLAIM_019`) and Treasury state-level
similarity principle claim (`CLAIM_020`) should be labelled as proposed or
implementation materials and not conflated with the GENIUS Act statutory
text above.

The CLARITY Act is now extracted only for stablecoin-specific
market-structure treatment. It defines a "permitted payment stablecoin" as a
national-currency-denominated digital asset designed for payment or settlement,
issued by a State- or Federal-supervised issuer and either fixed-value
redeemable/repurchasable or represented as maintaining stable value; it
excludes national currency, certain securities, deposits, and credit-union
accounts (`CLAIM_119`). Sec. 301 would exclude permitted payment stablecoins
from several federal securities-law definitions (`CLAIM_120`). Sec. 302 would
apply SEC anti-fraud, anti-manipulation and insider-trading authority to
permitted payment stablecoin transactions only when brokered, traded, or
custodied by broker/dealers, alternative trading systems, or national
securities exchanges, while preserving a rule that the section does not
prohibit other custody arrangements (`CLAIM_121`). The boundary is important:
CLARITY does not supply the reserve-composition, issuer-eligibility,
redemption, holder-yield or insolvency baseline that GENIUS supplies for U.S.
payment stablecoins.

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
| Eligible issuer | Permitted payment stablecoin issuer only; Treasury limited safe harbors (`CLAIM_082`); 3-year transition gate plus Section 18 foreign-issuer exception / reciprocity screen (`CLAIM_083`, `CLAIM_126`) | Authorised ART issuer; significant-ART regime supervised by EBA (`CLAIM_094`) | Credit institution or e-money institution only; white paper notification/publication required (`CLAIM_127`); significant-EMT regime supervised by EBA subject to non-euro home-state derogation (`CLAIM_097`, `CLAIM_129`) | Recognised systemic stablecoin issuer under FSMA 2023, jointly regulated by Bank and FCA after HMT recognition; wide cross-border use also subject to home authority regime (`CLAIM_088`, `CLAIM_090`, `CLAIM_130`) | DFS-regulated virtual currency entity issuing under DFS supervision (`CLAIM_036`) |
| Reserve composition | Exhaustive HQLA list: Fed-account balances, insured deposits, ≤93-day Treasuries, overnight repos / reverse repos, registered MMFs invested solely in those assets, similar approved government-issued assets (`CLAIM_084`) | Reserve of assets at least equal to aggregate holder claims, segregated; significant-ART issuers have ≥60% minimum deposits in each referenced official currency under EBA RTS (`CLAIM_069`, `CLAIM_094`) | At least 30% of funds in separate credit-institution accounts plus remainder in secure, low-risk, highly liquid same-currency assets (`CLAIM_043`) | At least 40% unremunerated BoE central bank deposits + up to 60% short-term sterling-denominated UK government debt; step-up regime up to 95% UK gilts at launch (`CLAIM_090`) | Short-dated U.S. Treasury bills, qualifying overnight reverse repos, U.S.-government MMF shares under DFS limits, deposit accounts under DFS restrictions (`CLAIM_039`) |
| Redemption right | Issuer must be obligated to convert/redeem/repurchase for fixed monetary value (Sec. 2 definition); rehypothecation prohibited except for narrow purposes (`CLAIM_084` framing) | Permanent redemption right against the issuer; redemption in funds or referenced assets; generally no-fee except under Article 46 (`CLAIM_070`); recovery plan may impose liquidity fees, daily caps, or temporary suspension under competent authority (`CLAIM_095`) | At-any-time, par-value redemption from the issuer (`CLAIM_042`); Article 51/53 white paper and marketing communications must state redemption conditions / par-redemption right (`CLAIM_122`, `CLAIM_124`) | Robust legal claim and always-at-par fiat redemption, with backing assets and recovery/administration design intended to support redemption (`CLAIM_089`, `CLAIM_131`) | Lawful-holder at-par redemption in a timely fashion with default T+2 after a compliant redemption order (`CLAIM_038`) |
| Insolvency / wind-down | Customer-priority rule: customer claims for held payment stablecoins take priority over non-customer claims in any insolvency proceeding (Sec. 11, `CLAIM_087`) | ART redemption (wind-down) plan with temporary administrator designation triggered by competent authority determination of inability to fulfil obligations (`CLAIM_096`); ART recovery plan separately required (`CLAIM_095`) | Inherits EU credit-institution / EMI resolution framework via Article 48; significant-EMT issuers subject to Article 45-style obligations including six-month independent audits (`CLAIM_097`) | Recovery and administration plan plus shortfall reserve on statutory trust for the benefit of coinholders, in addition to PFMI capital (`CLAIM_089`) | Reserve assertion subject to monthly CPA examinations + annual controls attestation under DFS letter (`CLAIM_040`) |
| Holder yield / interest | No permitted or foreign payment stablecoin issuer may pay holders any form of interest or yield solely in connection with holding, use, or retention (Sec. 4(11), `CLAIM_086`) | ART issuers and CASPs prohibited from granting interest or holding-time-linked equivalent benefits (Article 40, `CLAIM_071`) | EMT issuers and CASPs may not grant interest; time-linked remuneration, compensation, discounts or equivalent benefits are treated as interest (`CLAIM_128`) | Backing-asset CBD component is unremunerated; remunerated assets allowed only in the up-to-60% UK government debt sleeve (`CLAIM_090`) | n/a directly in the 2022 guidance; permitted reserve composition is the operative constraint (`CLAIM_039`) |
| Significant-token threshold | n/a (no formal significant-token tier) | EBA classification when at least three of the Article 43(1) criteria are met; Article 45 additional obligations and EBA supervision (`CLAIM_094`) | EBA classification when at least three of the Article 43(1) criteria are met; Article 58(1) imposes Article 45(1)-(4)-style obligations plus six-monthly independent audits, subject to non-euro 80% home-state derogation (`CLAIM_097`, `CLAIM_129`) | HMT recognises systemic status on Bank recommendation under FSMA 2023; per-coin holding limits of £20,000 retail and £10 million business (`CLAIM_091`, `CLAIM_130`) | n/a |

## Foreign-issuer equivalence screen

The table above is descriptive. The dedicated working screen is
`04_matrices/foreign_issuer_equivalence_matrix.csv`. The screen's conclusion
is not that any foreign regime is already "substantially similar" to GENIUS.
Rather, GENIUS Section 18 makes foreign access a Treasury comparability,
registration, U.S. liquidity, sanctions/AML, and lawful-order question
(`CLAIM_083`, `CLAIM_126`).

The BoE systemic regime is the closest non-U.S. comparison in supervisory
intensity: HMT recognition, Bank/FCA joint supervision, home-authority
coordination for cross-border use, central-bank-deposit backing, short-term
government-debt backing, robust legal claim, always-at-par fiat redemption,
and recovery / administration planning all point toward a high-standard
regime (`CLAIM_089` to `CLAIM_091`, `CLAIM_130`, `CLAIM_131`). The fit is
still indeterminate for Section 18 because the BoE sources do not establish a
U.S. Treasury comparability determination, Comptroller registration,
U.S.-customer liquidity reserves, or U.S. lawful-order compliance. The
95%-UK-gilt launch step-up also requires a separate analysis against GENIUS
Section 4(a)'s 93-day Treasury and approved-government-asset baseline.

MiCA EMT is the stronger EU comparator for a fiat-currency payment
stablecoin because the issuer must be a credit institution or EMI, EMTs have
at-any-time par redemption, Article 50 prohibits EMT interest, Article 54
sets fund-safeguarding / investment rules, and Articles 51-55 supply white
paper, liability, marketing, recovery and redemption-plan layers
(`CLAIM_042`, `CLAIM_043`, `CLAIM_122` to `CLAIM_128`). Significant EMT
supervision can transfer to EBA, but the non-euro 80% home-state derogation
keeps some significant EMT supervision at home-state level (`CLAIM_129`).
MiCA EMT therefore cannot be treated as automatically comparable to GENIUS:
its reserve architecture and access mechanics differ, and it does not itself
provide the U.S. Section 18 registration, liquidity-reserve, reciprocal-
arrangement, or lawful-order pathway.

MiCA ART is weaker for GENIUS payment-stablecoin equivalence because ARTs can
reference baskets or assets, redemption may be in funds or referenced assets,
and the recovery plan can include liquidity fees, daily caps, or temporary
redemption suspension (`CLAIM_069` to `CLAIM_071`, `CLAIM_094` to
`CLAIM_096`). CLARITY should not be used for equivalence at all; it is a
market-structure bill for securities-law perimeter and intermediary conduct,
not a reserve, redemption, or foreign-access regime (`CLAIM_119` to
`CLAIM_121`).

## Remaining work

- Register and extract enacted Taiwan stablecoin legislation or sub-rules
  separately if they become available; CBC materials are policy framing, not
  enacted statute.
