# Chapter 5 - Central Bank and International Institution Views

Working status: upgraded after deficiency-source recovery (v0.3). Use
`04_matrices/central_bank_theme_matrix.csv` as the chapter spine and cite
`03_claim_tables/claim_table_master.csv` before moving any conclusion into the
final report. Where this chapter draws on sources that are registered but not
yet anchored at claim level (notably ECB_001–004, BIS_001–003, FSB_001/003),
the discussion is framed at digest level only and flagged as conditional
pending v0.4 extraction. Taiwan CBC materials are now claim-backed at
`CLAIM_112` to `CLAIM_118`.

## Why this chapter exists

No major central bank or international institution treats stablecoins as a
settled question. Their public output is best read as a structured menu of
analytical channels - singleness/elasticity/integrity, deposit substitution,
safe-asset demand, run risk, payment competition, regulatory baseline - rather
than as a single verdict. The chapter inventories those channels with the
evidence currently anchored in the claim table, separates conditional framings
from formally extracted claims, and now adds a bounded Taiwan-specific
synthesis from CBC sources.

## BIS: the three-tests conceptual frame (digest-level)

BIS work is the strongest conceptual scaffolding in the registry. The 2025
Annual Economic Report (BIS_001) evaluates stablecoins against three monetary-
system tests — singleness of money, elasticity of supply, and integrity of
settlement — and concludes that current stablecoin design falls short on each.
BIS Papers No. 170 (BIS_002) develops the international monetary-system and
digital dollarisation angle, particularly for emerging-market economies where
private dollar-denominated tokens compete with the local unit of account.
BIS Working Paper 1270 (BIS_003) connects stablecoin demand to short-term
Treasury-bill pricing, which is the channel that links chapter 5 to the
reserve-assets discussion in chapter 3.

These three frames are present in
`02_source_digests/central_bank_source_digest.md` and
`04_matrices/central_bank_theme_matrix.csv` but have not yet been compressed
into discrete `CLAIM_XXX` entries. They should be treated as **conditional
framings**, not claim-anchored conclusions, until v0.4 extraction.

## Federal Reserve: market growth, vulnerabilities, deposits, credit

The Federal Reserve source set is the most fully extracted central-bank
material in this project. A 2025 FEDS Note links stablecoin adoption to the
holding of safer and more liquid reserves, while explicitly flagging
vulnerabilities arising from complex intermediation chains, vertical
integration between issuers and wallets, and retail wallet partnerships
(`CLAIM_044`, `CLAIM_045`). Market-capitalisation growth of roughly fifty
percent through 2025 is documented, but the FEDS Note treats it as a
market-development observation rather than as evidence of realised payment
demand.

The Fed's banking-system work supports a **conditional deposit-impact frame**:
bank deposits may shrink, recycle, or restructure depending on the demand
source, what assets users convert into stablecoins, and how issuers allocate
reserves between bank deposits, repo, and Treasury bills (`CLAIM_046`).
Credit effects therefore should not be stated as a one-way drain; the
mechanically defensible channel runs through deposit volume, deposit
composition, funding cost, and liquidity management (`CLAIM_047`). The IFDP
1334 framework (`CLAIM_048`) supplies the prior analytical scaffold: a
two-tiered banking arrangement can support stablecoin issuance and credit
creation, while a narrow-bank reserve design can strengthen peg credibility
at the cost of more direct disintermediation.

The unifying message is that the Federal Reserve does not endorse a single
deposit-flight story. It supplies the channels and asks for empirical
discipline on which channels actually operate in a given period.

## ECB: financial stability, monetary sovereignty, safe-asset and transmission channels (digest-level)

ECB output covers four overlapping themes documented in the theme matrix:
financial stability and spillovers (ECB_001), monetary sovereignty and
use-case decomposition (ECB_002), the global safe-asset channel from USD
stablecoins into U.S. public debt (ECB_003), and bank-deposit substitution
and monetary-policy transmission (ECB_004). The monetary-sovereignty paper is
particularly load-bearing for chapter 7's "raw on-chain volume is not payment
volume" guardrail: ECB analysis emphasises that the bulk of stablecoin activity
remains concentrated in crypto/DeFi/exchange liquidity, with payment and
treasury use still small in the snapshots they survey.

These four ECB sources are registered, locally archived, and discussed in
`central_bank_source_digest.md`, but they have not been formalised into
`CLAIM_XXX` entries in this build. Their inclusion here is digest-level
framing, marked for v0.4 extraction.

## IMF: run risk, reserve design, and payment competition

Two IMF claims are anchored. The reserve-backing / run-risk paper supports a
clear trade-off (`CLAIM_049`): safer asset backing lowers redemption-run risk
but reduces issuer profitability, weakening the private incentive to choose
conservative reserves absent other revenue mechanisms — a tension that maps
directly onto MiCA's interest prohibition and the GENIUS Act's reserve rules
discussed in chapter 4. The payment-competition paper anchors a market-
expectation result (`CLAIM_050`): an event-study estimate of roughly an
eighteen-percent value decline in incumbent payment-firm equity after
stablecoin-supportive policy news. This is a market-expectation observation,
not direct evidence of realised payment adoption, and should be cited as such.

IMF_002 and IMF_004 remain registered but unextracted; their inclusion would
extend coverage to statistics and shock channels.

## FSB: global baseline and implementation gap (digest-level)

The FSB output provides the global regulatory baseline. The 2023 Global
Stablecoin Recommendations (FSB_001) set the high-level expectations on
regulation, supervision, redemption, reserves, and disclosure. The 2025
thematic review (FSB_003) documents that implementation across jurisdictions
remains uneven, fragmented, and incomplete — which is the strongest available
source for the "regulatory arbitrage" framing in chapter 4. Neither has been
formalised at claim level in this build; both are treated here as digest-
level framings pending v0.4.

## Taiwan CBC: bounded Taiwan-specific synthesis

The CBC source set now supports a Taiwan-specific synthesis at claim level.
The first boundary is monetary status. CBC frames fiat-backed stablecoins as
tokenized private-sector money rather than legal-tender central-bank money:
they do not have legal-tender status, future development still depends on
central-bank money as anchor, and CBC does not expect central-bank seigniorage
power to be materially affected on that basis (`CLAIM_112`). This does not
mean stablecoins are irrelevant to policy; it means the relevant policy channel
is not loss of legal-tender issuance authority. The channels CBC emphasises
are payment design, reserve design, FX monitoring, digital dollarisation,
bank-credit transmission, and supervision.

The second boundary is architecture. CBC's tokenized-money-system paper keeps
the modern two-tier structure intact. Deposit tokens and stablecoins can be
private tokenized money, but central-bank money remains the cross-system
settlement asset that anchors singleness of money and payment finality
(`CLAIM_113`). This aligns CBC with the BIS-style public/private architecture:
innovation can occur in private money, but final trust still rests on the
central-bank settlement layer.

The third boundary is the USD stablecoin channel. CBC identifies a
digital-dollarisation and FX-management risk channel for broad USD-stablecoin
use. In CBC's framing, USD stablecoins can strengthen the dollar's role in
trade and payments, complicate traditional capital-management tools because
blockchain flows do not fully depend on centralized intermediaries, and in
high-inflation or capital-controlled economies can weaken local-currency
functions and pressure FX reserves and financial stability (`CLAIM_114`). For
Taiwan, this means the analytical question is not only whether an NTD
stablecoin is authorised. It is also whether global USD stablecoins create a
parallel dollar liquidity channel that affects FX monitoring and domestic
money-demand behaviour.

The fourth boundary is the New Taiwan dollar stablecoin design. CBC frames a
potential NTD stablecoin as similar to tokenized electronic-payment stored
value: issuance involves receiving funds from the general public for payment
use, and user funds should be protected by 100% reserve assets. CBC indicates
that once issuance reaches a threshold, part of the reserve should be placed as
central-bank reserves, while the rest may be held in deposits or high-quality,
highly liquid financial assets such as short-term bills or bonds
(`CLAIM_115`). CBC's regulatory description also records the draft virtual
asset service law direction: issuance permission, issuer qualification, asset
segregation, reserve management, audit/assurance, prohibition on interest or
yield payments, disclosure, and FSC-CBC consultation / joint sub-rules
(`CLAIM_118`). These are still draft-rule / policy-position materials, not a
substitute for enacted statutory text.

The fifth boundary is domestic macro impact. CBC expects current domestic
payment-system impact to be limited because Taiwan has few NTD-denominated
virtual assets and already has a complete, diverse, low-cost and real-time
payment environment (`CLAIM_116`). On monetary statistics and policy
transmission, CBC expects NTD stablecoin issuance to mainly reallocate funds
inside the monetary system rather than materially change broad money, bank
credit creation, or monetary-policy transmission. CBC states that M2 would
remain broadly unchanged, credit-creation effects should be limited,
short-term government-bond supply is limited, and CBC could still manage NTD
liquidity through policy rates and open-market operations (`CLAIM_117`).

The Taiwan synthesis should therefore be phrased as follows: Taiwan's central
bank does not currently frame stablecoins as a direct threat to legal-tender
issuance, but it treats USD stablecoins, NTD stablecoins, deposit tokens and
CBDC as separate design choices inside a two-tier money system. USD
stablecoins raise dollarisation and FX-monitoring issues; NTD stablecoins are
closer to tokenized electronic-payment stored value and require reserve,
redemption, disclosure and no-yield controls; domestic payment and M2 effects
are expected to be limited under current market conditions, but the conclusion
is conditional on the size of issuance and the development of NTD-denominated
tokenized assets.

The CBC policy synthesis above is now complemented by a separate
legislative-timeline layer. FSC Chairman Peng Jin-lung publicly stated on
2025-12-03 that Taiwan's first regulated stablecoin may enter the market in
the latter half of 2026 at the earliest and that an additional six-month
buffer is required after the FSC publishes subordinate regulations before the
law takes effect (`CLAIM_138`). Earlier draft-mechanics commentary describes
domestic stablecoin issuance approval, foreign-stablecoin trading consent,
reserve / audit / disclosure obligations, and subordinate regulations in
preparation (`CLAIM_139`).

The official Executive Yuan update dated 2026-04-02 states that the cabinet
approved the FSC draft VASP Act and submitted it to the Legislative Yuan,
covering VASPs and stablecoin issuers with financial-soundness, segregated-
custody and unfair-trading safeguards (`CLAIM_144`). A 2026-06-03 local press
report states that the Legislative Yuan Finance Committee completed first
review of the draft, including stablecoin licensing, full reserve segregation,
and fraud / manipulation provisions (`CLAIM_145`). The official Legislative
Yuan bill-detail page for the Executive Yuan draft records Finance Committee
review entries through 2026-06-03 with gazette production pending for the
June entries (`CLAIM_146`). These legislative-stage
claims should be cited alongside the CBC policy claims above, but they should
not be merged: CBC framing describes monetary-architecture and risk-channel
reasoning, while the VASP Act draft describes the legal gateway that will
govern issuance once enacted. Until enacted statutory text or FSC sub-rules
are registered, Taiwan should not be treated as having an in-force stablecoin
regime.

## Guardrails

- Do not state that stablecoins mechanically reduce bank lending. The
  supported position is conditional and depends on user conversion assets,
  reserve allocation, and whether deposits are recycled through banking
  channels.
- Separate retail payment adoption, DeFi/liquidity use, issuer reserve demand,
  and bank-funding effects.
- Treat CBDC and tokenised deposits as alternative public/private design
  responses, not as automatic substitutes for every stablecoin use case.
- Treat BIS, ECB, and FSB sub-sections above as digest-level framings, not as
  claim-anchored conclusions, until v0.4 formal claim extraction.

## Chapter limitations

- Fourteen central-bank claims (`CLAIM_044`-`CLAIM_050` and
  `CLAIM_112`-`CLAIM_118`) are formally anchored at this build; BIS, ECB,
  and FSB discussions remain digest-level. Readers should not treat the BIS
  three-tests framing, the ECB
  monetary-sovereignty argument, or the FSB implementation-gap finding as
  formally claim-backed.
- IMF_002 and IMF_004 are registered but unextracted.
- The Taiwan-specific synthesis is claim-backed for CBC_002-CBC_004 and
  now also has a legislative-stage layer at `CLAIM_138`, `CLAIM_139`,
  `CLAIM_144`, `CLAIM_145`, and `CLAIM_146` using `TAIWAN_VASP_001` to
  `TAIWAN_VASP_005`. Enacted Taiwan statutory text or FSC sub-rules have
  not been registered.
- See `00_project_management/unresolved_open_questions.md` for the full
  central-bank backlog.

## Next extraction tasks

- Promote ECB_001–004 themes to `CLAIM_XXX` entries (deposit substitution,
  monetary-policy transmission, monetary sovereignty, safe-asset channel).
- Promote BIS_001–003 themes to `CLAIM_XXX` entries (three-tests, EM
  dollarisation, T-bill price channel).
- Promote FSB_001/003 implementation-gap findings to `CLAIM_XXX` entries.
- Extract page-level Federal Reserve and IMF claims where the current entries
  are still abstract/summary based.
- If Taiwan's enacted VASP Act text or FSC sub-rules become available,
  register them separately from `TAIWAN_VASP_001` and `TAIWAN_VASP_002`
  (which remain legislative-stage) and from CBC policy framing.
- Normalise Treasury-market and safe-asset demand claims against issuer
  reserve data in the reserve-assets chapter.
