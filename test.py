class SavingsAccount:

    def __init__(self, account_holder, interest_rate):
        self.account_holder = account_holder
        self.interest_rate = interest_rate
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
             self.balance -= amount

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


    def __str__(self):
        return f"Savings account for {self.account_holder} has £{self.balance:.2f}"

def test_savings_account():
    acc = SavingsAccount("Alicia", 0.05)
    print("Inital Account")
    print(acc)

    print("\nDepositing £100..")
    acc.deposit(100)
    print(acc)

    print("\nWithdrawing £40")
    acc.withdraw(40)
    print(acc)

    print("Attempting to withdraw £200")
    acc.withdraw(200)
    print(acc)

    print("Adding interest")
    acc.add_interest()
    print(acc)

test_savings_account()