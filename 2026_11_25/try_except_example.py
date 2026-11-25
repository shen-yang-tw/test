"""Python try ~ except 例外處理：由淺至深示範程式

對應教學文件：2026_11_25/try_except_guide.md
執行方式：uv run python 2026_11_25/try_except_example.py
"""

from calc import divide


def print_section(title):
    """印出清楚的章節分隔線，方便課堂演示觀察輸出"""
    print("\n" + "=" * 60)
    print(f"【{title}】")
    print("=" * 60)


# ==============================================================================
# 第一階（初探）：最基礎的 try ~ except 防護網
# ==============================================================================
print_section("第一階：最基礎的 try ~ except 安全防護網")

try:
    print("嘗試將字串 'abc' 轉換成整數...")
    number = int("abc")
    print(f"轉換結果：{number}")
except ValueError:
    print("⚠️ 捕捉到錯誤：'abc' 不是合法的整數，但程式沒有當機！")

print("👉 程式繼續往下執行。")


# ==============================================================================
# 第二階（入門）：指名道姓捕捉多重例外與讀取錯誤訊息 (as e)
# ==============================================================================
print_section("第二階：多重 except 與 as e 取得錯誤詳情")


def parse_and_divide(text_num, divisor):
    """示範同時防範轉型失敗與除以零"""
    try:
        value = int(text_num)
        result = value / divisor
        print(f"✅ 計算成功：{value} / {divisor} = {result}")
    except ValueError as e:
        print(f"❌ 數值轉換失敗（{e}）：請確認輸入為整數！")
    except ZeroDivisionError:
        print("❌ 數學錯誤：除數不可為 0！")
    except TypeError as e:
        print(f"❌ 型別錯誤（{e}）：請傳入正確的資料型別！")


parse_and_divide("10", 2)
parse_and_divide("hello", 2)
parse_and_divide("10", 0)


# ==============================================================================
# 第三階（進階）：完整生命週期 try ~ except ~ else ~ finally
# ==============================================================================
print_section("第三階：try ~ except ~ else ~ finally 餐廳結帳比喻")


def checkout(balance, cost):
    """示範成功與失敗時，else 與 finally 的執行差異"""
    print(f"\n--- 準備結帳：餘額 {balance} 元，消費 {cost} 元 ---")
    try:
        if cost < 0:
            raise ValueError("消費金額不可為負數")
        if balance < cost:
            raise RuntimeError("帳戶餘額不足")
        remaining = balance - cost
    except (ValueError, RuntimeError) as e:
        print(f"⚠️ 結帳失敗：{e}")
    else:
        # 只有 try 完全順利執行、沒有任何例外時才會執行
        print(f"✅ 結帳成功！剩餘餘額：{remaining} 元，贈送甜點一份！")
    finally:
        # 無論成功或失敗，最後一定都會執行收尾動作
        print("🧾 [finally] 列印交易紀錄並關閉收銀台。")


checkout(500, 200)  # 成功：try -> else -> finally
checkout(100, 300)  # 失敗：try -> except -> finally


# ==============================================================================
# 第四階（實戰）：主動拋出 raise 與呼叫堆疊（Call Stack）傳遞
# ==============================================================================
print_section("第四階：結合 calc.py 主動 raise 與例外傳遞")


def calculate_average(total, count):
    """中繼函式不處理錯誤，直接將 calc.divide() 的例外往外傳遞"""
    return divide(total, count)


for count in (4, 0):
    try:
        avg = calculate_average(100, count)
        print(f"✅ 總分 100 分給 {count} 人，平均為：{avg}")
    except ValueError as e:
        # 接住來自 calc.divide() 主動拋出的 ValueError("除數不可為零")
        print(f"⚠️ 主程式攔截到 calc.divide() 的例外：{e}")


# ==============================================================================
# 第五階（高階）：自訂例外類別與例外鏈 (raise ... from e)
# ==============================================================================
print_section("第五階：自訂例外類別與例外鏈")


class InsufficientBalanceError(Exception):
    """自訂例外：當帳戶餘額不足時拋出"""


class ConfigLoadError(Exception):
    """自訂例外：當設定值解析失敗時拋出"""


def withdraw(balance, amount):
    """示範拋出語意明確的自訂例外"""
    if amount > balance:
        raise InsufficientBalanceError(
            f"提款失敗：想領 {amount} 元，但餘額僅剩 {balance} 元"
        )
    return balance - amount


def load_port(raw_text):
    """示範使用 raise ... from e 保留原始例外線索"""
    try:
        return int(raw_text)
    except ValueError as e:
        raise ConfigLoadError(f"無法解析連接埠設定：'{raw_text}'") from e


try:
    withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print(f"🏦 攔截到自訂例外：{e}")

try:
    load_port("not_a_port")
except ConfigLoadError as e:
    print(f"⚙️ 攔截到設定載入例外：{e}")
    print(f"   └─ 原始觸發原因 (__cause__)：{type(e.__cause__).__name__}: {e.__cause__}")


# ==============================================================================
# 第六階（最佳實踐）：EAFP 風格示範
# ==============================================================================
print_section("第六階：Pythonic 的 EAFP 風格")

user_profile = {"name": "小明", "role": "學員"}

# EAFP (Easier to Ask for Forgiveness than Permission)：
# 直接嘗試讀取，若鍵值不存在再由 except 處理預設值
try:
    nickname = user_profile["nickname"]
except KeyError:
    nickname = "未設定暱稱"

print(f"學員 {user_profile['name']} 的暱稱：{nickname}")
print("\n🎉 所有階段示範執行完畢！")
