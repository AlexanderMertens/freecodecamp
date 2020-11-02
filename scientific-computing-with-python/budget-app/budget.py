import math

DESCR_STR = "description"
AMOUN_STR = "amount"
LINE_WIDTH = 30


class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=''):
        if amount >= 0:
            self.ledger.append({AMOUN_STR: amount, DESCR_STR: description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) and amount >= 0:
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

    def get_withdrawn_total(self):
        withdrawn = 0
        for entry in self.ledger:
            if entry[AMOUN_STR] < 0:
                withdrawn -= entry[AMOUN_STR]
        return withdrawn

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
    withdraw_amounts = list(map(lambda x: x.get_withdrawn_total(), categories))
    total_withdrawn = sum(withdraw_amounts)
    withdraw_percentages = list(map(lambda x: round_down((100 * x) / total_withdrawn), withdraw_amounts))
    result = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        percentage = str(i)
        percentage_string = ''.join((' ' * (3 - len(percentage)), percentage, '|'))
        percentage_bars = '  '.join('o' if percentage >= i else ' ' for percentage in withdraw_percentages)
        result += ' '.join((percentage_string, percentage_bars, ' \n'))
    result = ''.join((result, ' ' * 4, '-' * (3 * len(categories) + 1), '\n'))
    longest_name = max(map(lambda x: len(x.name), categories))
    names = [category.name + (longest_name - len(category.name)) * ' ' for category in categories]
    for line in zip(*names):
        result += ' ' * 5
        result += '  '.join(line) + "  \n"
    return result.rstrip('\n')


def round_down(n):
    decimals = -1
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
