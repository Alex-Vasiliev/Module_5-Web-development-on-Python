import requests
from datetime import datetime


def exchange_rates(value, val_code):
    try:
        date = datetime.now().strftime('%Y%m%d')
        url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={date}&valcode={val_code}&sort=exchangedate&order=desc&json"
        response = requests.get(url)
        data = response.json()
        response.raise_for_status()

        exchange = data[0]['rate']
        valcode = data[0]['cc']
        calc_rate = value * exchange
        result = round(calc_rate, 2)

        print("*" * 35)
        print("Current rate:", 1, valcode, f"= {exchange} UAH")
        print(f"Calculation: {value} {valcode} = {result} UAH")
        print("*" * 35, "\n")
    except requests.exceptions.HTTPError as err:
        print("!" * 50)
        print(f"HTTP request error: {err}")
        print("!" * 50, "\n")
    except requests.exceptions.RequestException as err:
        print("!" * 50)
        print(f"Request error: {err}")
        print("!" * 50, "\n")
    except Exception as err:
        print("!" * 50)
        print(f"Unexpected error: {err}")
        print("!" * 50, "\n")


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
            exchange_rates(value, "USD")
        elif val_code == 2:
            exchange_rates(value, "BYN")
        elif val_code == 3:
            exchange_rates(value, "EUR")
        elif val_code == 4:
            exchange_rates(value, "RUB")
        elif val_code == 5:
            exchange_rates(value, "PLN")
    elif val_code == 6:
        val_code = input("Enter the currency: ")
        value = float(input("Enter the amount: "))
        exchange_rates(value, val_code)
    else:
        print("Incorrect value selected")
