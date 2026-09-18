# deck-contract

**Eric Presentation Design System v1.3** — 一套可被機器檢查（machine-checkable）的個人簡報設計標準，用於產生簡報（PPTX 或離線 HTML），讓人類與 AI 生成器都能遵循一致的設計判斷。

這個 repo 保存可跨題目重複使用的設計規格，不保存特定專案的內容母文件、參考簡報或衍生產物。

## 核心檔案

| 檔案 | 角色 | 權威範圍 |
|---|---|---|
| [`DESIGN.md`](DESIGN.md) | 設計系統規格 | 簡報的 Contract、Canon、視覺語言、Pattern 與 QA 標準 |
| [`scripts/check_repo.rb`](scripts/check_repo.rb) | 規格完整性檢查 | Canon、Pattern、Motif、Smell 編號與本地文件連結 |

`DESIGN.md` 是唯一的 canonical specification。專案可以在自己的 Contract 中指定 reference deck，但該參考只用於該專案，不會改變本 repo 的規則優先順序。

## 這是什麼

這是一套規則系統，規範在進行任何視覺設計之前，一份簡報必須先定義「什麼」（Contract），以及事後要「如何」被檢視（Critique）。目標風格是 **70% Editorial Tech／30% Strategy Deck**——清晰、克制、以敘事為導向，同時明確避免常見的通用型 SaaS 簡報樣式（icon 方格、漸層、玻璃擬態、裝飾性卡片）。

語言：以繁體中文（zh-Hant）為主，支援雙語編輯。

## 在專案中的使用方式

```text
專案內容來源 ──▶ Deck Contract ──▶ Narrative / Slide Contract ──▶ HTML 或 PPTX
                  DESIGN.md ───────設計與驗收規則────────────────▲
```

- 每個簡報專案自行維護內容來源與 Deck Contract。
- 本 repo 只回答「怎麼設計」與「怎麼驗收」，不保存「這次要講什麼」。
- 專案參考簡報只能校準視覺語言，不能覆蓋 Contract 或 Canon。
- 事實或數據變動時，應回到該專案的內容來源修改。

## 結構

規則分層組織，並有明確的優先順序（層級越高，優先權越高）：

1. **Contract（合約）**——在開始構圖前必須完成的必要元資訊（受眾、目標、核心訊息、限制條件）。
2. **Canon（準則，C01–C15）**——不可協商的規則：一頁一個核心概念、一個視覺焦點、內文最小字級、不得為了塞進內容而縮小、標題即結論等。
3. **Language（語言）**——字體排印、色彩 token、網格與間距、中文編輯排版、簽名式視覺動機（M-A–M-H）、視覺能量等級，以及數字修辭。
4. **Pattern Library（版型庫，P01–P15）**——可重複使用的溝通版型（HERO、CONTRAST、PROCESS、EVIDENCE、ARCHITECTURE、DECISION 等），各自定義使用條件、預設動機與資訊密度。
5. **Critique（審查）**——簡報「氣味」清單（S01–S15）、結構／語意／視覺三層檢查、嚴重程度分級（P0–P3），以及最終 PASS／REVISE 的驗收標準。

## 產出流程

```
Source Material → Contract → Narrative Spine → Slide Intents → Takeaways
→ Pattern Selection → Density → Energy → Visual Anchor → Composition
→ Generate → Render → Structural Lint → Semantic Lint → Visual Lint
→ Rhythm Strip → Revise → Final Pass
```

生成刻意被安排在流程後段——結構與意圖必須先確立，才能進行任何視覺設計。

## 自動檢查

執行：

```bash
ruby scripts/check_repo.rb
```

目前會檢查：

- Canon 是否完整且依序為 C01–C15。
- Pattern 是否完整且依序為 P01–P15。
- Motif 是否完整且依序為 M-A–M-H。
- Presentation Smell 是否完整且依序為 S01–S15。
- README 的本地 Markdown 連結是否存在。

這支檢查器只驗證規格本身的完整性。特定簡報的 structural、semantic 與 visual lint 應在各自專案內執行。

## 本地範例

開發規格時可以把內容母文件、參考 HTML 與內容追溯表放在工作目錄中比對，但這些檔案屬於專案素材，不提交到本 repo。

目前 `.gitignore` 已排除本地的 Playbook 母文件、參考 HTML 與其 `DECK_MAP.md`。
