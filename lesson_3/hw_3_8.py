"""
Author: Roman Mostyko
Date_hw: 07/04/2026
Summary: hw_3
"""

# 8. Дано трехзначное число, найти сумму его цифр.
# Например, дано 123 – сумма 6, дано 555, сумма 15.

num = int(input("Введите трехзначное число: "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

if len(str(num)) != 3:
    print(
        f"Введное вами число {num} не является трехзначным."
    )  # Так добавил небольшую проверку :)
else:
    print(
        f"Кол-во десятков = {hundreds}\nКол-во сотен = {tens}\nКол-во единиц = {units}\nСумма = {hundreds + tens + units}"
    )
