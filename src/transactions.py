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
        transactions = '\n'.join([str(transaction)
                                 for transaction in self.transactions])
        return transactions

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)
