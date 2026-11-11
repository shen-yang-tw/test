# Python 檔案操作入門

Python 可以讀取文字檔，也可以建立、覆寫或追加檔案內容。建議使用 `with open(...)` 開啟檔案：離開 `with` 區塊後，檔案會自動關閉。

## 讀取文字檔

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

- `"sample.txt"` 是檔案名稱或路徑。
- `"r"` 表示讀取；這是 `open` 的預設模式。
- `encoding="utf-8"` 可正確處理大多數中文文字檔。
- `read()` 會一次讀取全部內容，並以字串回傳。

其他常見讀法：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()  # 讀取一行

with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:             # 逐行讀取，適合較大的檔案
        print(line, end="")
```

`readlines()` 也能讀取所有行，但會將每一行放進串列；檔案很大時，逐行讀取通常較省記憶體。

## 寫入與追加

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("這是第一行\n")
    file.write("這是第二行\n")
```

常見檔案模式：

| 模式 | 用途 | 注意事項 |
| --- | --- | --- |
| `"r"` | 讀取 | 檔案必須已存在 |
| `"w"` | 寫入 | 檔案不存在時會建立；若已存在，原有內容會被清空 |
| `"a"` | 追加 | 寫入到檔案結尾；檔案不存在時會建立 |

追加內容的例子：

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("這行會加在檔案最後。\n")
```

使用 `"w"` 前請確認不會需要舊內容。若只想讀取，不要使用 `"w"`。

## 路徑與常見錯誤

相對路徑（例如 `"sample.txt"`）是以程式執行時的目前工作目錄為基準，不一定是 Python 程式所在的目錄。下面的範例使用 `Path(__file__).parent`，因此會在範例程式所在的資料夾尋找檔案。

如果讀取的檔案不存在，Python 會發生 `FileNotFoundError`。請檢查檔名和路徑；文字檔也建議明確指定編碼。

## 執行範例

本資料夾包含：

- `sample.txt`：供程式讀取的範例文字。
- `readfile_example.py`：讀取 `sample.txt`，並示範寫入及追加 `output.txt`。

在終端機切換到此資料夾後執行：

```bash
python readfile_example.py
```

也可以從其他目錄執行，只要提供 Python 範例程式的完整路徑。執行後會在範例程式所在的資料夾建立或更新 `output.txt`；這是 `"w"` 模式的效果。
