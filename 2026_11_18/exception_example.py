"""
Python 例外處理（Exception Handling）示範程式碼
對應教學文件：2026_11_18/exception_handling.md
"""

print("=" * 60)
print("【範例 1：最基礎的 try...except（防護網接住錯誤）】")
print("=" * 60)

def safe_divide_basic(a, b):
    try:
        ans = a / b
        print(f"{a} / {b} = {ans}")
    except:
        print(f"⚠️ 計算 {a} / {b} 時發生錯誤，但程式沒有當機！")

safe_divide_basic(10, 2)
safe_divide_basic(10, 0)


print("\n" + "=" * 60)
print("【範例 2：多重 except —— 指名道姓對症下藥】")
print("=" * 60)

def calculate_recipe(data_str, index):
    try:
        # 可能發生 IndexError
        items = ["蘋果", "香蕉", "奇異果"]
        picked = items[index]
        
        # 可能發生 ValueError
        num = int(data_str)
        
        # 可能發生 ZeroDivisionError
        ratio = 100 / num
        
        print(f"成功取出【{picked}】，每份比例為: {ratio:.2f}")

    except IndexError:
        print(f"❌ 索引錯誤：找不到第 {index} 個水果！")
    except ValueError:
        print(f"❌ 數值錯誤：無法把 '{data_str}' 轉換成整數！")
    except ZeroDivisionError:
        print("❌ 數學錯誤：除數不能為 0！")
    except Exception as e:
        print(f"❌ 未預期的錯誤：{e}")

# 正常運行
calculate_recipe("2", 1)
# 觸發 IndexError
calculate_recipe("2", 10)
# 觸發 ValueError
calculate_recipe("無效字串", 0)
# 觸發 ZeroDivisionError
calculate_recipe("0", 0)


print("\n" + "=" * 60)
print("【範例 3：四部曲全家福 try...except...else...finally】")
print("=" * 60)

def test_full_flow(dividend, divisor):
    print(f"\n--- 開始執行除法：{dividend} / {divisor} ---")
    try:
        result = dividend / divisor
    except ZeroDivisionError as e:
        print(f"【except 救援區】抓到除以零錯誤！系統訊息: {e}")
    else:
        print(f"【else 成功區】計算完全無誤！結果為: {result}")
    finally:
        print("【finally 收尾區】不管成不成功，我都一定會執行（清理現場、關閉資源）！")

test_full_flow(20, 4)  # 成功案例：走 try -> else -> finally
test_full_flow(20, 0)  # 失敗案例：走 try -> except -> finally


print("\n" + "=" * 60)
print("【範例 4：主動報警 —— 使用 raise 拋出例外】")
print("=" * 60)

def set_user_age(name, age):
    if not isinstance(age, int):
        raise TypeError(f"年齡必須是整數，但傳入了 {type(age).__name__}！")
    if age < 0 or age > 150:
        raise ValueError(f"年齡 {age} 不在合理的生存範圍內 (0 ~ 150)！")
    
    print(f"✅ 使用者 {name} 的年齡設定成功：{age} 歲")

# 正常情境
try:
    set_user_age("小明", 25)
except (TypeError, ValueError) as err:
    print(f"設定失敗: {err}")

# 不合理情境 1：年齡為負數
try:
    set_user_age("阿飄", -10)
except (TypeError, ValueError) as err:
    print(f"設定失敗: {err}")

# 不合理情境 2：傳入字串型別
try:
    set_user_age("小美", "十八歲")
except (TypeError, ValueError) as err:
    print(f"設定失敗: {err}")


print("\n" + "=" * 60)
print("【範例 5：實戰模擬 —— 模擬安全的輸入檢驗防呆】")
print("=" * 60)

def mock_safe_input(simulated_inputs):
    """
    模擬使用者多次輸入直到輸入正確的過程
    """
    print("模擬使用者輸入驗證流程：")
    for user_input in simulated_inputs:
        print(f"使用者輸入了: '{user_input}'")
        try:
            val = int(user_input)
            print(f"🎉 驗證成功！取得合法數字: {val}\n")
            return val
        except ValueError:
            print("⚠️ 格式錯誤！請輸入純整數，繼續等待下一次輸入...\n")

# 模擬使用者前兩次亂打，第三次才打對
mock_safe_input(["hello", "12.34", "99"])

print("=" * 60)
print("所有例外處理範例演示完成！")
print("=" * 60)
