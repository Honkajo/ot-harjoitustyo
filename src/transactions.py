import os


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
    def __init__(self, transactions_file):
        self.transactions = []
        self.transactions_file = transactions_file
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'r') as file:
                for line in file:
                    amount, description, date = line.strip().split('|')
                    amount = float(amount)
                    if amount > 0:
                        transaction = Revenue(amount, description, date)
                    else:
                        transaction = Expense(-amount, description, date)
                    self.transactions.append(transaction)

    def save_transactions(self):
        with open(self.transactions_file, 'w') as file:
            for transaction in self.transactions:
                file.write(
                    f"{transaction.amount}|{transaction.description}|{transaction.date}\n")

    def add_expense(self, amount, description, date):
        expense = Expense(amount, description, date)
        self.transactions.append(expense)
        self.save_transactions()

    def add_revenue(self, amount, description, date):
        revenue = Revenue(amount, description, date)
        self.transactions.append(revenue)
        self.save_transactions()

    def display_transactions(self):
        transactions = '\n'.join([str(transaction)
                                 for transaction in self.transactions])
        return transactions

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)

    def delete_transaction(self, index):
        del self.transactions[index]
