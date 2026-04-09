some_srt_1 = "123 abf aar"

print(len(some_srt_1))  # 7

# Найти номер позиции символа в строке поиск происходит слева
print(some_srt_1.find("a"))

# Найти номер позиции символа происх происходит справа, но возвращает его обычный номер позиции
print(some_srt_1.rfind("a"))

# Считает число повторений символа в строке
print(some_srt_1.count("a"))

#
print(some_srt_1.replace("a", "X"))
