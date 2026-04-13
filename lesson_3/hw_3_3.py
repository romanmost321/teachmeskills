"""
Author: Roman Mostyko
Date_hw: 07/04/2026
Summary: hw_3
"""

# 3.Дана строка, состоящая из слов, разделенных
# пробелами. (Вот 4 варианта тестовых данных для программы:
# ‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’).
# Определите, сколько в ней слов.

some_str: str = "Hello world, a b c, test, test1 test2 test3 test4 test5"
some_list = len(some_str.split())
print(f"На вход подана строка {some_str}\nВ ней содержится {some_list} слов.")
