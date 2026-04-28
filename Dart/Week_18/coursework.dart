void main() {
  priceOfEggs(2);
  priceOfPotatos(0.5);
  double total = priceOfEggs(2) + priceOfPotatos(0.5);
  print(total);
  print(totalCost(18, 2, 5));
}

double priceOfEggs(double quantity) {
  double price = 0.3;
  return quantity * price;
}

double priceOfPotatos(double quanity) {
  double price = 0.75;
  return price * quanity;
}

double totalCost(double age, double eggsQty, double potatQty) {
  double total = priceOfEggs(0.5) + priceOfPotatos(2);
  if (age <= 18) {
    total = total * 0.9;
  } else if (age <= 65) {
    //no discount
  } else {
    total = total * (2 / 3);
  }
  return total;
}
