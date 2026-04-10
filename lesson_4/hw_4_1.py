"""
Author: Roman Mostyko
Date_hw: 09/04/2026
Summary: hw_4
"""

# 1. Используя модуль math, вычислите значения по следующим формулам:
# Значения a, b, x ввести с клавиатуры, вывести 4 рассчитанных по формулам значения.
# Сделать красиво оформленные ввод и вывод данных.

from math import sin, cos, sqrt, cbrt

a = float(input("Введите а = "))
b = float(input("Введите b = "))
x = float(input("Введите x = "))


# print(round(pow(a, 2) / 3, 2))
# print(round((pow(a, 2) + 4) / b, 2))
# print(round((sqrt(pow(a, 2) + 4)) / 4, 2))
# print(round(sqrt(pow((pow(a, 2) + 4), 3)) / 4, 2))

print(
    f"\tTask a: y = {round((round(pow(a, 2) / 3, 2)) + (round((pow(a, 2) + 4) / b, 2)) + 
                     (round((sqrt(pow(a, 2) + 4)) / 4, 2)) + (round(sqrt(pow((pow(a, 2) + 4), 3)) / 4, 2)), 2)}"
)

print(f"\tTask b: y = {round((cos(x) + sin(x)), 2)}")

print(
    f"\tTask c: y = {round((cbrt((round((pow((cos(pow(x, 2))), 2) + pow((sin((2 * x - 1))), 2)), 2)))), 2)}"
)
print(
    f"\tTask d: y = {round(((5 * x) + ((3 * (pow(x, 2))) * sqrt(1 + (pow(sin(x), 2))))), 2)}"
)
