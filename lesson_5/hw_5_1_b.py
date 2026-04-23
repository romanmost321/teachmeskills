"""
Author: Roman Mostyko
Date_hw: 16/04/2026
Summary: hw_5
"""

# 1. Продолжаем работать с формулами.

from math import cos, factorial

n = int(input("Enter n: "))
x = int(float("Enter x: "))

result = 0

cos_result = cos(x)

for i in range(n + 1):
    sign = pow(-1, i)
    numerator = pow(x, (2 * i))
    denominator = factorial(2 * i)
    total = sign * numerator / denominator
    result += total

print(f"cos_result: {cos_result}, result: {result}")
