# AGENTS.md：給 AI 助理的簡報製作手冊

這份手冊寫給被要求「讀 deck-contract 幫我做簡報」的 AI 助理，例如 GitHub Copilot 或 Claude Code。請從頭到尾照著做，不要只參考風格。

## 名詞

- **deck-contract**：本 repo，存放設計規則、範本與檢查工具。
- **簡報資料夾**：使用者在編輯器中開啟、放有簡報素材的資料夾。所有產出都放在這裡。

## 三條禁止事項

1. **不得寫入 deck-contract。** 本 repo 是公開的。簡報、Contract、素材與任何公司資料，只能存放在簡報資料夾。不要 commit 或 push deck-contract。
2. **不得使用外部資源。** 簡報要在不能上網的電腦播放：不使用線上字型、CDN 程式庫或外部圖片（DESIGN.md 3.5）。
3. **事實只能來自素材。** 數字、事件、名稱與結論，都必須能在簡報資料夾的素材中找到。素材沒有的內容不要補上；需要時問使用者。

## 步驟

### 1. 讀取素材

讀取簡報資料夾中的所有素材。列出你找到的檔案，並摘要其中的事實、數字與已有的結論。

### 2. 建立 Deck Contract

依 DESIGN.md 1.1 的格式，在簡報資料夾建立 `contract.yaml`，並加上一行 `design_system: v1.6`。

DESIGN.md 1.2 規定下列欄位缺一不可，否則不得開始構圖：

- `audience`
- `goal.type`、`goal.outcome`
- `core_message`
- `constraints.slide_count_max`
- `constraints.technical_depth`

素材中找不到的欄位，**停下來問使用者**，不要自己猜。另外依 DESIGN.md 3.13 選定 `voice`（project-report、technical-review、education），不確定時一併詢問。

格式可參考 deck-contract 的 `golden/*/contract.yaml`。

### 3. 讀取規格

DESIGN.md 很長，至少完整讀完以下章節，再開始製作：

| 章節 | 內容 |
|---|---|
| 0 | 規則優先順序 |
| 1.1–1.4 | Deck、Narrative、Slide、Evidence Contract |
| 2 | Canon C01–C15，以及品質底線與設計約束的區別 |
| 3.2、3.3 | 字型（只用系統字型）、中文排版 CT01–CT06 |
| 3.5、3.7 | HTML 單檔原則、簡報模式與換頁 |
| 3.11、3.13 | 信心狀態的文字標示、語氣與禁用詞 |
| 4 | 視覺化優先，以及 P01–P15 版型 |
| 6.1、6.5、6.9 | 簡報氣味、視覺檢查、驗收標準 |

### 4. 寫 Slide Contract

在簡報資料夾建立 `slides.yaml`。依 DESIGN.md 1.3、1.4 的格式，為每一頁寫出 `intent`、`takeaway`、`pattern`、`density`、`energy`、`motif` 與 `evidence`。

- 寫不出 `intent` 或 `takeaway` 的頁面，刪除或重新設計。
- 投影片上每個數字都要對應一筆 `evidence`，包含來源、計算方式、量測口徑與信心狀態。
- `motif` 與版型的 Default motif 不同時，在 `visual_rationale` 寫明理由。

格式可參考 deck-contract 的 `golden/*/outputs/*.slides.yaml`。

### 5. 製作簡報

把 deck-contract 的 `templates/deck.html` 複製到簡報資料夾，命名為 `deck.html`，再修改投影片內容。

- **不要重寫範本的樣式與換頁程式**（標記為 `deck-runtime` 的區塊）。可以新增投影片專用的樣式。
- 每頁是 `<section class="slide">`，並加上 `data-density` 與 `data-energy`；上緣標籤與頁尾加上 `data-chrome`。
- 有結構的資訊用表格、時間軸、架構圖、因果流程圖或路線圖呈現（DESIGN.md 第 4 節「視覺化優先」）。圖表使用 inline SVG。
- 每頁不超過 120 個文字單位（C10），計算方式見 DESIGN.md C10。
- 每頁構圖要有變化，不要每頁都是「標題在上、內容在下」（C09）。
- 標題寫成結論（C05），未驗證的內容依 3.11 以文字標示（C13）。

可參考 deck-contract 的 `golden/technical-review/outputs/v1.5-r2.html`，這是目前被使用者認可的畫面。

### 6. 檢查

**有 Python 時**，在簡報資料夾執行：

```bash
python <deck-contract 的路徑>/scripts/check_deck.py deck.html --contract contract.yaml
```

有 ERROR 必須修正；WARNING 要逐一判斷並向使用者說明。

**沒有 Python 時**，逐項人工確認：

- [ ] 每頁文字單位不超過 120
- [ ] 頁數不超過 `slide_count_max`
- [ ] 沒有 `http://`、`https://` 開頭的外部資源，也沒有 `@import`
- [ ] 沒有 `prefers-color-scheme`
- [ ] 字型清單沒有新細明體或任何明體、襯線字型
- [ ] 沒有 3.13 的禁用詞、預告句、破折號與 emoji
- [ ] 缺少樣本支持的絕對用語（例如「都能」「完全」）都已改寫
- [ ] 檔案保留了 `deck-runtime` 換頁程式
- [ ] 投影片上每個數字都能在 `slides.yaml` 的 `evidence` 找到

不論有沒有 Python，下列項目都需要在瀏覽器實際打開才能確認：字級是否看得清楚、有沒有文字溢出、標題斷行、每頁的視覺焦點。

### 7. 回報

完成後告訴使用者：

1. 產出的檔案：`contract.yaml`、`slides.yaml`、`deck.html`。
2. 檢查結果：ERROR 與 WARNING 的數量，以及每個 WARNING 的處理方式。
3. 你沒有辦法確認、需要使用者親自檢查的項目。
4. 素材中缺少、因此沒有放進簡報的內容。

播放方式：用瀏覽器開啟 `deck.html`，方向鍵或空白鍵換頁，F 全螢幕，O 切換總覽模式。
