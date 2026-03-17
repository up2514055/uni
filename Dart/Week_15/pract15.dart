import 'dart:io';
import 'dart:math';

void main() {
  // sayName();
  // studentDetails();
  // eurosToPounds(20);
  // fahrenheitToCelsius(100);
  // areaOfCircle();
  // print(areaOfCircle2(50));
  // print(circumferenceOfCircl2(20));
  // circleInfo();
  // displayBurgerOrder(3, 9.99);
  print(howManyBurgers(10, 25));
}

void sayName() {
  print("Dylan Mazur");
}

void studentDetails() {
  print("My name is Dylan Mazur");
  print("My student number is 2514055");
  print("My email address is up2514055@myport.ac.uk");
}

void eurosToPounds(double euros) {
  double pounds = euros * 0.86;
  print(pounds);
}

void fahrenheitToCelsius(double fahrenheit) {
  double celsius = (fahrenheit - 32) * 5 / 9;
  print(celsius);
}

void areaOfCircle() {
  print("Please enter the radius:");
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double area = pi * pow(radius, 2);
  print("Area: $area");
}

double areaOfCircle2(double radius) {
  return pi * pow(radius, 2);
}

double circumferenceOfCircl2(double radius) {
  return pi * (radius * 2);
}

void circleInfo() {
  print("Please enter the radius");
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double area = pi * pow(radius, 2);
  double circumference = pi * (radius * 2);
  print("Area of circle: $area");
  print("Circumference of circle: $circumference");
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