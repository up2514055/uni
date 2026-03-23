import 'dart:io';
void main() {
  burgerOrder();
}

void displayBurgerOrder(int numberOfBurgers, double pricePerBurger) {
  double totalPrice = numberOfBurgers * pricePerBurger;

  String burgers = '🍔' * numberOfBurgers;

  print("Your order: $burgers");
  print("Total: £${totalPrice.toStringAsFixed(2)}");
}

int howManyBurgers(double priceOfBurger, double moneyUserHas) {
  int amount = moneyUserHas ~/ priceOfBurger;
  return amount;
}

void burgerOrder() {
  print("How much money are you willing to spend?");
  String? input = stdin.readLineSync();
  double moneyWillingToSpend = double.parse(input!);
  double pricePerBurger = 9.99;
  int burgers = howManyBurgers(pricePerBurger, moneyWillingToSpend);
  displayBurgerOrder(burgers, pricePerBurger);
}