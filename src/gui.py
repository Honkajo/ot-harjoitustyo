import tkinter as tk
from transactions import Budget


class WalletTrackerGUI(tk.Tk):
    """Määrittelee käyttäjän tilin näkymän, johon sisältyy painikkeet toimintoineen, tekstikentät ja niiden sijainnit. 
    Lisäksi myös tekstien, painikkeiden ja ikkunan koot.

    Args:
        tk (_type_): _description_
    """
    def __init__(self, transactions_file):
        super().__init__()
        self.transactions_file = transactions_file
        self.title("WalletTracker")

        self.budget = Budget(transactions_file)

        self.expense_label = tk.Label(self, text="Syötä tulo tai meno")
        self.expense_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_label = tk.Label(self, text="Määrä:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)

        self.description_label = tk.Label(self, text="Kuvaus:")
        self.description_label.grid(row=2, column=0, padx=10, pady=10)

        self.date_label = tk.Label(self, text="Aika (YYYY-MM-DD):")
        self.date_label.grid(row=3, column=0, padx=10, pady=10)

        self.balance_label = tk.Label(self, text="Saldo:")
        self.balance_label.grid(row=5, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=1, column=1, padx=0, pady=10)

        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=3, column=1, padx=10, pady=10)

        self.transactions_text = tk.Text(self, height=10, width=50)
        self.transactions_text.grid(
            row=4, column=0, columnspan=2, padx=10, pady=10)

        self.balance_text = tk.Text(self, height=1, width=20)
        self.balance_text.grid(row=5, column=1, padx=10, pady=10)

        self.add_expense_button = tk.Button(
            self, text="Lisää meno", command=self.add_expense)
        self.add_expense_button.grid(row=4, column=2, padx=10, pady=10)

        self.add_revenue_button = tk.Button(
            self, text="Lisää tulo", command=self.add_revenue)
        self.add_revenue_button.grid(row=5, column=2, padx=0, pady=10)

        self.display_transactions_button = tk.Button(
            self, text="Näytä tapahtumat", command=self.display_transactions)
        self.display_transactions_button.grid(
            row=6, column=0, padx=10, pady=10)

        self.display_balance_button = tk.Button(
            self, text="Näytä saldo", command=self.display_balance)
        self.display_balance_button.grid(row=6, column=1, padx=10, pady=10)

        self.delete_transaction_button = tk.Button(
            self, text="Poista tapahtuma", command=self.delete_transaction)
        self.delete_transaction_button.grid(row=6, column=2, padx=10, pady=10)

    def add_expense(self):
        """Hakee graafisessa käyttöliittymässä syötetyn menon määrän ja muuttaa sen liukuluvuksi. Lisäksi hakee myös tapahtuman kuvauksen ja päivämäärän.
        Meno lisätään transactions-listaan. Lopuksi poistaa syötetyt tiedot tekstikentistä.
        """
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        date = self.date_entry.get()
        self.budget.add_expense(amount, description, date)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def add_revenue(self):
        """Hakee graafisessa käyttöliittymässä syötetyn tulon määrän ja muuttaa sen liukuluvuksi. Lisäksi hakee myös tapahtuman kuvauksen ja päivämäärän.
        Meno lisätään transactions-listaan. Lopuksi tyhjentää tekstikentät.
        """
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        date = self.date_entry.get()
        self.budget.add_revenue(amount, description, date)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def display_transactions(self):
        """Poistaa transactions_text-tekstikentästä kaiken siinä olevan tekstin. "1.0" viittaa ensimmäisen rivin ensimmäiseen merkkiin ja tk.END koko tekstin loppuun.
        Kutsuu display_transactions-metodia, joka palauttaa tapahtumat yhtenä merkkijonona ja lisää tämän merkkijonon tekstikenttään, jossa tapahtumat näkyvät.
        """
        transactions = self.budget.display_transactions()
        self.transactions_text.delete("1.0", tk.END)
        self.transactions_text.insert(tk.END, transactions)

    def display_balance(self):
        """Hakee nykyisen saldon Budget-oliosta, poistaa olemassa olevan tekstin saldoa vastaavasta tekstikentästä graafisessa käyttöliittymässä ja
        lisää nykyisen saldon kahden desimaalin tarkkuudella saldon tekstikenttään
        """
        balance = self.budget.get_balance()
        self.balance_text.delete("1.0", tk.END)
        self.balance_text.insert(tk.END, f"{balance:.2f}€")

    def delete_transaction(self):
        """Hakee nykyisen rivin indeksin transactions_text kentästä. Metodi jakaa merkkijonon ensimmäisen "."-merkin jälkeen ja 
        ottaa kyseistä merkkiä edeltävän tekstin, mikä sattuu olemaan rivin rivinumero. Koska tkinterissä tekstikentässä rivinumerot alkavat 1:stä ja 
        Pythonin listat alkavat 0:sta, tulee indeksi kokonaislukumuodosta vähentää 1:ksi. Tämän jälkeen indeksiä vastaava tapahtuma poistetaan ja tapahtumat näytetään uudestaa
        """
        index = self.transactions_text.index(tk.CURRENT).split('.', 1)[0]
        index = int(index) - 1
        self.budget.delete_transaction(index)
        self.display_transactions()
