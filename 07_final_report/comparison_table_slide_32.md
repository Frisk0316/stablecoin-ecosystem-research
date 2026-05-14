# Slide 32 — Cross-jurisdiction comparison (2/2)

跨司法管轄比較（下半）：破產 / 清算、持有人收益、Significant-token 門檻

This is the second of two slide-ready tables that together reproduce the
six-dimension cross-jurisdiction comparison at the close of chapter 4.
Together with the table for Slide 31, this covers the full six-dimension
comparison. Source claims are listed in shortened form to fit slide
formatting.

## Table

| 維度 / Dimension | GENIUS Act<br/>(US 聯邦) | MiCA ART<br/>(EU) | MiCA EMT<br/>(EU) | BoE 系統性<br/>(UK) | NYDFS 指引<br/>(NY) |
| --- | --- | --- | --- | --- | --- |
| **破產／清算**<br/>Insolvency / wind-down | 客戶優先：在任何 insolvency proceeding 中，客戶對其持有之 payment stablecoin 之債權優先於非客戶<br/>(Sec. 11, `CLAIM_087`) | 每位 ART 發行人須備 redemption (wind-down) plan，由主管機關判定無力履約時啟動，並指定臨時管理人<br/>(`CLAIM_096`); 另須備 recovery plan<br/>(`CLAIM_095`) | 沿用歐盟 credit institution / EMI 之 resolution 架構 (Art. 48); significant-EMT 須適用 Art. 45-style 義務 + 6 個月獨立 audit<br/>(`CLAIM_097`) | 發行人須備 recovery & administration plan + shortfall reserve on statutory trust，PFMI 資本之外的額外保障<br/>(`CLAIM_089`) | 儲備認證採月度 CPA 檢視 + 年度 controls attestation under DFS letter<br/>(`CLAIM_040`) |
| **持有人收益**<br/>Holder yield / interest | 任何 permitted 或 foreign payment stablecoin issuer 不得單純因 holding / use / retention 而給予持有人任何形式之 interest 或 yield (Sec. 4(11))<br/>(`CLAIM_086`) | ART issuer 與 CASP 禁止給予 interest 或 holding-time-linked equivalent benefits (Art. 40)<br/>(`CLAIM_071`) | EMT 統一規則中無直接 yield 禁令；Art. 49 par-value redemption 獨立適用；EMI 審慎制度依 Art. 48 適用 | Backing-asset 中央行存款部分為不付息 (unremunerated); 付息資產僅允於 ≤60% 英國公債部位<br/>(`CLAIM_090`) | 2022 指引未直接禁止；以允許之儲備組成作為實質約束<br/>(`CLAIM_039`) |
| **Significant-token 門檻**<br/>Significant-token threshold | 無正式 significant-token tier | EBA 在符合 Art. 43(1) 至少三項時 classify；Art. 45 額外義務並由 EBA 監管<br/>(`CLAIM_094`) | EBA 在符合 Art. 43(1) 至少三項時 classify；Art. 58(1) 套用 Art. 45(1)-(4) 義務 + 6 個月獨立 audit<br/>(`CLAIM_097`) | HMT 依 FSMA 2023 與 Bank 建議 recognise systemic 地位；個人持有上限 £20,000、企業 £10m<br/>(`CLAIM_091`) | 無正式 significant-token tier |

## Speaker notes (bilingual)

- The bottom half of the table is where the five regimes diverge most. The
  US chose a *bankruptcy-priority* rule; the EU chose an *operational
  wind-down plan* requirement; the UK chose a *statutory trust + shortfall
  reserve* construct; New York chose a *monthly examination* regime.
- 下半表是制度差異最顯著的部分：美國採客戶破產優先；歐盟採營運清算計畫＋臨時管理人；英國採法定信託＋短缺準備；紐約州採月度檢視。
- **Holder yield 是少數五制度高度一致的維度**：GENIUS、MiCA ART、BoE（CBD 部分）都明文壓低 holder yield；MiCA EMT 沒有直接禁令但 Art. 49 par-value 條款使收益難以實現；NYDFS 透過儲備組成限制間接達成。
- **Significant-token 是另一個顯著差異點**：美國目前沒有 significant tier；歐盟與英國各有不同型態的「規模門檻 → 額外義務」設計。
- 提醒讀書會：談「跨境等價（equivalence）」時，這六維比較表是判斷的基線，但「substantially similar」判斷尚未在本研究內進行。

## Visual notes for the design step

- 投影片版面：建議與 Slide 31 並列為「橫式雙投影片」一組，左為上半（Slide 31）、右為下半（Slide 32）。
- 顯示秩序：每一橫列由左至右為 GENIUS → MiCA ART → MiCA EMT → BoE → NYDFS，與 Slide 31 保持一致以利對讀。
- 「Holder yield」與「Significant-token」兩列建議用顏色強調（例如：高度一致的 yield 行用一種色、差異顯著的 significant-token 行用另一種色），讓聽眾一眼看出哪些維度收斂、哪些發散。
- CLAIM 引用使用 small footnote-style。
- 全表來源：`03_claim_tables/claim_table_master.csv`；slide 引用即可、不需展開全文。

## Combined table (reference only, not for slide)

If a single combined six-row × five-column slide is wanted instead of the
two-slide split, the full table is reproduced below for copy-paste into a
single-slide layout. Recommend against this for the reading-group
presentation, where the row density would be hard to read.

| 維度 | GENIUS Act | MiCA ART | MiCA EMT | BoE 系統性 | NYDFS |
| --- | --- | --- | --- | --- | --- |
| 適格發行者 | `CLAIM_082`, `CLAIM_083` | `CLAIM_094` | `CLAIM_097` | `CLAIM_088`, `CLAIM_090` | `CLAIM_036` |
| 儲備組成 | `CLAIM_084` | `CLAIM_069`, `CLAIM_094` | `CLAIM_043` | `CLAIM_090` | `CLAIM_039` |
| 贖回權 | `CLAIM_084` | `CLAIM_070`, `CLAIM_095` | `CLAIM_042` | `CLAIM_089` | `CLAIM_038` |
| 破產／清算 | `CLAIM_087` | `CLAIM_095`, `CLAIM_096` | `CLAIM_097` | `CLAIM_089` | `CLAIM_040` |
| 持有人收益 | `CLAIM_086` | `CLAIM_071` | n/a | `CLAIM_090` | n/a |
| Significant-token 門檻 | n/a | `CLAIM_094` | `CLAIM_097` | `CLAIM_091` | n/a |
