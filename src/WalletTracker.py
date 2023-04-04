class Transaction:
    def __init__(self, amount, description, date):
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.description} ({self.date}): {self.amount}"


class Expense(Transaction):
    def __init__(self, amount, description, date):
        super().__init__(-abs(amount), description, date)


class Revenue(Transaction):
    def __init__(self, amount, description, date):
        super().__init__(abs(amount), description, date)


class Budget:
    def __init__(self):
        self.transactions = []

    def add_expense(self, amount, description, date):
        expense = Expense(amount, description, date)
        self.transactions.append(expense)

    def add_revenue(self, amount, description, date):
        revenue = Revenue(amount, description, date)
        self.transactions.append(revenue)

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)


def display_menu():
    print("\n--- MENU ---")
    print("1. Add Expense")
    print("2. Add Revenue")
    print("3. Display Transactions")
    print("4. Display Balance")
    print("0. Exit")


budget = Budget()

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        date = input("Enter expense date (YYYY-MM-DD): ")
        budget.add_expense(amount, description, date)
    elif choice == 2:
        amount = float(input("Enter revenue amount: "))
        description = input("Enter revenue description: ")
        date = input("Enter revenue date (YYYY-MM-DD): ")
        budget.add_revenue(amount, description, date)
    elif choice == 3:
        budget.display_transactions()
    elif choice == 4:
        print("Balance:", budget.get_balance())
    elif choice == 0:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
