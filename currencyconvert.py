import tkinter as tk
from forex_python.converter import CurrencyRates

def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())

    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = round(amount * exchange_rate, 2)

    result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")

# GUI setup
app = tk.Tk()
app.title("Currency Converter")

# Entry for user to input amount
amount_entry = tk.Entry(app, font=('Arial', 14))
amount_entry.pack(pady=10)

# Dropdown for selecting from currency
from_currency_var = tk.StringVar()
from_currency_var.set("USD")  # default currency
from_currency_dropdown = tk.OptionMenu(app, from_currency_var, "USD", "EUR", "GBP", "JPY")
from_currency_dropdown.pack(pady=10)

# Dropdown for selecting to currency
to_currency_var = tk.StringVar()
to_currency_var.set("EUR")  # default currency
to_currency_dropdown = tk.OptionMenu(app, to_currency_var, "USD", "EUR", "GBP", "JPY","INR")
to_currency_dropdown.pack(pady=10)

# Button to convert currency
convert_button = tk.Button(app, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Label to display the conversion result
result_label = tk.Label(app, text="", font=('Arial', 16))
result_label.pack(pady=10)

app.mainloop()
