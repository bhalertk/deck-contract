# Golden Deck

Golden Deck 是一組固定的測試素材，用來回答一個問題：DESIGN.md 改版後，產出的簡報有沒有真的變好？

規格檢查（`check_repo.py`）通過，只代表規格的格式正確，不代表簡報品質提升。只有用同樣的素材重新產生簡報、比較結果，才能知道規則是否有效。

所有素材都是虛構的，用途是測試規則，不是專案內容。

## 三個案例

| 案例 | Voice | 主要測試的規則 |
|---|---|---|
| [project-report](project-report/) | project-report | 數據證據與量測口徑（C12、1.4）、判斷與取捨（3.13） |
| [technical-review](technical-review/) | technical-review | 架構圖與依賴關係（P06、P07）、節奏覆蓋（C14）、客觀語氣 |
| [education](education/) | education | 循序說明、避免誇大、自然的 Voice |

每個案例包含：

- `source.md`：原始素材，產生簡報時唯一可以使用的事實來源。
- `contract.yaml`：Deck Contract 與 Slide Contract。
- `outputs/`：各版本產生的簡報，檔名為版本號，例如 `v1.5.html`。產生器撰寫的 Slide Contract 放在同名的 `v1.5.slides.yaml`，用來人工比對證據對應。

## 每一輪測試的步驟

1. 以目前版本的 DESIGN.md，只根據 `source.md` 與 `contract.yaml` 產生簡報。
2. 存成 `outputs/<版本>.html`。
3. 執行文字檢查：

   ```bash
   python scripts/check_deck.py golden/<案例>/outputs/<版本>.html --contract golden/<案例>/contract.yaml
   ```

4. 人工檢查 check_deck 標示為 NOT CHECKED 的項目，包括字級、溢出、證據對應與視覺焦點。
5. 修改到可以使用為止，並記錄每一次修改的類型。產生器自己發現的修改與使用者審查後的修改分開記錄。
6. 在 [LOG.md](LOG.md) 新增一列。

## 判斷是否進步

比較的重點不是 AI 給的分數，而是：

- 是否出現錯誤的數字或誤導的結論？
- 人工修改的次數與類型，是否比上一版少？
- 三個案例之間，是否保留了符合情境的差異？

如果新版本更符合所有規則，卻需要花更多時間修改，那就不算進步。

## 修改素材的規則

`source.md` 與 `contract.yaml` 一旦開始用於比較，就不應修改。若必須修改，在 LOG.md 註明，並把修改前後的結果視為不同的基準。
