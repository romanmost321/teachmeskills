"""
Author: Roman Mostyko
Date_hw: 07/04/2026
Summary: hw_3
"""

# 4. Дана строка. Замените в этой строке все появления
# буквы h на букву H, кроме первого и последнего вхождения.
# Подсказка: использовать метод replace с параметрами.
# Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’

original_str: str = "hhhabchghhh"
modified_str = original_str[0] + original_str[1:-1].replace("h", "H") + original_str[-1]
print(
    f"На вход была подана строка {original_str}, в которой были заменены символы {modified_str}."
)
