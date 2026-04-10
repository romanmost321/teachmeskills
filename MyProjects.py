from tkinter import *

# 1. Создаем окно приветствия
hello_window = Tk()
hello_window.title("Начало работы")
hello_window.geometry("400x300")  # Ширина x Высота

# 2. Добавляем виджеты
label = Label(
    hello_window, text="Здравствуйте, как вас зовут?", font=("Arial", 14, "bold")
)
label.pack(pady=10)  # Текстовая метка # Размещаем её в окне

# 3. Строка для ввода имени
name = Entry(hello_window, width=20, borderwidth=5)
name.pack(pady=10)


# Функция, которая заберет текст из поля
def myClick():
    user_text = name.get()  # Вот так мы получаем текст
    label = Label(
        hello_window,
        text="Здравстуй, "
        + user_text
        + "!"
        + " Далее перейдем для расчета твоего кредита",
        wraplength=200,
    )
    hello_window.after(2000, hello_window.destroy)
    label.pack()


# Кнопка, после которой выводится текс
btn = Button(hello_window, text="Далее", command=myClick)
btn.pack()

# 3. Запускаем цикл для окна 1
hello_window.mainloop()

# 1. Создаем окно2 расчета
calc_window = Tk()
calc_window.title("Расчет параметров кредита")
calc_window.geometry("500x400")  # Ширина x Высота

# 2. Добавляем виджеты
label = Label(
    calc_window,
    text="Укажите необходимые данные, которые представлены ниже.",
    font=("Arial", 14, "bold"),
    wraplength=400,
)
label.pack(pady=10)  # Текстовая метка

# 2. Добавляем виджеты заголовок для годовая процентная ставка
label = Label(
    calc_window,
    text="Годовая процентная ставка",
    font=("Arial", 8),
    wraplength=400,
)
label.pack(pady=5)  # Текстовая метка

# 3. Строка для ввода годовая процентная ставка
interest_rate = Entry(calc_window, width=20, borderwidth=5)
interest_rate.pack(pady=5)
interest_rate.pack()

# 2. Добавляем виджеты заголовок для сумма займа
label = Label(
    calc_window,
    text="Сумма займа",
    font=("Arial", 8),
    wraplength=400,
)
label.pack(pady=5)  # Текстовая метка

# 3. Строка для ввода сумма займа
loan_amount = Entry(calc_window, width=20, borderwidth=5)
loan_amount.pack(pady=5)
loan_amount.pack()

# 2. Добавляем виджеты заголовок для кол-во месяцев
label = Label(
    calc_window,
    text="Кол-во месяцев",
    font=("Arial", 8),
    wraplength=400,
)
label.pack(pady=5)  # Текстовая метка

# 3. Строка для ввода количество месяцев, на которые взят кредит
months = Entry(calc_window, width=20, borderwidth=5)
months.pack(pady=5)
months.pack()


def myClick_1(user_text):
    user_text_1 = interest_rate.get()  # Вот так мы получаем текст
    label = Label(
        calc_window,
        text="На основании введеных тобой данных, мы получаем",
        wraplength=200,
    )
    calc_window.after(2000, calc_window.destroy)
    label.pack()


# Кнопка, после которой выводится текс
btn = Button(calc_window, text="Рассчитать", command=myClick_1)
btn.pack()


# 3. Запускаем цикл для окна 2
calc_window.mainloop()

# 1. Создаем окно2 расчета
exit_window = Tk()
exit_window.title("Итоговый расчет")
exit_window.geometry("500x400")  # Ширина x Высота

label = Label(
    exit_window,
    text="Сумма займа",
    font=("Arial", 8),
    wraplength=400,
)
label.pack(pady=5)  # Текстовая метка

exit_window.mainloop()
