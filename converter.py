import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    if data.get("result"):
        return data["result"]
    else:
        return None

print("=====Currency converter App=====")

while True:
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD, INR, EUR): ").upper()
        to_currency = input("To currency (e.g., USD, INR, EUR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)

        if result is None:
            print("Invalid currency or API error. Try Again.")

        else:
            print(f"\n{amount} {from_currency} = {round(result, 2)} {to_currency}\n")

    except ValueError:
        print("Please enter a valid number.")

    choice = input("Do you want to convert again? (y/n): ").lower()
    if choice != 'y':
        print("Thank you for using the currency converter!")

    break
