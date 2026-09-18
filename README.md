# deck-contract

**Eric Presentation Design System v1.2** — 一套可被機器檢查（machine-checkable）的簡報設計系統規範，用於產生簡報（PPTX 或離線 HTML），設計上讓人類與 AI 生成器都能遵循。

完整規範請見：[DESIGN.md](DESIGN.md)

## 這是什麼

這是一套規則系統，規範在進行任何視覺設計之前，一份簡報必須先定義「什麼」（Contract），以及事後要「如何」被檢視（Critique）。目標風格是 **70% Editorial Tech／30% Strategy Deck**——清晰、克制、以敘事為導向，同時明確避免常見的通用型 SaaS 簡報樣式（icon 方格、漸層、玻璃擬態、裝飾性卡片）。

語言：以繁體中文（zh-Hant）為主，支援雙語編輯。

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

## 參考實作

`AI_Playbook_DesignSystem_v1.1.html` 是本系統的標準參考簡報，當某條規則存在多種合理的視覺詮釋時，以此參考簡報校準比例、非對稱性、留白與節奏。
