"""
Author: Roman Mostyko
Date_hw: 16/04/2026
Summary: hw_5
"""

# 5. Дан список чисел. Реализовать программу, которая
# проверит, все ли числа в списке уникальны (встречаются
# только один раз). Программа должна вывести результат
# проверки, и, если не все элементы уникальны, вывести
# дублирующиеся элементы и количество их повторений в
# списке

nums_list = [1, 3, 4, 5, 3, 4]
nums_dict = {}

# Находим сколько раз повторяется каждое число
for num in nums_list:
    if num in nums_dict:
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1

# Выводим только повторы
nums_list_len = len(nums_list)
nums_dict_len = len(nums_dict)

if nums_dict_len == nums_list_len:
    print("Все числа уникальны.")
else:
    for key, value in nums_dict.items():
        if value > 1:
            print(f"Число {key} повторяется {value} раз(a)")
