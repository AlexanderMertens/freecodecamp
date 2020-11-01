DESCR_STR = "description"
AMOUN_STR = "amount"
LINE_WIDTH = 30


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

    def __str__(self):
        if len(self.name) > 30:
            result = self.name[:30]
        else:
            length = (LINE_WIDTH - len(self.name)) // 2
            front_spacing = '*' * length
            back_spacing = '*' * (LINE_WIDTH - length - len(self.name))
            result = ''.join((front_spacing, self.name, back_spacing))
        for entry in self.ledger:
            result = ''.join((result, '\n', entry_to_string(entry)))
        total = num_to_string(self.get_balance())
        result = ''.join((result, '\n', 'Total: ', total))
        return result


def entry_to_string(entry):
    description = entry[DESCR_STR]
    if len(description) > 23:
        description = description[:23]
    amount = num_to_string(entry[AMOUN_STR])
    spacing = ' ' * (LINE_WIDTH - len(description) - len(amount))
    return spacing.join((description, amount))


def num_to_string(num):
    num_str = str(round(num, 2))
    if '.' not in num_str:
        num_str = '.'.join((num_str, "00"))
    if '.' in num_str[-2:]:  # check if there's only a single digit after the dot
        num_str += '0'
    return num_str

def create_spend_chart(categories):
    return ''
