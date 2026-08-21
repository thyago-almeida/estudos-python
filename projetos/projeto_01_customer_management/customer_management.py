def menu():
    print("=" * 30)
    print("Customer Management System")
    print("=" * 30)
    print("1 - Add Customer")
    print("2 - Show Customer")
    print("3 - Search Customers")
    print("4 - Remove Customer")
    print("5 - Exit")


customers = []

def load_customers():
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                customer = line.strip()
                customers.append(customer)
    except FileNotFoundError:
        print("No saved customers found. Starting with an empty list.")

def save_customers():
    with open("customers.txt", "w") as file:
        for customer in customers:
            file.write(customer + "\n")

def add_customer():
    found = False
    new_customer = input("Add a Customer: ").strip()

    if not new_customer:
        print("Customer name cannot be empty.")
        return

    for customer in customers:
        if customer.lower() == new_customer.lower():
            found = True
            print("Customer already registered.")
            break
    if not found:
        customers.append(new_customer)
        save_customers()
        print("Customer Added Successfully.")


def show_customers():
    if customers:
        for index, customer in enumerate(customers, 1):
            print(f"{index} - {customer}")
    else:
        print ("No customers registered.")

def search_customers():
    found = False
    search_name = input("Search a customer: ")
    for customer in customers:
        if customer.lower() == search_name.lower():
            found = True
            print("Customer Found.")
            break
    if not found:
        print("Customer not found.")

def remove_customer():
    found = False
    customers_to_remove = input("Remove a Customer: ")
    for customer in customers:
        if customer.lower() == customers_to_remove.lower():
            found = True
            customers.remove(customer)
            save_customers()
            print("Customer Removed Successfully")
            break
    if not found:
        print("Customer not found.")

load_customers()

option = 0

while option != 5:
    menu()

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Invalid option. Please enter a number.")
        continue

    if option == 1:
        add_customer()
    elif option == 2:
        show_customers()
    elif option == 3:
        search_customers()
    elif option == 4:
        remove_customer()
    elif option == 5:
        print("Thank's for using it")
    else:
        print("Invalid option")



