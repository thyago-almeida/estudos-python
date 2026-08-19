import json
from datetime import datetime

def menu():
    print("=" * 30)
    print("Expense Tracker")
    print("=" * 30)
    print("1 - Add Expense")
    print("2 - List Expenses")
    print("3 - Show Summary")
    print("4 - Exit")

expenses = []

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses.extend(json.load(file))
    except FileNotFoundError:
        print("No saved expense found. Starting with an empty expense list.")
    except json.JSONDecodeError:
        print("Invalid JSON. Please enter a valid JSON.")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def read_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")

def read_description():
    while True:
        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty.")
            continue

        return description

def read_category():
    while True:
        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            continue

        return category

def read_date():
    while True:
        date = input("Enter date (DD/MM/YYYY): ").strip()

        if not date:
            print("Date cannot be empty.")
            continue

        try:
            datetime.strptime(date, "%d/%m/%Y")
            return date

        except ValueError:
            print("Invalid date. Please use DD/MM/YYYY.")


def add_expense():
    expense = {
        "description": read_description(),
        "amount": read_amount(),
        "category": read_category(),
        "date": read_date()
    }

    expenses.append(expense)

    save_expenses()

    print("Expense Added Successfully.")

def show_expenses():
    if expenses:
        for index, expense in enumerate(expenses, 1):
            print(f"{index} - {expense['description']} - {expense['amount']} - {expense['category']} - {expense['date']}")
    else:
        print ("No expenses registered.")

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def show_summary():
    if not expenses:
        print("No expenses registered.")
    else:
        total = calculate_total()
        print(f"Total expenses: R$ {total:.2f}")

load_expenses()

option = 0

while option != 4:
    menu()

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Invalid option. Please enter a number.")
        continue

    if option == 1:
        add_expense()
    elif option == 2:
        show_expenses()
    elif option == 3:
        show_summary()
    elif option == 4:
        print("Thanks for using it")
    else:
        print("Invalid option")