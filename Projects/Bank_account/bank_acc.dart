class BankAccount {
  String owner;
  double _balance = 0;

  BankAccount(this.owner, this._balance);

  double get balance => _balance;

  void deposit(double amount) {
    if (amount <= 0) {
      print("Invalid amount entered");
    } else {
      _balance += amount;
      print("Deposited $amount");
    }
  }

  void withdrawal(double amount) {
    if (amount <= 0) {
      print("Invalid amount entered");
    } else if (balance < amount) {
      print("You don't have enough money available");
    } else {
      _balance -= amount;
      print("Withdrew $amount, from your account");
    }
  }

  void printStatement() {
    print("Account Owner: $owner");
    print("Current Balance: £$_balance");
  }

  void totalBalance() {
    print("Balance is now: $_balance");
  }
}

void main() {
  var account = BankAccount('Alice', 100.0);

  account.printStatement();
  account.withdrawal(10);
  account.totalBalance();
  account.deposit(50);
  account.totalBalance();
  print("Your total are as follows: ");
  account.printStatement();
}
