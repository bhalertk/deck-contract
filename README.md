# deck-contract

**Eric Presentation Design System v1.5** — 一套可被機器檢查（machine-checkable）的個人簡報設計標準，用於產生簡報（PPTX 或離線 HTML），讓人類與 AI 生成器都能遵循一致的設計判斷。

這個 repo 保存可跨題目重複使用的設計規格，不保存特定專案的內容母文件、參考簡報或衍生產物。`golden/` 中的測試素材都是虛構的，用途是驗證規則，不是專案內容。

## 核心檔案

| 檔案 | 角色 | 權威範圍 |
|---|---|---|
| [`DESIGN.md`](DESIGN.md) | 設計系統規格 | 簡報的 Contract、Canon、視覺語言、Pattern 與 QA 標準 |
| [`scripts/check_repo.py`](scripts/check_repo.py) | 規格完整性檢查 | Canon、Pattern、Motif、Smell 編號與欄位、ID 引用、CHANGELOG 與本地文件連結 |
| [`scripts/check_deck.py`](scripts/check_deck.py) | HTML 簡報檢查 | 每頁文字單位、頁數、BOLD 節奏、禁用詞、emoji、絕對用語、外部資源、深色模式、明體字型 |
| [`golden/README.md`](golden/README.md) | Golden Deck 測試素材 | 用固定素材比較各版本的產出，確認改版是否真的進步 |

`DESIGN.md` 是唯一的 canonical specification。專案可以在自己的 Contract 中指定 reference deck，但該參考只用於該專案，不會改變本 repo 的規則優先順序。

## 這是什麼

這是一套規則系統，規範在進行任何視覺設計之前，一份簡報必須先定義「什麼」（Contract），以及事後要「如何」被檢視（Critique）。目標風格是 **70% Editorial Tech／30% Strategy Deck**——清晰、克制、以敘事為導向，同時明確避免常見的通用型 SaaS 簡報樣式（icon 方格、漸層、玻璃擬態、裝飾性卡片）。

語言：以繁體中文（zh-Hant）為主，支援雙語編輯。

HTML 簡報以「不能上網的電腦」為前提：一份簡報就是一個檔案，不載入任何外部資源，只使用 Windows 與 macOS 內建的系統字型（微軟正黑體、蘋方），並固定使用淺色主題。

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

1. **Contract（合約）**——在開始構圖前必須完成的必要元資訊（受眾、目標、核心訊息、限制條件、語氣），以及每個數字的證據來源。
2. **Canon（準則，C01–C15）**——分為品質底線與設計約束。品質底線（C03 最小字級、C13 誠實）不得被覆蓋；設計約束可由 Contract 寫明理由後覆蓋。
3. **Language（語言）**——字體排印、色彩 token、網格與間距、中文編輯排版、簽名式視覺動機（M-A–M-H）、視覺能量等級、數字修辭，以及語氣（Voice）。
4. **Pattern Library（版型庫，P01–P15）**——可重複使用的溝通版型（HERO、CONTRAST、PROCESS、EVIDENCE、ARCHITECTURE、DECISION 等），各自定義使用條件、預設動機與資訊密度。
5. **Critique（審查）**——簡報「氣味」清單（S01–S15）、結構／語意／視覺三層檢查、嚴重程度分級（P0–P3），以及最終 PASS／REVISE 的驗收標準。

## 產出流程

```
Source Material → Contract → Narrative Spine → Slide Intents → Takeaways
→ Evidence Mapping → Pattern Selection → Motif Selection → Density → Energy
→ Visual Anchor → Composition → Generate → Render → Structural Lint
→ Semantic Lint → Visual Lint → Rhythm Strip → Revise → Final Pass
```

生成刻意被安排在流程後段——結構與意圖必須先確立，才能進行任何視覺設計。

## 自動檢查

兩支檢查器都只使用 Python 3 標準函式庫，不需額外安裝套件。兩者的 PASS 意義不同，不應混為一談。

### 規格檢查

```bash
python scripts/check_repo.py
```

確認 DESIGN.md 本身的格式正確：

- Canon 是否完整且依序為 C01–C15，每條都有 RULE、WHEN、CHECK、SEVERITY 且內容不為空，SEVERITY 須標明 ERROR 或 WARNING。
- Pattern 是否完整且依序為 P01–P15，每個都有 Use when、Do not use when、Default motif、Density 且內容不為空，Density 須為 LOW、MEDIUM 或 HIGH。
- Motif 是否完整且依序為 M-A–M-H。
- Presentation Smell 是否完整且依序為 S01–S15，且每條都有觸發條件。
- DESIGN.md 與 README 中引用的 C／P／S／M 編號都必須存在。
- README 與 DESIGN.md 的版本號一致，且 CHANGELOG 最新一筆與標題版本相同。
- 3.13 的禁用詞清單可被 `check_deck.py` 讀取。
- README 與 DESIGN.md 的本地 Markdown 連結是否存在。

通過只代表規格格式正確，不代表產出的簡報品質好。

### HTML 簡報檢查

```bash
python scripts/check_deck.py path/to/deck.html --contract path/to/contract.yaml
```

簡報的標記方式：

- 每一頁是 class 含有 `slide` 的元素。
- 可選的屬性：`data-density`（LOW、MEDIUM、HIGH）、`data-energy`（CALM、FOCUSED、BOLD）、`data-energy-override`（偏離 C14 節奏的理由）。
- 上緣標籤、頁尾等 Chrome 元素加上 `data-chrome`，不計入文字單位。

會檢查：

- C10：每頁文字單位不超過 120，並對照 Density 的建議區間。
- Contract：頁數不超過 `slide_count_max`。
- C14：連續 5 頁沒有 BOLD，且沒有寫明理由。
- 3.13：禁用詞、預告句、破折號。
- 3.11 與 C13：emoji，以及需要樣本支持的絕對用語。
- 3.5：載入外部資源（線上字型、CDN、外部圖片）為 ERROR；跟隨系統深色模式為 WARNING。
- 3.2：字型清單中出現明體或襯線字型。

字級、溢出、安全邊界、對比、強調色數量與證據對應需要渲染後的畫面或人工審查，檢查器會列為 NOT CHECKED。

## Golden Deck

[`golden/`](golden/README.md) 保存三個固定的測試案例：專案成果報告、技術架構審查、教育訓練。每次修改 DESIGN.md 後，用同樣的素材重新產生簡報，執行檢查，並在 [`golden/LOG.md`](golden/LOG.md) 記錄人工修改的次數與類型。

## 本地範例

開發規格時可以把內容母文件、參考 HTML 與內容追溯表放在工作目錄中比對，但這些檔案屬於專案素材，不提交到本 repo。

目前 `.gitignore` 已排除本地的 Playbook 母文件、參考 HTML 與其 `DECK_MAP.md`。
