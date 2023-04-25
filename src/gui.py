import tkinter as tk
from transactions import Budget


class WalletTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WalletTracker")

        self.budget = Budget()

        self.expense_label = tk.Label(self.root, text="Syötä tulo tai meno")
        self.expense_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_label = tk.Label(self.root, text="Määrä:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)

        self.description_label = tk.Label(self.root, text="Kuvaus:")
        self.description_label.grid(row=2, column=0, padx=10, pady=10)

        self.date_label = tk.Label(self.root, text="Aika (YYYY-MM-DD):")
        self.date_label.grid(row=3, column=0, padx=10, pady=10)

        self.balance_label = tk.Label(self.root, text="Saldo:")
        self.balance_label.grid(row=5, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=3, column=1, padx=10, pady=10)

        self.transactions_text = tk.Text(self.root, height=10, width=50)
        self.transactions_text.grid(
            row=4, column=0, columnspan=2, padx=10, pady=10)

        self.balance_text = tk.Text(self.root, height=1, width=20)
        self.balance_text.grid(row=5, column=1, padx=10, pady=10)

        self.add_expense_button = tk.Button(
            self.root, text="Lisää meno", command=self.add_expense)
        self.add_expense_button.grid(row=4, column=2, padx=10, pady=10)

        self.add_revenue_button = tk.Button(
            self.root, text="Lisää tulo", command=self.add_revenue)
        self.add_revenue_button.grid(row=5, column=2, padx=10, pady=10)

        self.display_transactions_button = tk.Button(
            self.root,text="Näytä tapahtumat", command=self.display_transactions)
        self.display_transactions_button.grid(
            row=6, column=0, padx=10, pady=10)

        self.display_balance_button = tk.Button(
            self.root, text="Näytä saldo", command=self.display_balance)
        self.display_balance_button.grid(row=6, column=1, padx=10, pady=10)

    def add_expense(self):
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        date = self.date_entry.get()
        self.budget.add_expense(amount, description, date)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def add_revenue(self):
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        date = self.date_entry.get()
        self.budget.add_revenue(amount, description, date)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def display_transactions(self):
        transactions = self.budget.display_transactions()
        self.transactions_text.delete("1.0", tk.END)
        self.transactions_text.insert(tk.END, transactions)

    def display_balance(self):
        balance = self.budget.get_balance()
        self.balance_text.delete("1.0", tk.END)
        self.balance_text.insert(tk.END, f"${balance:.2f}")
