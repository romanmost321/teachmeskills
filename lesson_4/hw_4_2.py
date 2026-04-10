"""
Author: Roman Mostyko
Date_hw: 09/04/2026
Summary: hw_4
"""

# 2. «Играл с кредитами – проиграл»
# m – ежемесячная выплата (monthly_payment)
# i – годовая процентная ставка (interest_rate)
# p – месячная процентная ставка (monthly_rate)
# s – сумма займа (loan_amount)
# n – количество месяцев, на которые взят кредит (months)
# Пользователь вводит с клавиатуры i, s и n, программа должна рассчитать размер ежемесячной выплаты по
# формуле, а также найти, сколько пользователь всего заплатит банку и сколько составит переплата.
# Сделать ввод/вывод данных красивым интерактивом.

interest_rate = float(input("Укажите годовую процентную ставку: "))
loan_amount = float(input("Укажите сумму займа: "))
months = int(input("Укажите кол-во месяцев для займа: "))

monthly_rate = interest_rate / (12 * 100)  # месячная процентная ставка
monthly_payment = round(
    (
        (loan_amount * monthly_rate * (pow((1 + monthly_rate), months)))
        / ((pow((1 + monthly_rate), months)) - 1)
    ),
    2,
)  # ежемесячная выплата
total = round((monthly_payment * months), 2)  # сколько всего заплатит банку
over_payment = round((total - loan_amount), 2)  # переплата


print(
    f"\tРазмер ежемесячной выплаты составит: {monthly_payment}\n\tПользователь заплатит банку: {total}\n\tПереплата составит: {over_payment}"
)
