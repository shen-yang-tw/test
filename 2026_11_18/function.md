# Python 函式（Function）新手友善入門指南

歡迎來到 Python 的核心殿堂！如果你剛開始學寫程式，看到 `def`、`return`、`參數` 這些詞彙覺得有點抽象，請不要擔心。這份教學會用最生活化的例子，帶你輕鬆搞懂函式的本質。

---

## 一、什麼是函式？——生活中的「果汁機」比喻

想像你家裡有一台「**多功能果汁機**」：
1. **丟入水果（輸入/參數）**：你把一顆蘋果丟進去。
2. **按下按鈕（呼叫函式）**：機器開始旋轉、攪拌。
3. **倒出果汁（輸出/回傳值）**：果汁機吐出一杯新鮮蘋果汁。

在程式世界裡，**函式（Function）就是這台果汁機**。它是一段「包裝好、有特定功能」的程式碼積木。

### 為什麼一定要學會寫函式？
- **告別複製貼上（DRY 原則 - Don't Repeat Yourself）**：如果你需要打 10 次果汁，你不需要買 10 台機器，只要重複使用同一台機器就好。
- **程式乾淨好維護**：把複雜的大程式拆解成一個個小零件，哪裡壞掉就修哪裡，不會牽一髮動全身。

---

## 二、基本語法結構：定義與呼叫

在 Python 裡，打造一台機器叫做**定義（Define）**，開動機器叫做**呼叫（Call）**。

### 1. 語法結構說明

```python
def 函式名稱():
    # 這裡放函式要做的事情（記得縮排 4 個空格）
    print("機器運轉中...")
```

- `def`：Python 的關鍵字，告訴電腦「我要開始定義一個新函式了」。
- `函式名稱`：你自己取的名字，建議用有意義的英文小寫，例如 `make_juice`、`say_hello`。
- `()`：小括號，用來放傳進去的材料（參數）。即使不需要材料，括號也不能省！
- `:`：冒號，代表「接下來是函式的內部主體」，一定要有。
- **縮排（Indentation）**：冒號下一行必須縮排（通常按鍵盤的 `Tab` 或 4 個空格），Python 靠縮排來認出「哪些程式碼屬於這台機器內部」。

### 2. 動手寫第一個函式

```python
# 步驟 1：定義機器（打造果汁機）
def say_hello():
    print("哈囉！歡迎學習 Python 函式！")

# 步驟 2：呼叫機器（按下按鈕啟動它）
say_hello()
say_hello()  # 可以重複呼叫好幾次！
```

> [!TIP]
> **重要細節**：單純寫 `say_hello`（沒加小括號），就像只是看著果汁機的說明書；一定要加上小括號 `say_hello()`，機器才會真正運轉！

---

## 三、輸入材料：參數（Parameters & Arguments）

很多時候機器需要吃材料才能做事。傳進函式的材料就叫做「**參數**」。

### 1. 單一參數：客製化輸出

```python
def greet(name):
    print(f"你好，{name}！祝你有個美好的一天！")

greet("小明")  # 輸出：你好，小明！祝你有個美好的一天！
greet("小華")  # 輸出：你好，小華！祝你有個美好的一天！
```

### 2. 多個參數：用逗號 `,` 分開

```python
def add(a, b):
    total = a + b
    print(f"{a} + {b} 的總和是：{total}")

add(5, 3)    # 輸出：5 + 3 的總和是：8
add(10, 25)  # 輸出：10 + 25 的總和是：35
```

### 3. 預設值參數（Default Argument）：不用每次都給材料

有時候某些材料有「預設設定」，當使用者沒提供時，就用預設值：

```python
def order_drink(drink, sugar="半糖"):
    print(f"您點了一杯「{drink}」，甜度為「{sugar}」。")

order_drink("珍珠奶茶")          # 沒填甜度，自動使用預設值：半糖
order_drink("紅茶", sugar="無糖") # 有自訂甜度，使用指定的：無糖
```

---

## 四、初學者最大魔王關：`print()` 與 `return` 到底差在哪？

初學者最常有的疑問：「**我用 `print()` 就能看到結果了，為什麼還需要 `return`？**」

這兩者的差別是全篇最重要的概念，請記住這個比喻：

| 項目 | `print()`（在螢幕亮燈） | `return`（把成品交給你） |
| :--- | :--- | :--- |
| **比喻** | **大聲公喊話 / 電視螢幕顯示** | **外送員把披薩交到你手中** |
| **電腦角度** | 只負責把文字印在螢幕上給人看。印完就消失了，程式**無法拿它繼續做計算**。 | 函式執行完後，將計算結果**回傳交給呼叫者**，你可以存進變數繼續用！ |
| **若存進變數** | 存進去會變成 `None`（空空如也）。 | 變數會真正拿到計算後的數值。 |

### 程式碼對比示範

```python
# ❌ 只用 print：無法把結果拿去做後續運算
def add_with_print(a, b):
    print(a + b)

result1 = add_with_print(3, 5)
print("result1 的內容是：", result1)  # 螢幕會顯示 None！
# 想要算 result1 * 2 會引發 TypeError 報錯！

# ⭕ 正確使用 return：成品可以被保存並繼續運算
def add_with_return(a, b):
    return a + b

result2 = add_with_return(3, 5)
print("result2 的內容是：", result2)  # 內容是 8！
print("拿去乘以 2：", result2 * 2)     # 可以正常運算，得到 16！
```

> [!IMPORTANT]
> - 如果你的函式目的是「**計算出一個答案供後續使用**」，請務必使用 `return`！
> - 一旦函式執行到 `return`，這台機器就會**立刻停止運轉**並把結果送出，寫在 `return` 下方的程式碼都不會被執行。

---

## 五、變數的活動範圍：區域變數（Local）與全域變數（Global）

程式中的變數是有「活動範圍（Scope）」的。

- **全域變數（Global）**：寫在函式外面的變數，像公園的長椅，大家都能看得到。
- **區域變數（Local）**：寫在函式裡面的變數，像你家臥室的物品，**外面的人拿不到**。

```python
x = 100  # 全域變數，大家都可以存取

def my_func():
    y = 50  # 區域變數，只在 my_func 裡面有效
    print("函式內部讀取 y:", y)
    print("函式內部讀取 x:", x)

my_func()

print("函式外部讀取 x:", x)
# print(y)  # ❌ 這行會報錯 NameError: name 'y' is not defined！
```

---

## 六、新手最常踩的 3 個雷（踩坑指南）

### ❌ 雷區 1：呼叫函式忘了加 `()`
```python
def say_hi():
    return "Hi!"

# 錯誤示範：
print(say_hi)   # 印出 <function say_hi at 0x...>（印出函式物件本身，沒有執行它）

# 正確作法：
print(say_hi()) # 印出 Hi!
```

### ❌ 雷區 2：忘記縮排或縮排不一致
```python
def check():
print("沒縮排會出事！")  # 報錯：IndentationError
```

### ❌ 雷區 3：把程式碼寫在 `return` 後方（幽靈代碼）
```python
def calculate():
    return 10
    print("這句話永遠不會被印出來！")  # return 之後函式已結束
```

---

## 七、動手練習題（附參考答案）

請試著不看答案，自己在電腦上挑戰寫寫看！

### 題目 1：個人化打招呼
> **題目**：寫一個函式 `greet_user(name)`，接收一個名字，並回傳（return）字串 `"歡迎光臨，XXX！"`。

<details>
<summary>點我查看參考解答</summary>

```python
def greet_user(name):
    return f"歡迎光臨，{name}！"

message = greet_user("小美")
print(message)  # 輸出：歡迎光臨，小美！
```
</details>

---

### 題目 2：計算 BMI 函式
> **題目**：寫一個函式 `calc_bmi(weight, height_m)`，傳入體重（公斤）與身高（公尺），利用公式 `BMI = weight / (height_m ** 2)` 計算並回傳 BMI 數值（四捨五入到小數點後兩位）。

<details>
<summary>點我查看參考解答</summary>

```python
def calc_bmi(weight, height_m):
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

my_bmi = calc_bmi(65, 1.75)
print(f"你的 BMI 是：{my_bmi}")  # 輸出：你的 BMI 是：21.22
```
</details>

---

## 八、執行範例程式碼

本資料夾已附帶可執行的範例檔 `function_example.py`。
請開啟終端機（PowerShell 或 CMD），在專案目錄下執行以下任一指令即可體驗：

使用專案推薦的 `uv` 工具執行：
```bash
uv run python 2026_11_18/function_example.py
```

或使用虛擬環境中的 Python 執行：
```powershell
.\.venv\Scripts\python.exe 2026_11_18/function_example.py
```
（若系統全域環境已安裝 Python，亦可直接輸入 `python 2026_11_18/function_example.py`）
