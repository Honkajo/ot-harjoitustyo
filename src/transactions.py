import os


class Transaction:
    """Konstruktoriluokka, joka kuvaa tapahtumaa, jolla on kolme ominaisuutta: määrä, 
    kuvaus sekä päivämäärä. __str__ - metodi palauttaa tapahtuman merkkijonomuodossa.
    """

    def __init__(self, amount, description, date):
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.description} ({self.date}): {self.amount}"


class Expense(Transaction):
    """Expense-luokka perii Transaction-luokan ominaisuudet ja metodit, 
    mutta muuttaa määrän negatiiviseksi ottamalla arvosta itseisarvon ja 
    lisäämällä miinus-merkin perään

    Args:
        Transaction (_type_): _description_
    """

    def __init__(self, amount, description, date):
        super().__init__(-abs(amount), description, date)


class Revenue(Transaction):
    """Revenue-luokka perii Transaction-luokan ominaisuudet ja 
    metodit ja ottaa määrä-attribuutista itseisarvon

    Args:
        Transaction (_type_): _description_
    """

    def __init__(self, amount, description, date):
        super().__init__(abs(amount), description, date)


class Budget:
    """Luokka hallinnoi käyttäjien tiedostoja, joihin on tallennettu syötetyt tapahtumat 
    sekä hakee ja esittää tiedot käyttäjälle käyttäjän niin halutessaan 
    """

    def __init__(self, transactions_file):
        """Alustaa listan, johon käyttäjän tiedostoon tallennetut tapahtumat 
        siirretään niiden latauksen jälkeen. 
        Sen lisäksi myös lataa tapahtumat tiedostosta, kun olio luodaan

        Args:
            transactions_file (_type_): _description_
        """
        self.transactions = []
        self.transactions_file = transactions_file
        self.load_transactions()

    def load_transactions(self):
        """Avaa tiedoston, johon käyttäjän tapahtumat on tallennettu. 
        Lukee jokaisen rivin tiedostosta ja 
        jakaa ne |-merkillä. Jakaa tapahtumat menoihin ja tuloihin sen mukaan,
        ovatko ne negatiivisia vai positiivisia. Lisää tulot ja 
        menot aikaisemmin luotuun transactions-listaan
        """
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
        """Käy läpi jokaisen tapahtuman transactions-listassa ja kirjoittaa sen tiedostoon
        """
        with open(self.transactions_file, 'w') as file:
            for transaction in self.transactions:
                file.write(
                    f"{transaction.amount}|{transaction.description}|{transaction.date}\n")

    def add_expense(self, amount, description, date):
        """Luo uuden Expense-olion, jonka jälkeen tallentaa tapahtumat tiedoston

        Args:
            amount (_type_): _description_
            description (_type_): _description_
            date (_type_): _description_
        """
        expense = Expense(amount, description, date)
        self.transactions.append(expense)
        self.save_transactions()

    def add_revenue(self, amount, description, date):
        """Luo uuden Revenue-olion, jonka jälkeen tallentaa tapahtumat tiedostoon

        Args:
            amount (_type_): _description_
            description (_type_): _description_
            date (_type_): _description_
        """
        revenue = Revenue(amount, description, date)
        self.transactions.append(revenue)
        self.save_transactions()

    def display_transactions(self):
        """Muuttaa kaikki tapahtumat merkkijonoiksi ja yhdistää ne rivinvaihtomerkeillä. 
        Lopuksi palauttaa merkkijonon

        Returns:
            _type_: _description_
        """
        transactions = '\n'.join([str(transaction)
                                 for transaction in self.transactions])
        return transactions

    def get_balance(self):
        """Laskee yhteen kaikkien tapahtumien määrät ja palauttaa summan

        Returns:
            _type_: _description_
        """
        return sum(transaction.amount for transaction in self.transactions)

    def delete_transaction(self, index):
        """Poistaa transactions-listasta annetussa indexissä olevan tapahtuman

        Args:
            index (_type_): _description_
        """
        del self.transactions[index]
