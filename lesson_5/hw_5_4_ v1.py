"""
Author: Roman Mostyko
Date_hw: 16/04/2026
Summary: hw_5
"""

# 4. Дан список чисел. Реализовать программу, которая посчитает сумму всех чисел в списке, а также найдет
# минимальный и максимальный элементы.

# Variant_1_с использование range

# nums = int(input("Введите сколько необходимо сгенерировать числе: "))

# total = 0
# min_num = min(range(1, nums + 1))
# max_num = max(range(1, nums + 1))

# for num in range(1, nums + 1):
#     total += num

# print(f"Сумма всех сгенерированных чисел = {total}")
# print(f"Минимальное число = {min_num}")
# print(f"Максимальное число = {max_num}")

# Variant_2_генерируем рандомную последовательность

# import random

# count_nums = int(input("Сколько числе хотите сгенерировать: "))
# start_nums = int(
#     input(
#         "Сейчас мы сгенерируем список чисел. Введите от какого числа необходимо сгенерировать список: "
#     )
# )
# end_nums = int(input("Введите до какого числа необходимо сгенерировать список: "))


# list_nums = []  # Генерируем список чисел
# for list_num in range(count_nums):
#     list_nums.append(random.randint(start_nums, end_nums))

# print(f"Сгенерированный список чисел: {list_nums}")


# total = 0
# min_num = min(list_nums)
# max_num = max(list_nums)

# for num in list_nums:
#     total += num

# print(f"Сумма всех сгенерированных чисел = {total}")
# print(f"Минимальное число = {min_num}")
# print(f"Максимальное число = {max_num}")

# Variant_3_без использования min и max

import random

count_nums = int(input("Сколько числе хотите сгенерировать: "))
start_nums = int(
    input(
        "Сейчас мы сгенерируем список чисел. Введите от какого числа необходимо сгенерировать список: "
    )
)
end_nums = int(input("Введите до какого числа необходимо сгенерировать список: "))


list_nums = []  # Генерируем список чисел
for list_num in range(count_nums):
    list_nums.append(random.randint(start_nums, end_nums))

print(f"Сгенерированный список чисел: {list_nums}")


total = 0
min_num = 0
max_num = 0

for num in list_nums:
    total += num
    if max_num < num:
        max_num = num

print(f"Сумма всех сгенерированных чисел = {total}")
print(f"Минимальное число = {min_num}")
print(f"Максимальное число = {max_num}")
