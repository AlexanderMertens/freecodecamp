DESCR_STR = "description"
AMOUN_STR = "amount"


class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({AMOUN_STR: amount, DESCR_STR: description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({AMOUN_STR: -amount, DESCR_STR: description})
            return True
        else:
            return False

    def transfer(self, amount, other):
        if self.withdraw(amount, f"Transfer to {other.name}"):
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry[AMOUN_STR]
        return balance

    def check_funds(self, amount):
        return amount <= self.get_balance()
