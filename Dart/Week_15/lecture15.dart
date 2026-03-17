import 'dart:io';
import 'dart:math';

void main() {
  //int x = 5;
  //int result = multiplyBy2(x);
  //print('Result: $result');
  //the $ is the same as using {} in python when using f strings
  // double distance = 100;
  // double time = 9.58;
  // speedCalculator(distance, time);
  // print(secret(5, 10.0));
  // typeConversion();
  birthdayMessage("dylan", 15);
  pizzaOrder();
}

int multiplyBy2(int number) {
  return number * 2;
}

void speedCalculator(double distance, double time) {
  double speed = distance / time;
  print('Speed: $speed');
}

//double means float in python

double secret(int x, double y) {
  x += 5;
  y /= 5;
  x ~/= 3;
  y *= 2;
  x++;
  double result = x * y;
  return result;
}
// ++ increments the numerical value by 1 and -- is the opposite

void typeConversion() {
  int i = 5;
  double d = 10.65;

  // convert from double to integer
  int dAsInt = d.toInt();
  int dFloor = d.floor();
  int dCeil = d.ceil();
  int dRounded = d.round();
  print("dAsInt: $dAsInt, dFloor: $dFloor, dCeil: $dCeil, dRounded: $dRounded");

  // convert from int to double
  double iAsDouble = i.toDouble();
  print("iAsDouble: $iAsDouble");

  // convert from int or double to String
  String iAsString = i.toString();
  String dAsString = d.toString();
  String dAsFixed = d.toStringAsFixed(1);
  print("iAsString: $iAsString, dAsString: $dAsString, dAsFixed: $dAsFixed");

  // convert from String to int or double
  i = int.parse(iAsString);
  d = double.parse(dAsString);
  print("i: $i, d: $d");
}

String getGreetings() {
  String arabic = 'مرحبا';
  String hindi = 'नमस्ते';
  String russian = 'Привет';
  String chinese = '你好';
  String emoji = '👋';
  return '$arabic, $hindi, $russian, $chinese, $emoji';
}

void birthdayMessage(String name, int ageLastYear) {
  print(" Happy" + (ageLastYear + 1).toString() + "th birthday, " + name + "!");
  print("Happy ${ageLastYear + 1}th birthday, $name!");
  //place longer expression in curly brackets
}

// ? tells the complier that studentnumber could be NUL
// can use ! to promise the compiler that the user will enter a number
void askForStudentNumber() {
  print("What is your student number?");
  String? input = stdin.readLineSync();
  print("Your student number is $input");
}

int x = 50;
double xSqrt = sqrt(x);
int xSquared = pow(x, 2).toInt();
double areaOfCircle = pi * pow(x, 2);
double sinX = sin(x); // sin of x in radians
double cosX = cos(x); // cos of x in radians

void circumferenceOfCircle() {
  print('Enter the radius of a circle:');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double circumference = 2 * pi * radius;
  print('Circumference: ${circumference.toStringAsFixed(2)}');
}

String getPizzaType() {
  print('What type of pizza do you want?');
  String? input = stdin.readLineSync();
  return input!;
}

int getPizzaSize() {
  print('Enter the diameter of the pizza:');
  String? input = stdin.readLineSync();
  return int.parse(input!);
}

double getPizzaPrice(int radius) {
  double pricePerSquareInch = 0.05;
  double area = pi * pow(radius / 2, 2);
  return area * pricePerSquareInch;
}

void pizzaOrder() {
  String pizzaType = getPizzaType();
  int pizzaSize = getPizzaSize();
  double pizzaPrice = getPizzaPrice(pizzaSize);
  print(
    'A $pizzaSize inch $pizzaType pizza '
    'costs £${pizzaPrice.toStringAsFixed(2)}',
  );
}

void printNumbers(int n) { 
  for (int i = 1; i <= n; i++) { 
    stdout.write("$i "); 
  } 
} 