# Slide 31 — Cross-jurisdiction comparison (1/2)

跨司法管轄比較（上半）：適格發行者、儲備組成、贖回權

This is the first of two slide-ready tables that together reproduce the
six-dimension cross-jurisdiction comparison at the close of chapter 4.
Each cell cites the `CLAIM_XXX` rows that anchor it. Source claims are
listed in shortened form to fit slide formatting; full citations remain in
`03_claim_tables/claim_table_master.csv`.

## Table

| 維度 / Dimension | GENIUS Act<br/>(US 聯邦) | MiCA ART<br/>(EU) | MiCA EMT<br/>(EU) | BoE 系統性<br/>(UK) | NYDFS 指引<br/>(NY) |
| --- | --- | --- | --- | --- | --- |
| **適格發行者**<br/>Eligible issuer | Permitted payment stablecoin issuer only; Treasury 限縮 safe harbors; 3-年 distribution transition gate<br/>(`CLAIM_082`, `CLAIM_083`) | Authorised ART issuer; significant-ART 由 EBA 監管<br/>(`CLAIM_094`) | Credit institution 或 e-money institution (MiCA Art. 48); significant-EMT 由 EBA 監管<br/>(`CLAIM_097`) | Recognised systemic stablecoin issuer under FSMA 2023; Bank 與 FCA 共同監管<br/>(`CLAIM_088`, `CLAIM_090`) | DFS-regulated virtual currency entity issuing under DFS supervision<br/>(`CLAIM_036`) |
| **儲備組成**<br/>Reserve composition | 列舉式 HQLA 清單：Fed-account balances、insured deposits、≤93-day Treasuries、overnight repos / reverse repos、registered MMFs invested solely in those assets<br/>(`CLAIM_084`) | 儲備至少等於持有人總請求權、segregated；significant-ART 須持每一參考幣別 ≥60% 存款（EBA RTS）<br/>(`CLAIM_069`, `CLAIM_094`) | ≥30% 資金在獨立 credit institution 帳戶 + 餘額在 secure, low-risk, highly liquid 同幣別資產<br/>(`CLAIM_043`) | ≥40% 不付息 BoE 央行存款 + ≤60% 短期英國公債；step-up regime 發行初期可達 95% UK gilts<br/>(`CLAIM_090`) | 短期 U.S. Treasury bills、qualifying overnight reverse repos、U.S.-government MMF shares 與存款<br/>(`CLAIM_039`) |
| **贖回權**<br/>Redemption right | 發行人必須對 fixed monetary value 提供 convert / redeem / repurchase 義務 (Sec. 2 definition); rehypothecation 原則禁止<br/>(`CLAIM_084`) | 對發行人之 permanent redemption right; redemption in funds 或 referenced assets; 原則無 fee（Art. 46 例外）<br/>(`CLAIM_070`, `CLAIM_095`) | At-any-time, par-value redemption from the issuer<br/>(`CLAIM_042`) | Par-value 贖回 + safeguarding 制度確保 backing assets 可滿足贖回; redemption fees 原則禁止或限於成本<br/>(`CLAIM_089`) | Lawful-holder at-par redemption in a timely fashion，預設 T+2 after compliant order<br/>(`CLAIM_038`) |

## Speaker notes (bilingual)

- The five regimes converge on a common *structural* idea — only an
  authorised entity may issue, only enumerated assets may serve as
  reserves, and the issuer must owe an enforceable redemption duty —
  but they diverge materially on the **mix** of permitted reserve
  assets and on the *timing* of redemption.
- 五制度在「結構」上趨同（只有適格發行者、僅限列舉資產、發行人須負贖回義務），但「儲備組成」與「贖回時限」三制度差異顯著。
- 唯一強制要求央行存款作為儲備的是 BoE 系統性穩定幣制度；其他制度都允許短期國債 + 銀行存款 + 政府 MMF 組合。
- NYDFS 的 T+2 是目前所有制度中對 lawful holder（而非客戶）最直接的法定贖回時限。
- 提醒：「Lawful holder」與「Customer」不可混為一談；本研究第 2 章 issuer matrix 顯示直接贖回幾乎都被 Customer-only gating 限縮。

## Visual notes for the design step

- 表格五欄寬度建議：維度欄 12%、其他四欄各 22%；MiCA ART 與 MiCA EMT 並列以強化「兩套規則」對照。
- 若投影片版面太擠，可以把 GENIUS / NYDFS 並為「美國」群組、MiCA ART / EMT 並為「歐盟」群組、BoE 單列，三大群組以背景色區分。
- CLAIM 引用使用 small footnote-style，不要佔主體版面。
- 全表來源：`03_claim_tables/claim_table_master.csv`；slide 引用即可、不需展開全文。
