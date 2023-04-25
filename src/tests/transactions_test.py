import unittest
import sys
import os
from transactions import Expense, Revenue, Budget, Transaction

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")))


class TestTransactions(unittest.TestCase):
    def test_expense_creation(self):
        expense = Expense(50, "Ruokaostokset", "2023-04-06")
        self.assertEqual(expense.amount, -50)
        self.assertEqual(expense.description, "Ruokaostokset")
        self.assertEqual(expense.date, "2023-04-06")

    def test_budget_set_up(self):
        budget = Budget()
        self.assertEqual(budget.transactions, [])

    def test_add_expense(self):
        budget = Budget()
        budget.add_expense(50, "Ruokaostokset", "2022-02-01")
        self.assertEqual(len(budget.transactions), 1)
        self.assertEqual(budget.transactions[0].amount, -50)
        self.assertEqual(budget.transactions[0].description, "Ruokaostokset")

    def test_add_revenue(self):
        budget = Budget()
        budget.add_revenue(200, "Palkka", "2023-04-17")
        self.assertEqual(len(budget.transactions), 1)
        self.assertEqual(budget.transactions[0].amount, 200)
        self.assertEqual(budget.transactions[0].description, "Palkka")

    def test_get_balance(self):
        budget = Budget()
        budget.add_expense(50, "Ruokaostokset", "2023-04-18")
        budget.add_revenue(200, "Palkka", "2023-04-18")
        self.assertEqual(budget.get_balance(), 150)

    def test_revenue_creation(self):
        revenue = Revenue(200, "Palkka", "2022-07-04")
        self.assertEqual(revenue.amount, 200)
        self.assertEqual(revenue.description, "Palkka")
        self.assertEqual(revenue.date, "2022-07-04")
