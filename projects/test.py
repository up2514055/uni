class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"{self.account_holder} has £{self.balance}"
    
def test_bank_account():
    bank1 = BankAccount("James", 100)
    bank2 = BankAccount("Sarah")

    bank1.deposit(100)
    bank2.deposit(200)

    bank1.withdraw(50)
    print(bank1)
    print(bank2)

test_bank_account()

