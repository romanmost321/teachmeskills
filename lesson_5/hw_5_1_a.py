"""
Author: Roman Mostyko
Date_hw: 16/04/2026
Summary: hw_5
"""

# 1. Продолжаем работать с формулами.
# Используя модуль math, вычислите значения по следующим
# формулам:

import math

n = int(input("Enter n: "))
x = int(float("Enter x: "))

result = 0

sin_result = math.sin(x)

for i in range(n + 1):
    sign = pow(-1, i)
    numerator = pow(x, (2 * i + 1))
    denominator = math.factorial(2 * i + 1)
    total = sign * numerator / denominator
    result += total

print(f"sin_result: {sin_result}, result: {result}")
