import unittest
import sys
import os
from transactions import Expense, Revenue, Budget, Transaction

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")))


class TestTransactions(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(50, "Ruokaostokset", "2023-04-06")
        self.assertEqual(transaction.amount, 50)
        self.assertEqual(transaction.description, "Ruokaostokset")
        self.assertEqual(transaction.date, "2023-04-06")


class TestExpenses(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense(100, "Testimeno", "2023-04-21")
        self.assertEqual(expense.amount, -100)
        self.assertEqual(expense.description, "Testimeno")
        self.assertEqual(expense.date, "2023-04-21")


class TestBudget(unittest.TestCase):

    def setUp(self):
        self.test_file = "testi_transactions.txt"
        with open(self.test_file, "w") as file:
            file.write("-100|Testimeno|2023-04-21\n200|Testitulo|2023-04-21")
        self.transactions_file = self.test_file
        self.budget = Budget(self.transactions_file)

    def tearDown(self):
        self.budget.transactions = []
        self.budget.save_transactions()
        os.remove(self.test_file)

    def test_budget_set_up(self):
        self.assertEqual(self.budget.transactions[0].amount, -100)
        self.assertEqual(self.budget.transactions[0].description, "Testimeno")
        self.assertEqual(self.budget.transactions[0].date, "2023-04-21")
        self.assertEqual(self.budget.transactions[1].amount, 200)
        self.assertEqual(self.budget.transactions[1].description, "Testitulo")
        self.assertEqual(self.budget.transactions[1].date, "2023-04-21")

    def test_add_expense(self):
        self.budget.add_expense(50, "Uusi testimeno", "2023-05-11")
        self.assertEqual(len(self.budget.transactions), 3)
        self.assertEqual(self.budget.transactions[2].amount, -50)
        self.assertEqual(self.budget.transactions[2].description, "Uusi testimeno")
        self.assertEqual(self.budget.transactions[2].date, "2023-05-11")

    def test_add_revenue(self):
        self.budget.add_revenue(25, "Uusi testitulo", "2023-04-17")
        self.assertEqual(len(self.budget.transactions), 3)
        self.assertEqual(self.budget.transactions[2].amount, 25)
        self.assertEqual(
            self.budget.transactions[2].description, "Uusi testitulo")
        self.assertEqual(self.budget.transactions[2].date, "2023-04-17")

    def test_get_balance(self):
        self.assertEqual(self.budget.get_balance(), 100)

    def test_delete_transaction(self):
        self.budget.delete_transaction(1)
        self.assertEqual(len(self.budget.transactions), 1)
        self.assertEqual(self.budget.transactions[0].amount, -100)
        self.assertEqual(self.budget.transactions[0].description, "Testimeno")
        self.assertEqual(self.budget.transactions[0].date, "2023-04-21")
