class BankAccount(object):
    def __init__(self, balance = 5000):
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            return self.balance
        else:
            return 'Incorrect withdrawal amount'

class SubClass(BankAccount):
    def __init__(self, minimum):
        self.minimum = minimum



first = BankAccount()
#print(first.deposit(3000))
print(first.withdraw(1000))