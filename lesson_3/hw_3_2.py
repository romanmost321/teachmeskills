"""
Author: Roman Mostyko
Date_hw: 07/04/2026
Summary: hw_3
"""

# 2. Дан прямоугольный треугольник с катетами cat_a и
# cat_b. Найти площадь треугольника и его гипотенузу.

import math

cat_a = float(input("Укажите значение первого катета: "))
cat_b = float(input("Укажите значение второго катета: "))

c = print(
    f"Гипотенуза треугольника = {round((math.sqrt((pow(cat_a, 2) + pow(cat_b, 2)))), 2)}"
)

S = print(f"Площать треугольника = {(cat_a * cat_b) / 2}")
