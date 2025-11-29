"""
Unit tests for calculator module.
"""

import sys
import os

# Add parent directory to path to import calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, calculate_expr, subtract, multiply, divide, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5


def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(2, 10) == 1024

def test_calculate_expr():
    assert calculate_expr("2 + 3") == 5
    assert calculate_expr("5 - 2") == 3
    assert calculate_expr("4 * 2") == 8
    assert calculate_expr("8 / 4") == 2
    assert calculate_expr("3 ^ 3") == 27


if __name__ == "__main__":
    print("Running tests...")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_power()
    test_calculate_expr()
    print("All tests passed!")

