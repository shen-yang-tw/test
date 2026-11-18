"""
Python 函式參數與引數傳遞範例程式
對應教學文件：2026_11_18/function_manual.md 與 2026_11_18/function.ipynb
"""

print("=" * 60)
print("【單元 1：參數 (parameter) vs 引數 (argument)】")
print("=" * 60)

# name 是參數（定義時的佔位欄位）
def greet(name):
    print(f"Hello, {name}!")

# "Alice" 是引數（呼叫時實際傳入的值）
greet("Alice")


print("\n" + "=" * 60)
print("【單元 2：位置引數 vs 關鍵字引數】")
print("=" * 60)

def pet(animal, name):
    print(f"我養了一隻{animal}，它叫{name}。")

# 1. 位置引數 (依順序)
pet("狗", "小白")

# 2. 關鍵字引數 (指名道姓，順序可顛倒)
pet(animal="貓", name="小黑")
pet(name="小黑", animal="貓")


print("\n" + "=" * 60)
print("【單元 3：混用規則（位置引數必須在關鍵字引數前面）】")
print("=" * 60)

# 正確示範：位置引數在前，關鍵字引數在後
pet("狗", name="小白")


print("\n" + "=" * 60)
print("【單元 4：預設值參數 (Default Arguments)】")
print("=" * 60)

def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"點餐：{drink} {ice} / {sugar}")

order_drink("珍珠奶茶")              # 使用預設值
order_drink("綠茶", ice="少冰")       # 指定冰量
order_drink("紅茶", sugar="無糖")     # 指定糖分


print("\n" + "=" * 60)
print("【單元 5：特殊限制符號 / 與 *】")
print("=" * 60)

# id 只能用位置引數 (/ 前面)
# name 可用位置或關鍵字引數 (/ 與 * 之間)
# email 只能用關鍵字引數 (* 後面)
def register(id, /, name, *, email):
    print(f"註冊成功！ID: {id}, 姓名: {name}, 電子郵件: {email}")

register(123, "Alice", email="alice@example.com")
register(123, name="Bob", email="bob@example.com")


print("\n" + "=" * 60)
print("【單元 6：任意數量的位置引數 (*args)】")
print("=" * 60)

def sum_squares(*numbers):
    print(f"接收到的 numbers 型別為: {type(numbers)}，內容為: {numbers}")
    total = sum(x ** 2 for x in numbers)
    return total

result = sum_squares(1, 2, 3, 4)
print(f"平方和計算結果: {result}")


print("\n" + "=" * 60)
print("【單元 7：任意數量的關鍵字引數 (**kwargs)】")
print("=" * 60)

def build_profile(name, age, **info):
    print(f"接收到的 info 型別為: {type(info)}，內容為: {info}")
    profile = {
        "name": name,
        "age": age
    }
    profile.update(info)
    return profile

user_profile = build_profile("Alice", 30, location="New York", profession="Engineer")
print("建立的使用者檔案:", user_profile)

print("\n" + "=" * 60)
print("所有單元演示完畢！")
print("=" * 60)
