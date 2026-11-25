"""計算機模組單元測試 (tests/test_calc.py)

使用 Python 內建的 unittest 模組驗證 calc.py 的各項運算功能。
"""

import unittest
from calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):
    """測試 calc.py 的四則運算函式"""

    def test_add(self):
        """測試加法運算"""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """測試減法運算"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 5), -4)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        """測試乘法運算"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """測試正常除法運算"""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3)

    def test_divide_by_zero(self):
        """測試除數為零時拋出 ValueError("除數不可為零")"""
        # 使用 assertRaises 搭配 context manager 驗證是否拋出 ValueError
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        
        # 驗證拋出的例外訊息是否完全符合「除數不可為零」
        self.assertEqual(str(context.exception), "除數不可為零")

        # 同時也可測試小數或負數除以 0 的情境
        with self.assertRaises(ValueError) as context:
            divide(-5.5, 0)
        self.assertEqual(str(context.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
