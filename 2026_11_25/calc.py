"""計算機模組 (calc.py)

提供基礎的四則運算功能，包含加法、減法、乘法與除法。
"""


def add(a, b):
    """回傳 a 與 b 的加總結果。"""
    return a + b


def subtract(a, b):
    """回傳 a 減去 b 的結果。"""
    return a - b


def multiply(a, b):
    """回傳 a 與 b 的相乘結果。"""
    return a * b


def divide(a, b):
    """回傳 a 除以 b 的商。

    Args:
        a (int | float): 被除數
        b (int | float): 除數

    Raises:
        ValueError: 當除數 b 為 0 時拋出「除數不可為零」

    Returns:
        float: 除法運算結果
    """
    if b == 0:
        raise ValueError("除數不可為零")
    return a / b
