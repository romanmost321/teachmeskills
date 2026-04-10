import tkinter as ttk

hello_window = ttk.Tk()
hello_window.geometry("400x400")
hello_window.title("Greeting")


def greeting():
    hello_window.title("Greeting")
    name = person_name.get()
    res_label.config(text=f"Hello, {name}!", fg="orange")
    hello_window.after(1000, hello_window.destroy)


ttk.Label(hello_window, text="Enter ur name:").pack()
person_name = ttk.Entry(hello_window)
person_name.pack(pady=5)

ttk.Button(hello_window, text="Greet", command=greeting).pack()

res_label = ttk.Label(hello_window, text="")
res_label.pack()
hello_window.mainloop()


calc = ttk.Tk()
calc.geometry("400x400")
calc.title("Calculator")


def calculation():
    try:
        distance = float(entry_distance.get())
        consumption = float(consumption_per_km.get())
        price = float(price_per_liter.get())
        amount = consumption / 100 * distance
        full_cost = amount * price
        result_label.config(
            text=f"Понадобится: {amount:.2f} л.\nСтоимость: {full_cost:.2f} руб.",
            fg="green",
        )
    except ValueError:
        result_label.config(text="Не валидное значение", fg="red")


ttk.Label(calc, text="Расстояние км:").pack()
entry_distance = ttk.Entry(calc)
entry_distance.pack(pady=5)

ttk.Label(calc, text="Расход топлива на 100км:").pack()
consumption_per_km = ttk.Entry(calc)
consumption_per_km.pack(pady=5)

ttk.Label(calc, text="Цена за 1 литр").pack()
price_per_liter = ttk.Entry(calc)
price_per_liter.pack(pady=5)

ttk.Button(calc, text="Рассчитать", command=calculation).pack()

result_label = ttk.Label(calc, text="")
result_label.pack()

calc.mainloop()
