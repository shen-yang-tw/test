# 1. 安裝uv
```macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```Windows（PowerShell）
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# 2. 初始化新專案 (uv init)
```bash
# 建立全新專案資料夾並切換進去
uv init my-project
cd my-project

# 或：在現有目錄就地初始化（建立 pyproject.toml）
# --no-package建立平面化的版本(建議)
uv init --no-package
```

# 3. 啟動venv
```bash
source .venv/Scripts/activate
```

# 4. 關閉venv
```bash
deactivate
```

# 5. 安裝 JupyterLab

## 步驟 1：安裝 LSP 介面與 Basedpyright（會自動連帶安裝 JupyterLab）
```bash
uv add --dev jupyterlab-lsp basedpyright
```

## 步驟 2：啟動 JupyterLab
安裝完成後，使用 uv run 啟動：
```bash
uv run jupyter lab
```
執行後，系統會自動在瀏覽器中開啟 http://localhost:8888/lab 介面。

## 在虛擬環境執行某檔案
安裝完成後，使用 uv run 啟動：
```bash
uv run 路徑檔名
```
