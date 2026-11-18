"""
Python 函式（Function）教學範例程式碼
對應教學文件：2026_11_18/function.md
"""

print("=" * 50)
print("【範例 1：最基本的定義與呼叫】")
print("=" * 50)

def say_hello():
    print("哈囉！歡迎學習 Python 函式！")

# 呼叫函式
say_hello()
say_hello()


print("\n" + "=" * 50)
print("【範例 2：帶有參數的函式】")
print("=" * 50)

def greet(name):
    print(f"你好，{name}！祝你有個美好的一天！")

greet("小明")
greet("小華")

def add(a, b):
    total = a + b
    print(f"{a} + {b} 的總和是：{total}")

add(5, 3)
add(10, 25)


print("\n" + "=" * 50)
print("【範例 3：預設參數（Default Arguments）】")
print("=" * 50)

def order_drink(drink, sugar="半糖"):
    print(f"您點了一杯「{drink}」，甜度為「{sugar}」。")

order_drink("珍珠奶茶")            # 使用預設甜度（半糖）
order_drink("四季春", sugar="無糖") # 自訂甜度（無糖）


print("\n" + "=" * 50)
print("【範例 4：print vs return 實戰差異】")
print("=" * 50)

# 示範 1: 使用 print 的函式
def add_with_print(a, b):
    print(f"[函式內部 print] {a + b}")

result1 = add_with_print(3, 5)
print(f"變數 result1 拿到的值是: {result1} (因為沒有 return，所以是 None)")

# 示範 2: 使用 return 的函式
def add_with_return(a, b):
    return a + b

result2 = add_with_return(3, 5)
print(f"變數 result2 拿到的值是: {result2} (成功拿到回傳值 8)")
print(f"拿 result2 繼續計算 (result2 * 2): {result2 * 2}")


print("\n" + "=" * 50)
print("【範例 5：區域變數（Local）與全域變數（Global）】")
print("=" * 50)

global_var = "我是全域變數（大家都能看到我）"

def test_scope():
    local_var = "我是區域變數（只活在函式裡）"
    print(f"在函式內部讀取全域變數: {global_var}")
    print(f"在函式內部讀取區域變數: {local_var}")

test_scope()
print(f"在函式外部讀取全域變數: {global_var}")
# 如果嘗試執行 print(local_var)，會出現 NameError 錯誤。


print("\n" + "=" * 50)
print("【範例 6：實戰演練 - BMI 計算器】")
print("=" * 50)

def calc_bmi(weight, height_m):
    """
    計算 BMI 並回傳數值與體位評價
    """
    bmi = round(weight / (height_m ** 2), 2)
    if bmi < 18.5:
        status = "體重過輕"
    elif bmi < 24:
        status = "正常範圍"
    else:
        status = "體重過重"
    return bmi, status

# 測試 BMI 函式
my_bmi, my_status = calc_bmi(65, 1.75)
print(f"身高 1.75m、體重 65kg 的計算結果：")
print(f"-> BMI 數值: {my_bmi}")
print(f"-> 評估結果: {my_status}")

print("\n" + "=" * 50)
print("範例執行完畢！恭喜你掌握了 Python 函式的核心觀念！")
print("=" * 50)
