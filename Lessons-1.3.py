import requests
from datetime import datetime


def exchange_rates(date, value, val_code):
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={date}&valcode={val_code}&sort=exchangedate&order=desc&json"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print("Помилка: Неможливо отримати погодні дані")
        return

    exchange = data[0]['rate']
    valcode = data[0]['cc']
    calc_rate = value * exchange
    result = round(calc_rate, 2)

    print("*" * 50)
    print("Поточний курс:", 1, valcode, f"= {exchange} UAH")
    print(f"Розрахунок: {value} {valcode} = {result} UAH")
    print("*" * 50)


date = datetime.now().strftime('%Y%m%d')

while True:
    print("Enter valcode: \n"
          "1. USD\n"
          "2. BYN\n"
          "3. EUR\n"
          "4. RUB\n"
          "5. PLN\n"
          "6. OTHER currency\n"
          "0. Exit")

    val_code = int(input("Your value: "))

    if val_code == 0:
        print("Thank you for using the program. Goodbye!")
        break

    if val_code in [1, 2, 3, 4, 5]:
        value = int(input("Enter the amount: "))

        if val_code == 1:
            exchange_rates(date, value, "USD")
        elif val_code == 2:
            exchange_rates(date, value, "BYN")
        elif val_code == 3:
            exchange_rates(date, value, "EUR")
        elif val_code == 4:
            exchange_rates(date, value, "RUB")
        elif val_code == 5:
            exchange_rates(date, value, "PLN")
    elif val_code == 6:
        val_code = input("Enter the currency: ")
        value = float(input("Enter the amount: "))
        exchange_rates(date, value, val_code)
    else:
        print("Incorrect value selected")
