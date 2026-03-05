import requests

# List to store conversion history
history = []


# -----------------------------
# Function to get exchange rates
# -----------------------------
def get_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["rates"]

    except:
        print("❌ Error fetching exchange rates")
        return None


# -----------------------------
# Function to convert currency
# -----------------------------
def convert_currency():
    print("\n💱 Currency Converter 💱")

    base = input("Enter base currency (USD, INR, EUR etc): ").upper()
    target = input("Enter target currency: ").upper()

    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount!")
        return

    rates = get_rates(base)

    if rates is None:
        return

    if target not in rates:
        print("❌ Invalid target currency")
        return

    rate = rates[target]
    converted = amount * rate

    print("\n✅ Conversion Result")
    print(f"{amount} {base} = {round(converted, 2)} {target}")

    # Store in history list
    record = f"{amount} {base} = {round(converted, 2)} {target}"
    history.append(record)


# -----------------------------
# Function to show history
# -----------------------------
def show_history():
    print("\n📜 Conversion History")

    if len(history) == 0:
        print("No conversions yet.")

    else:
        for item in history:
            print(item)


# -----------------------------
# Function to show common currencies
# -----------------------------
def show_common_currencies():
    currencies = [
        "USD - US Dollar",
        "INR - Indian Rupee",
        "EUR - Euro",
        "GBP - British Pound",
        "JPY - Japanese Yen",
        "AUD - Australian Dollar",
        "CAD - Canadian Dollar",
        "CHF - Swiss Franc",
        "CNY - Chinese Yuan"
    ]

    print("\n🌍 Common Currency Codes")

    for c in currencies:
        print(c)


# -----------------------------
# Main Program (Menu)
# -----------------------------
while True:

    print("\n==============================")
    print("      CURRENCY CONVERTER")
    print("==============================")
    print("1. Convert Currency")
    print("2. Show Conversion History")
    print("3. Show Currency Codes")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        convert_currency()

    elif choice == "2":
        show_history()

    elif choice == "3":
        show_common_currencies()

    elif choice == "4":
        print("\nThank you for using Currency Converter 💱")
        break

    else:
        print("Invalid choice! Please try again.")