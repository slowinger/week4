# Solution to week4 homework
# By: Stephen Lowinger

class BankAccount:
    def __init__(self):
        self.balance = 0.00

    def deposit(self, amount):
        if amount >= 0:
            initial_balance = self.balance
            self.balance = float(initial_balance) + float(amount)
            return self.balance

    def withdraw(self, amount):
        if amount > 0:
            initial_balance = self.balance
            new_balance = float(initial_balance) - float(amount)
            if new_balance >= 0:
                self.balance = new_balance
                return self.balance

    def transfer(self, amount, account):
        internal_initial_balance = self.balance
        external_initial_balance = account.balance
        internal_new_balance = float(internal_initial_balance) - float(amount)
        external_new_balance = float(external_initial_balance) + float(amount)
        if internal_new_balance >= 0 and external_new_balance >= 0:
            self.balance = internal_new_balance
            account.balance = external_new_balance
            return self.balance, account.balance
