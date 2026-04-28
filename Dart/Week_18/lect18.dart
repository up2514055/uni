void main() {
  Motorcycle motor = Motorcycle("red", 10);
  print(motor.colour);
  print(motor.speed);
  motor.speed = 15;
  print(motor.speed);
  print(motor);
  /////////////////
  BankAccount bank = BankAccount('Dylan');
  bank._balance = 100;
  print(bank._balance);
  String sugar = Ingredient('Sugar', calories)
}

class Car {
  String colour = '';
  double speed = 0.0;
  //instance variables are seen as above

  Car(String inputColour, double inputSpeed) {
    colour = inputColour;
    speed = inputSpeed;
  }
}
//constructors are used to initalise objects they can accept parameters too
//constuctors have the same name as the class
//need to use "this" to distigush them from paramters as seen below

class Bike {
  String colour = '';
  double speed = 0.0;

  Bike(String colour, double speed) {
    this.colour = colour;
    this.speed = speed;
  }
}

class Motorcycle {
  String colour;
  double speed;

  Motorcycle(this.colour, this.speed);

  String toString() {
    return 'Motorcycle(colour: $colour, speed: $speed)';
  }
}
//instance varibles to be assingedto the values passed into the constructor
//Using an _ makes private instance vairables like python as seen below

class BankAccount {
  String owner;
  double _balance = 0.0;

  // Constructor
  BankAccount(this.owner);

  // Getter
  double get balance => _balance;

  // Setter
  void set balance(double amount) {
    if (amount >= 0) {
      _balance = amount;
    }
  }
}

class Ingredient {
  String name;
  int calories;

  //constructor
  Ingredient(this.name, this.calories);
  String toString() => '$name ($calories calories)';
}

class Recipe {
  String name;
  Set<Ingredient> ingredients = {};

  Recipe(this.name);

  String toString() => 'name: $ingredients';
}
//to use inheritence in dart we use the exstends keyword as seen below
class Meal {
  String burger;

  Meal(this.burger);
}

class KidsMeal extends Meal{
  String toy = '';
  KidsMeal(String burger) : super(burger){
    this.toy = toy;
  }
}