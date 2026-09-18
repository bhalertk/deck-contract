# Eric Presentation Design System v1.2

狀態：Canonical（權威版本）  
語言：zh-Hant 優先，支援雙語編輯  
參考實作：`AI_Playbook_DesignSystem_v1.1.html`

---

# 0. 規則優先順序

當規則彼此衝突時，依下列順序判斷：

1. **Contract**
2. **Canon**
3. **Pattern-specific rules**
4. **Language defaults**
5. **Critique suggestions**

層級較高者覆蓋層級較低者。

模型或生成器在 Contract 未完成前，**不得**進入構圖（composition）階段。

---

# 1. CONTRACT

Contract 定義這份簡報「為何而做」，必須在任何視覺決策之前完成。

## 1.1 必要的 Deck Contract

```yaml
deck_id:
language: zh-Hant
audience:
  type:
  description:

goal:
  type: understand | decide | adopt | align | teach
  outcome:

core_message:

constraints:
  time_min:
  slide_count_max:
  technical_depth: low | mid | high

must_include: []
must_avoid: []

reference_deck:
  - AI_Playbook_DesignSystem_v1.1.html

energy_plan: []
forbidden_patterns: []
```

## 1.2 Contract Gate（合約關卡）

**RULE**  
進入構圖前，Contract 必須完整。

**WHEN**  
所有生成的簡報。

**CHECK**  
若缺少下列任一項，須在版面生成前 STOP（停止）：

- audience
- goal.type
- goal.outcome
- core_message
- slide_count_max
- technical_depth

**SEVERITY**  
ERROR

---

## 1.3 Narrative Contract（敘事合約）

在生成投影片前，須先定義：

- Context（脈絡）
- Tension（張力）
- Insight（洞見）
- Solution（解法）
- Action（行動）

簡報可以調整此結構，但仍必須有清楚的敘事主軸（narrative spine）。

每一頁投影片都必須具備：

```yaml
slide:
  intent:
  takeaway:
  pattern:
  density: LOW | MEDIUM | HIGH
  energy: CALM | FOCUSED | BOLD
  visual_anchor:
  transition:
```

若 `intent` 或 `takeaway` 無法清楚寫出，該頁應刪除或重新設計。

---

# 2. CANON

Canon 規則不可協商，除非 Contract 明確覆蓋。

## C01 — 一頁一個概念（One Slide, One Idea）

**RULE**  
每一頁投影片只傳達一個核心概念。

**WHEN**  
所有非附錄（non-appendix）投影片。

**CHECK**  
若該頁需要用「和」「也」等連接詞串起兩個獨立的結論句，或存在各自獨立的結論，則應拆分。

**SEVERITY**  
ERROR

---

## C02 — 唯一主要視覺焦點（One Primary Visual Anchor）

**RULE**  
每一頁投影片恰好有一個主要視覺焦點。

**WHEN**  
所有非附錄投影片。

**CHECK**  
視覺 QA 必須辨識出「眼睛最先看到什麼」。  
若有兩個以上元素的視覺權重大致相當，標記：

`S15_MULTIPLE_ANCHOR`

**SEVERITY**  
WARNING

---

## C03 — BODY 最小字級

**RULE**  
BODY（內文）文字不得小於 15 pt 等效字級。

**WHEN**  
簡報模式（presentation-mode）投影片。

**CHECK**  
- PPTX：BODY < 15 pt → 不合格
- HTML：BODY 低於對應等效值 → 不合格

例外：
- source（來源標註）
- footnote（註腳）
- caption（圖說）
- code（程式碼）

**SEVERITY**  
ERROR

---

## C04 — 不得為了塞下內容而縮小（Never Shrink to Solve Complexity）

**RULE**  
不得僅為了讓內容塞得下而縮小字級或視覺尺度。

**ACTION ORDER（處理順序）**

1. Simplify（簡化）
2. Visualize（視覺化）
3. Split（拆分）

**SEVERITY**  
若文字被縮小至低於最小值，判定為 ERROR。

---

## C05 — 標題要傳達意義（Titles Communicate Meaning）

**RULE**  
標題應傳達該頁的結論（takeaway），而非僅是主題名稱。

不佳：
- 系統架構
- 現況分析
- 未來規劃

較佳：
- Playbook 將一次性的探索轉換成可重複利用的組織經驗。

**CHECK**  
語意檢查（Semantic lint）自問：

> 若聽眾只讀標題，他們是否理解這頁想讓他們相信或記住什麼？

**SEVERITY**  
WARNING

---

## C06 — 先判斷關係，再決定容器（Relationship Before Container）

**RULE**  
在使用方框／卡片之前，先判斷資訊之間的關係。

可能的關係：
- sequence（順序）
- cause/effect（因果）
- hierarchy（層級）
- contrast（對比）
- dependency（依賴）
- loop（循環）
- input/output（輸入／輸出）

容器不是預設選項。

**SEVERITY**  
WARNING

---

## C07 — 裝飾需要理由（Decoration Requires Justification）

**RULE**  
每一個視覺元素都必須服務於溝通。

**CHECK**  
自問：

> 若移除這個元素，溝通效果是否會變弱？

若否，它就是裝飾。

**SEVERITY**  
WARNING

---

## C08 — 唯一結構性強調色（One Structural Accent）

**RULE**  
每一頁投影片最多只能使用一個結構性強調色（structural accent color）。

結構性強調色範例：
- 關鍵路徑
- 關鍵步驟
- 強調線條
- 關鍵數字
- 重點陳述

若語意色彩（semantic colors）的含義明確，則不算作第二個結構性強調色。

範例：
- 紅色／珊瑚色 = 危險／失敗／被否決的路徑
- 綠色 = 成功／已驗證
- 琥珀色 = 警告
- 藍色 = 主要結構性強調色

**SEVERITY**  
WARNING

---

## C09 — 構圖不得重複超過兩次（No Repeated Composition > 2）

**RULE**  
相同的視覺輪廓（visual silhouette）不得連續出現超過兩次。

**CHECK**  
僅比對 Pattern ID 是不夠的。  
需比較構圖輪廓：
- 標題位置
- 主要視覺區塊位置
- 主軸方向
- 主要區域數量

**SEVERITY**  
ERROR

---

## C10 — 內容字數上限（Content Maximum）

**RULE**  
簡報頁面內容不得超過 120 字（words）。

建議：
- LOW：20–40
- MEDIUM：40–80
- HIGH：80–120

**SEVERITY**  
ERROR

---

## C11 — 敘事目的（Narrative Purpose）

**RULE**  
每一頁投影片都必須有明確的敘事目的。

**CHECK**  
必須能完成這句話：

> 這一頁的存在是為了……

**SEVERITY**  
ERROR

---

## C12 — 證據必須有脈絡（Evidence Must Have Context）

**RULE**  
孤立的數字不算證據。

一個數字至少應回答下列其中一項：

- 與什麼比較？
- 前後對比？
- 預期 vs 實際？
- 部分 vs 整體？
- 比率 vs 基準？
- 為什麼重要？

**SEVERITY**  
WARNING

---

## C13 — 誠實優於完整（Honesty Over Completeness）

**RULE**  
未經驗證的資訊，不得以與已驗證資訊相同的確定性呈現。

信心狀態：

- ✅ 已驗證
- ⚠️ 推測
- ❓ 未知
- ⏳ 暫緩

**SEVERITY**  
若隱藏不確定性，判定為 ERROR。

---

## C14 — 視覺張力是節奏性的，而非恆定的（Visual Boldness Is Rhythmic, Not Constant）

**RULE**  
有選擇性地使用 BOLD 構圖。

**TARGET（目標）**  
每 3–5 頁至少要有一頁 BOLD。

**CHECK**  
若連續 5 頁都沒有 BOLD 投影片，提出警告。

**SEVERITY**  
WARNING

---

## C15 — BOLD 必須言之有物（BOLD Slides Must Be Earned）

**RULE**  
BOLD 投影片必須使用至少一個已定義的 Signature Motif，並強化該頁的結論。

**CHECK**  
若移除 BOLD 手法後溝通效果不受影響，代表那是裝飾。

**SEVERITY**  
WARNING

---

# 3. LANGUAGE

Language 定義字體排印、色彩、構圖、視覺動機（motif）、版型（pattern）與編輯行為。

# 3.1 藝術方向（Art Direction）

目標比例：

- 70% Editorial Tech
- 30% Strategy Deck

整份簡報應該給人以下感覺：

- clear（清晰）
- restrained（克制）
- narrative-driven（以敘事為導向）
- technical when needed（必要時具技術感）
- visually intentional（視覺上是刻意安排的）
- editorially bold（編輯手法大膽）
- memorable without being decorative（令人印象深刻但不流於裝飾）

避免：

- generic SaaS deck look（通用 SaaS 簡報感）
- excessive cards（過多卡片）
- decorative gradients（裝飾性漸層）
- glassmorphism（玻璃擬態）
- neon glow（霓虹光暈）
- random blobs（隨機色塊／blob）
- icon-heavy layouts（大量 icon 的版面）
- corporate-template repetition（企業範本式的重複套用）

核心原則：

> 大膽應體現在尺度與構圖上，而非裝飾上。

---

# 3.2 字體排印（Typography）

## 字體家族

中文：
- Noto Sans TC
- Source Han Sans TC

英文：
- Inter

程式碼：
- JetBrains Mono（選用；僅用於 CODE pattern）

## 字級尺度（Type Scale）

PPTX 標準：

- DISPLAY：40–48 pt
- H1：30–34 pt
- H2：20–24 pt
- BODY：15–17 pt
- SMALL：11–12 pt
- CODE：12–14 pt

大數字（Big numbers）主要由視覺面積決定，而非嚴格的字級上限。

---

# 3.3 中文編輯排版（Chinese Editorial Typesetting）

## CT01 — 避免孤字（Avoid Orphan Characters）

在可避免的情況下，不要讓標題最後一行只剩 1–2 個中文字。

不佳：

```text
下一個人，不必重走我走過的
彎路。
```

較佳：

```text
下一個人，
不必重走我走過的彎路。
```

---

## CT02 — 數字與單位不可拆行（Keep Number + Unit Together）

避免在以下位置換行：

- 300 / 月
- 2.9 秒
- 5.3 倍
- 15 pt

---

## CT03 — 避免標點符號出現在行首（Avoid Punctuation at Line Start）

在可控制的情況下，不允許下列符號出現在行首：

- ，
- 。
- ：
- ；
- ）
- 】

---

## CT04 — 中英混排層級（Mixed Chinese / English Hierarchy）

預設雙語層級：

- eyebrow（上緣標籤）：英文／大寫
- primary title（主標題）：繁體中文
- technical identifiers（技術識別詞）：保留原文英文
- micro labels（微標籤）：可使用英文
- explanations（說明文字）：繁體中文

不要將英文的字距（letter-spacing）規則套用在中文文字上。

---

## CT05 — 結論式標題使用語句邏輯（Conclusion Titles Use Sentence Logic）

標題應以「結論」的方式書寫，而非目錄式的標籤。

只有在能改善閱讀節奏時才使用標點符號。

---

# 3.4 色彩（Color）

## 核心色彩 Token

```text
CANVAS       #F7F7F5
SURFACE      #FFFFFF
INK          #18181B
MUTED        #71717A
LINE         #E4E4E7
LINE_STRONG  #A1A1AA
ACCENT       #2563EB
ACCENT_LIGHT #60A5FA
```

## 語意色彩 Token

```text
SUCCESS      #16A34A
WARNING      #D97706
DANGER       #D85B42
INFO         #2563EB
```

備註：
`DANGER` 對齊參考簡報中的珊瑚色。

## 色彩使用規則

- 中性色（neutral palette）為主導色調。
- 每頁最多一個結構性強調色。
- 語意色彩需有明確含義。
- 「不同項目」不等於「不同顏色」。
- 避免彩虹式（rainbow）圖表。
- 預設避免裝飾性漸層。

---

# 3.5 實作對應（Implementation Mapping）

本系統同時支援 PPTX 與離線 HTML。

## 標準投影片座標系統

16:9  
13.333 × 7.5 in

## 安全範圍（Safe Area）

- 左：0.65"
- 右：0.65"
- 上：0.55"
- 下：0.50"

## HTML 對應

以標準化的 7.5 in 高畫布為基準：

```text
1vh ≈ 0.075in ≈ 5.4pt
```

這是「設計上等效」的對應關係，不保證瀏覽器上的實際物理英吋。

使用原則：
- PPTX → pt / in
- HTML → vh / vw

兩種實作都必須保留相對比例與視覺層級。

---

# 3.6 網格與間距（Grid and Spacing）

12 欄網格（12-column grid）。

常見分割方式：

- 6 + 6
- 8 + 4
- 5 + 7
- 4 + 4 + 4
- 3 + 6 + 3
- 2 + 8 + 2

間距尺度：

- 0.10"
- 0.20"
- 0.30"
- 0.40"
- 0.60"
- 0.80"
- 1.20"

網格是用來對齊的，不是用來自動產生方框的。

---

# 3.7 Chrome（介面裝飾框架）

Chrome 指的是重複出現的簡報介面元素。

## Eyebrow（上緣標籤）

預設格式：

```text
NN · LABEL
```

範例：

- 01 · POSITIONING
- 05 · EVIDENCE
- 10 · ADOPTION

樣式：
- 英文
- 大寫
- 低調色（muted）
- 半粗體（semibold）
- 可使用字距（letter spacing）

深色投影片：
- 使用淺色的 muted token

## Footer（頁尾）

選用。

用途：
- 簡報識別資訊
- 資料來源標註
- 小型脈絡標籤

不要重複無意義的資訊。

## Progress / Nav（進度／導覽）

僅適用於離線 HTML。

瀏覽器控制項不算作投影片內容。

---

# 3.8 Signature Motifs（簽名式視覺動機）

每頁最多使用一種主導 motif。

## M-A — Editorial Scale（編輯級放大）

使用一個超大型的陳述句或數字。

目標視覺面積：
- 30–65%

使用時機：
- statement（陳述）
- key evidence（關鍵證據）
- decision（決策）
- hero（開場主視覺）

---

## M-B — Directional Rule（方向性主軸線）

一條強而有力的線／箭頭作為結構主軸。

使用時機：
- before → after（前後對比）
- experience → playbook → next person（經驗 → 方法 → 下一個人）
- process（流程）
- transformation（轉變）
- data flow（資料流）

---

## M-C — Cropped Geometry（裁切幾何形）

使用 1–2 個從畫布邊緣進入的大型純色幾何形狀。

使用時機：
- hero（開場主視覺）
- section transition（章節轉場）
- conceptual framing（概念性框架）

不要使用裝飾性的隨機 blob。

---

## M-D — Evidence Split（證據分割）

預設比例：
- 65% 證據
- 35% 詮釋

避免自動採用 50/50。

---

## M-E — Full Visual（全幅視覺）

一個視覺元素主導幾乎整頁畫面。

使用於：
- screenshot（截圖）
- diagram（圖表）
- photo（照片）
- code excerpt（程式碼片段）

文字退居為註解。

---

## M-F — Dark Narrative Break（深色敘事轉折）

使用時機：
- insight（洞見）
- contradiction（矛盾）
- decision（決策）
- closing（結尾）

目標：
- 每份簡報 1–3 頁

警告：
- 深色投影片超過整份簡報的 25%

---

## M-G — Broken Symmetry（破除對稱）

使用不對稱構圖，反映資訊層級的不對等。

---

## M-H — Editorial Framing（編輯式框架）

使用：
- labels（標籤）
- rules（分隔線）
- margins（邊界）
- negative space（留白）

優先使用留白，而非容器。

---

# 3.9 視覺能量（Visual Energy）

每頁投影片有一個能量等級。

## CALM

使用於：
- technical detail（技術細節）
- tables（表格）
- architecture detail（架構細節）
- supporting explanation（輔助說明）

## FOCUSED

預設等級。

使用於：
- process（流程）
- evidence（證據）
- contrast（對比）
- relationship（關係）

## BOLD

使用於：
- hero（開場主視覺）
- key statement（關鍵陳述）
- key evidence（關鍵證據）
- decision（決策）
- narrative break（敘事轉折）
- closing（結尾）

建議的簡報節奏：

```text
BOLD → FOCUSED → FOCUSED → CALM → BOLD
```

非強制固定順序。

---

# 3.10 數字修辭（Number Rhetoric）

數字是一級視覺元素（first-class visual elements）。

## NR01 — Mega Number（超大數字）

使用時機：
- 單一數字即為主要證據
- 該數字改變了整體詮釋
- 存在有意義的基準值（baseline）

範例：
- 5,523 vs 1,038
- 9,702 created, then removed

## NR02 — Metric Band（指標群組）

使用時機：
- 3–5 個指標共同描述系統狀態

範例：
- 12,895 nodes
- 18,618 edges
- 10,756 links
- 300/month

## NR03 — Before / After（前後對比）

使用：
- 860 → 11,038
- 2.9 → 11.7 sec

當變化本身很重要時，優先使用方向性標記法。

## NR04 — No Orphan KPI（不留孤立指標）

一個沒有比較對象、詮釋或後果說明的大數字，不算是 EVIDENCE（證據）。

---

# 3.11 信心程度圖例（Confidence Legend）

信心狀態：

| 狀態 | 意義 | 視覺處理 |
|---|---|---|
| ✅ 已驗證 | 直接證據 | 正常／高信心 |
| ⚠️ 推測 | 推論而來 | 使用警告語意色 |
| ❓ 未知 | 無法判定 | 低調色／明確標示未知 |
| ⏳ 暫緩 | 尚未審查 | 低調色／標示待處理 |

除非該頁的重點就是「不確定性」本身，否則未驗證內容在視覺上不得壓過已驗證內容。

---

# 3.12 選用元件（Optional Components）

## Icons（圖示）

僅限 Lucide。

僅在以下情況使用：
- architecture（架構）
- code（程式碼）
- technical labels（技術標籤）
- 能改善理解時

不要僅為了裝飾卡片而加上 icon。

## Code（程式碼）

使用 JetBrains Mono。

優先原則：
- 5–15 行相關程式碼
- 除非 IDE 情境本身很重要，否則不使用完整 IDE 截圖

## Cards（卡片）

預設：避免使用。

僅在以下情況使用：
- 語意分組確有必要
- 邊界關係很重要
- 單靠留白無法說明分組關係

若必須使用：

- 背景：#FFFFFF
- 邊框：#E4E4E7
- 圓角：6–8 px
- 陰影：無

---

# 4. PATTERN LIBRARY（版型庫）

Pattern（版型）是溝通功能，不是固定範本。

每個 Pattern 包含：

- Use when（使用時機）
- Do not use when（不使用時機）
- Default motif（預設視覺動機）
- Density（密度）
- Reference（參考頁）

---

## P01 HERO

Use when：
- 引入核心概念
- 開場

Do not use when：
- 該頁只是章節標題頁
- 沒有明確的論點（thesis）

Default motif：
- M-A Editorial Scale
- M-C Cropped Geometry

Density：
- LOW

Reference：
- Reference Deck Slide 01

---

## P02 STATEMENT

Use when：
- 需要讓聽眾記住某個洞見
- 需要敘事重置（narrative reset）

Do not use when：
- 需要多個支持性論點

Default motif：
- M-A
- M-F

Density：
- LOW

Reference：
- Slide 05

---

## P03 PROBLEM

Use when：
- 需要呈現摩擦點、矛盾或隱藏成本

Do not use when：
- 內容只是一份沒有結構的問題清單

Default motif：
- M-A
- M-G

Density：
- MEDIUM

Reference：
- Slide 03

---

## P04 CONTRAST

Use when：
- before/after（前後對比）
- old/new（新舊對比）
- A/B
- wrong/right（對錯對比）

Do not use when：
- 兩側並不具有可比性
- 50/50 的呈現方式會暗示錯誤的對等關係

Default motif：
- M-D
- M-G

Density：
- MEDIUM

Reference：
- Slide 02

---

## P05 PROCESS

Use when：
- 順序很重要
- 轉變過程很重要

Do not use when：
- 各項目彼此相關但沒有順序性

Default motif：
- M-B

Density：
- MEDIUM

Reference：
- Slide 04

---

## P06 RELATIONSHIP

Use when：
- 說明概念之間的關係
- cause/effect（因果）
- dependency（依賴）
- hierarchy（層級）

Do not use when：
- 用 PROCESS（流程）呈現會更清楚

Density：
- MEDIUM

Reference：
- 非參考簡報中的主要版型；請套用 Architecture 相關規則

---

## P07 ARCHITECTURE

Use when：
- 系統結構與資料流很重要

Do not use when：
- 聽眾只需要理解單一概念性關係

Rules：
- 只有一個主導的流向
- 邊界必須清楚可見
- 漸進式揭露（progressive disclosure）
- 建議主要節點數量為 7 ± 2 個

Density：
- HIGH

---

## P08 EVIDENCE

Use when：
- 數據支持或推翻某個論點

Do not use when：
- 只有一個孤立的 KPI，沒有「所以呢（so what）」

Default motif：
- M-A
- M-D

Density：
- MEDIUM

Reference：
- Slide 06
- Slide 12

---

## P09 SCREENSHOT

Use when：
- 真實的 UI 或結果本身就是證據

Do not use when：
- 截圖只是裝飾性用途
- 截圖內容已不可讀

Default motif：
- M-E

Density：
- MEDIUM

Rules：
- crop（裁切）
- zoom（放大）
- annotate（加註）
- 建議標註文字為 3–8 個字

---

## P10 CODE

Use when：
- 實作細節能證明某個論點

Do not use when：
- 程式碼只是裝飾用途

Density：
- HIGH

---

## P11 DECISION

Use when：
- 需要做出決策或下一步行動

Do not use when：
- 這份簡報只是提供資訊，不需要決策

Default motif：
- M-A
- M-F

Density：
- LOW/MEDIUM

Reference：
- Slide 13

---

## P12 SUMMARY

Use when：
- 為敘事作結

Do not use when：
- 內容會變成條列式重點回顧

Density：
- LOW

Reference：
- Slide 13

---

## P13 QUALITY GATE

Use when：
- 需要區分「阻斷性問題」與「持續監控中的狀況」
- 需要判斷現階段哪些項目必須為零

Do not use when：
- 各類別在操作上並無實質差異

Default motif：
- 非對稱雙區塊對比（asymmetric two-zone contrast）

Density：
- MEDIUM

Reference：
- Slide 09

---

## P14 COST SPLIT

Use when：
- 區分可重複使用與需重新校準的工作
- 說明成本實際發生在哪裡

Do not use when：
- 成本只是單一純量數字

Default motif：
- 流程 + 分割詮釋

Density：
- MEDIUM

Reference：
- Slide 10

---

## P15 ADOPTION STEPS

Use when：
- 存在導入／上手階段
- 其中某個階段特別關鍵

Do not use when：
- 各階段地位相同，沒有敘事焦點

Default motif：
- M-B
- 標記出關鍵中段步驟（keyed middle step）

Density：
- MEDIUM

Reference：
- Slide 11

---

# 5. REFERENCE DECK（參考簡報）

標準參考檔案：

`AI_Playbook_DesignSystem_v1.1.html`

當某條抽象規則存在多種合理的視覺詮釋方式時，優先採用參考簡報所展示的視覺語言。

## 5.1 版型對照表（Pattern Map）

| Slide | Pattern | Energy | Motif |
|---|---|---|---|
| 01 | HERO | BOLD | M-A + M-C |
| 02 | CONTRAST | FOCUSED | M-G |
| 03 | PROBLEM | FOCUSED | M-A |
| 04 | PROCESS / REFRAME | FOCUSED | M-B |
| 05 | STATEMENT | BOLD | M-F |
| 06 | EVIDENCE | FOCUSED | M-A + M-D |
| 07 | EVIDENCE / PITFALL | BOLD | M-A |
| 08 | EVIDENCE | FOCUSED | text-led |
| 09 | QUALITY GATE | FOCUSED | asymmetric zone |
| 10 | COST SPLIT | FOCUSED | M-B |
| 11 | ADOPTION STEPS | BOLD | keyed step |
| 12 | EVIDENCE | FOCUSED | metric band |
| 13 | DECISION / SUMMARY | BOLD | M-F |

## 5.2 參考原則

參考簡報不是可以逐字複製的範本。

用它來校準：
- scale（比例尺度）
- asymmetry（不對稱）
- whitespace（留白）
- headline behavior（標題表現方式）
- rhythm（節奏）
- 大膽時刻的使用方式

---

# 6. CRITIQUE（審查）

Critique 檢查輸出結果是否符合 Contract、Canon 與 Language。

# 6.1 簡報氣味（Presentation Smells）

除非特別標註，Smells 一律視為警告（warnings）。

## S01 Card Grid Smell（卡片方格氣味）

觸發條件：
- 出現 3 個以上視覺上相同的卡片
- 使用卡片並沒有語意分組上的理由

---

## S02 Topic Title Smell（主題式標題氣味）

觸發條件：
- 標題只點出主題，沒有傳達結論

---

## S03 Wall of Text Smell（文字牆氣味）

觸發條件：
- LOW 超過 40 字
- MEDIUM 超過 80 字
- HIGH 超過 120 字
- 出現 4 個以上的長條列點

---

## S04 Tiny Text Smell（小字氣味）

觸發條件：
- BODY 小於 15 pt 等效字級

Severity（嚴重程度）：
- ERROR

---

## S05 Decoration Smell（裝飾氣味）

觸發條件：
- 移除該元素不會造成資訊損失

---

## S06 Generic AI Imagery Smell（通用 AI 意象氣味）

觸發條件：
- 出現通用的 AI／機器人／發光大腦／握手／火箭意象
- 沒有與內容相關的理由

---

## S07 Rainbow Smell（彩虹氣味）

觸發條件：
- 使用多種飽和色彩，卻沒有語意上的角色分工

---

## S08 Everything-in-a-Box Smell（什麼都裝箱氣味）

觸發條件：
- 文字與概念被不必要地包進容器中

---

## S09 Perfect Symmetry Smell（完美對稱氣味）

觸發條件：
- 不對等的資訊被賦予相同的視覺權重

---

## S10 Repeated Layout Smell（版面重複氣味）

觸發條件：
- 相同輪廓連續出現超過 2 次

Severity：
- ERROR

---

## S11 Diagram Spaghetti Smell（義大利麵圖表氣味）

觸發條件：
- 節點過多
- 連接線交錯
- 流向方向混亂
- 邊界不清楚

---

## S12 Document-on-a-Slide Smell（文件搬進投影片氣味）

觸發條件：
- 直接複製來源文件的結構
- 該頁看起來像是報告的其中一頁

---

## S13 Flat Design Smell（扁平設計氣味）

觸發條件：
- 每一頁都很安全但令人無感
- 連續 5 頁都沒有視覺上的節奏轉換（visual reset）

---

## S14 Template Rhythm Smell（範本節奏氣味）

觸發條件：
- 內容不同，但標題／內容的骨架一再重複相同

---

## S15 Multiple Anchor Smell（多重焦點氣味）

觸發條件：
- 兩個以上的元素在競爭主要視覺焦點的地位

---

# 6.2 負面構圖範例（Negative Composition Examples）

不應生成以下內容：

1. 三張視覺上相同的圓角卡片，各自搭配一個 icon、標題與段落。
2. 連續三頁使用相同的「標題在上、內容在下」輪廓。
3. 資訊重要性不對等時，卻採用 50/50 的對比呈現。
4. 直接把來源文件的章節標題拿來當投影片標題。
5. 深色背景搭配密集的條列清單。
6. 大數字後面緊跟著另一個同樣醒目的長段落。
7. 使用多種強調色，卻只是為了讓各項目看起來不一樣。
8. 截圖被縮小到文字已無法閱讀。

---

# 6.3 結構檢查（Structural Lint）

盡可能以機器可檢查的方式進行。

檢查項目：

- BODY 最小字級
- 總字數
- 溢出（overflow）
- 安全邊界（safe margins）
- 重複構圖
- 投影片頁數
- 深色投影片比例
- 結構性強調色數量
- 缺少 intent
- 缺少 takeaway
- 已宣告的 pattern
- 已宣告的 density
- 已宣告的 energy

---

# 6.4 語意檢查（Semantic Lint）

檢查項目：

- 標題是否即為結論（takeaway）
- 該頁是否只有一個概念
- 視覺表現是否符合資訊關係
- 證據是否有詮釋
- 容器使用是否有正當理由
- 不確定性是否明確標示
- 該頁是否對整體敘事有貢獻
- 轉場是否合理

---

# 6.5 視覺檢查（Visual Lint）

渲染成圖片後檢視：

- 視覺層級
- 最先吸引注意力的元素
- 留白
- 平衡感
- 換行
- 截圖可讀性
- 圖表可讀性
- 不對稱手法的品質
- 整份簡報的節奏
- 視覺重複情形

---

# 6.6 QA 輸出格式（QA Output Schema）

每個問題都必須採用以下格式：

```yaml
slide:
layer: structural | semantic | visual | deck
severity: P0 | P1 | P2 | P3
smell:
where:
what:
why:
action:
```

範例：

```yaml
slide: 7
layer: semantic
severity: P1
smell: S02_TOPIC_TITLE
where: title
what: 標題只描述主題
why: 聽眾不知道這頁要相信什麼
action: 改成「三個合理推論都被實測推翻」
```

不允許使用模糊的評論，例如：
- 讓它更專業一點
- 增加一些視覺趣味
- 改善一致性

---

# 6.7 嚴重程度（Severity）

## P0 — Broken（損壞）

- overflow（溢出）
- clipping（裁切錯誤）
- unreadable text（文字無法閱讀）
- broken connectors（連接線斷裂）

## P1 — Communication（溝通問題）

- 沒有結論（takeaway）
- 層級混亂
- 誤導性的證據
- 隱藏的不確定性
- 令人困惑的圖表

## P2 — Composition（構圖問題）

- 密度
- 間距
- 重複性
- 平衡感不足

## P3 — Polish（潤飾）

- 細微的優化調整

---

# 6.8 整份簡報的節奏帶（Deck-Level Rhythm Strip）

每份簡報都應產出一份節奏帶：

```text
01 HERO       LOW    BOLD     M-A/M-C
02 CONTRAST   MED    FOCUSED  M-G
03 PROBLEM    MED    FOCUSED  M-A
04 PROCESS    MED    FOCUSED  M-B
05 STATEMENT  LOW    BOLD     M-F
...
```

檢查項目：

- 相同 pattern 不得連續出現超過 2 次
- 相同輪廓不得連續出現超過 2 次
- 不得連續 5 頁都沒有 BOLD
- 深色投影片超過 25% 時提出警告
- density 需有足夠變化以產生喘息空間

---

# 6.9 驗收標準（Acceptance Criteria）

最終簡報必須符合：

- 沒有 P0
- 沒有未解決的 ERROR
- BODY >= 15 pt 等效字級
- 沒有溢出
- 每頁一個概念
- 每頁一個明確的 intent
- 每頁一個 takeaway
- 每頁一個主要視覺焦點
- 相同輪廓不連續出現超過 2 次
- 沒有隱藏的不確定性
- 證據附有脈絡
- 開場與結尾前後呼應
- 截圖清晰可讀
- 圖表能快速理解
- 整份簡報節奏具有變化
- 大膽感來自尺度與構圖，而非裝飾

最終狀態：

- PASS
- REVISE

不使用數字化的品質分數。

---

# 7. GENERATION WORKFLOW（生成流程）

必要順序：

```text
Source Material
↓
Contract
↓
Narrative Spine
↓
Slide Intents
↓
Takeaways
↓
Pattern Selection
↓
Density
↓
Energy
↓
Visual Anchor
↓
Composition
↓
Generate
↓
Render
↓
Structural Lint
↓
Semantic Lint
↓
Visual Lint
↓
Rhythm Strip
↓
Revise
↓
Final Pass
```

生成（Generate）刻意被安排在流程的後段。

---

# 8. REVISION LOOP（修訂迴圈）

建議的最大迴圈次數：

## Round 1
Structure + P0/P1（結構與 P0/P1 問題）

## Round 2
Narrative + composition（敘事與構圖）

## Round 3
Polish（潤飾）

錯誤都已解決後，不要無止盡地繼續修訂。

---

# 9. SOURCE MATERIAL TRANSFORMATION RULE（來源素材轉換規則）

簡報不是把文件內容分頁呈現。

絕不將來源文件的標題直接轉為投影片。

透過以下步驟轉換來源素材：

```text
Source Fact
↓
Communication Intent
↓
Takeaway
↓
Relationship
↓
Pattern
↓
Visual Form
```

此規則優先於便利性考量。

---

# 10. CHANGELOG（變更紀錄）

## v1.2

- 重新建構為 Contract / Canon / Language / Critique 四層結構。
- 新增規則優先順序。
- 新增可機器填寫的 Contract YAML。
- 為 Canon 新增明確的 RULE / WHEN / CHECK 邏輯。
- 新增 PPTX 與 HTML 的實作對應（Implementation Mapping）。
- 將色彩 token 對齊參考簡報。
- 新增 Chrome 規則。
- 新增中文編輯排版規則。
- 新增數字修辭（Number Rhetoric）。
- 新增信心程度圖例（Confidence Legend）。
- 將參考簡報訂為標準實作範例。
- 為各 Pattern 新增 Use / Do Not Use / Motif / Density / Reference 欄位。
- 新增 QUALITY GATE、COST SPLIT、ADOPTION STEPS 三種 Pattern。
- 重新排序 Smells 為 S01–S15。
- 新增固定的 QA 輸出格式。
- 新增節奏帶（rhythm strip）。
- 減少重複的理念敘述。
- 將「大膽感」從模糊的指引轉為可於整份簡報層級衡量的警告機制。

---

# 11. FINAL DESIGN INTENT（最終設計意圖）

Eric Presentation 應該給人以下感覺：

- 有結構但不僵化
- 克制但不扁平
- 具技術感但不枯燥
- 大膽但不流於裝飾
- 編輯感十足但不為藝術而藝術
- 一致但不制式化
- 由 AI 協助完成，但清楚由人主導

當聽眾記住的是這個想法本身，而不是這份範本，這套系統就是成功的。
