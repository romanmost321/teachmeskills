import tkinter as tk

# 1. Создаем окно_1 приветствия
hello_window = tk.Tk()
hello_window.title("Начало работы")
hello_window.geometry("500x400")

# 2. Добавляем виджеты, котороый содержит текст
label = tk.Label(hello_window, text="Здравствуйте, как вас зовут?")
label.pack()

# 3. Строка для ввода имени
name = tk.Entry(hello_window)
name.pack()


# 4. Функция, которая заберет текст из поля и выведет его
def click() -> None:
    name_user_text = name.get()  # Вот так мы получаем текст

    hello_window.destroy()

    # 1. Создаем окно_2 расчет кредита
    cal_window = tk.Tk()
    cal_window.title("Расчет параметров кредита")
    cal_window.geometry("500x400")

    # 2. Добавляем виджеты, котороый содержит текст
    label = tk.Label(
        cal_window,
        text=f"Здравствуйте, {name_user_text}!\n"
        f"Далее перейдем для расчета твоего кредита.\n"
        f"Для этого необходимо указать данные ниже:",
    )
    label.pack()

    # 3. Добавляем виджеты заголовок для годовая процентная ставка
    label = tk.Label(cal_window, text="1. Годовая процентная ставка:")
    label.pack()

    # 4. Строка для ввода годовая процентная ставка
    interest_rate = tk.Entry(cal_window)
    interest_rate.pack()

    # 5. Добавляем виджеты заголовок для сумма займа
    label = tk.Label(cal_window, text="2. Сумма займа:")
    label.pack()

    # 6. Строка для ввода сумма займа
    loan_amount = tk.Entry(cal_window)
    loan_amount.pack()

    # 7. Добавляем виджеты заголовок для кол-во месяцев
    label = tk.Label(cal_window, text="3. Кол-во месяцев:")
    label.pack()

    # 8. Строка для ввода количество месяцев, на которые взят кредит
    months = tk.Entry(cal_window)
    months.pack()

    # 9. Функция, которая заберет текст из поля и выведет его
    def click_1() -> None:
        interest_rate_user_text = float(interest_rate.get())
        loan_amount_user_text = float(loan_amount.get())
        months_user_text = float(months.get())

        cal_window.destroy()

        # 1. Создаем окно_3 итог результатов
        exit_window = tk.Tk()
        exit_window.title("Итоговый расчет")
        exit_window.geometry("500x400")

        # 2. Добавляем виджеты
        label = tk.Label(
            exit_window,
            text=f"{name_user_text}, Вами были указаны следующие данные:\n"
            f"Годовая процентная ставка - {interest_rate_user_text}%\n"
            f"Сумма займа - {loan_amount_user_text} бел. руб.\n"
            f"Кол-во месяцев - {months_user_text} мес.",
        )
        label.pack()

        # 3. Производим расчеты
        monthly_rate = interest_rate_user_text / (
            12 * 100
        )  # месячная процентная ставка
        monthly_payment = round(
            (
                (
                    loan_amount_user_text
                    * monthly_rate
                    * (pow((1 + monthly_rate), months_user_text))
                )
                / ((pow((1 + monthly_rate), months_user_text)) - 1)
            ),
            2,
        )  # ежемесячная выплата
        total = round(
            (monthly_payment * months_user_text), 2
        )  # сколько всего заплатит банку
        over_payment = round((total - loan_amount_user_text), 2)  # переплата

        # 4. Добавляем виджеты заголовок для кол-во месяцев
        label = tk.Label(
            exit_window,
            text=f"Размер ежемесячной выплаты составит: {monthly_payment}\n"
            f"Пользователь заплатит банку: {total}\n"
            f"Переплата составит: {over_payment}",
        )
        label.pack()

        # 5. Запускаем цикл для окна_1
        exit_window.mainloop()

    # 10. Кнопка
    btn = tk.Button(cal_window, text="Рассчитать", command=click_1)
    btn.pack()

    # 11. Запускаем цикл для окна_2
    cal_window.mainloop()


# 5. Кнопка
btn = tk.Button(hello_window, text="Далее", command=click)
btn.pack()


# 6. Запускаем цикл для окна_1
hello_window.mainloop()
