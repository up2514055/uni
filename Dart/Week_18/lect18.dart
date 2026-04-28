void main() {
  Car myCar = Car('red', 10.0);
  print(myCar.colour);
  print(myCar.speed);
  myCar.colour = 'blue';
  print(myCar.colour);

  myCar.accelerate(10);
  print(myCar.speed);
  myCar.brake();
  print(myCar.speed);
  print(myCar);

  Ingredient pasta = Ingredient('Pasta', 200);
  Ingredient sauce = Ingredient('Sauce', 100);
  Recipe pastaRecipe = Recipe('Pasta');
  pastaRecipe.addIngredient(pasta);
  pastaRecipe.addIngredient(sauce);
  print(pastaRecipe.ingredients);
  print(pastaRecipe.totalCalories());
  print(pastaRecipe);

  KidsMeal happyMeal = KidsMeal('Cheeseburger', 'Slimer');
  happyMeal.toy = 'Ectomobile';
  print(happyMeal.toy); // Ectomobile
  Meal meal = Meal('Big Mac');
  print(meal); // Big Mac, chips and drink
  print(happyMeal); // Cheeseburger, chips and drink plus a Ectomobile
}

class Car {
  String colour;
  double speed;

  Car(this.colour, this.speed);

  void accelerate(double inc) {
    speed += inc;
  }

  void brake() {
    speed = 0;
  }

  String toString() {
    return 'Car(colour: $colour, speed: $speed)';
  }
}

class BankAccount {
  String owner;
  double _balance = 0.0;

  BankAccount(this.owner);

  void deposit(double amount) => _balance += amount;

  void withdraw(double amount) {
    if (_balance - amount >= 0) {
      _balance -= amount;
    }
  }

  // Not needed anymore as we have balance getter and setter below
  // double getBalance() => _balance;

  // double get balance {
  //   return _balance;
  // }

  // Getter using arrow syntax
  double get balance => _balance;

  void set balance(double amount) {
    if (amount >= 0) {
      _balance = amount;
    }
  }
}

class Ingredient {
  String name;
  int calories;

  Ingredient(this.name, this.calories);

  String toString() => '$name ($calories calories)';
}

class Recipe {
  String name;
  Set<Ingredient> ingredients = {};

  Recipe(this.name);

  // String toString() => '$name: $ingredients';

  String toString() {
    String result = '$name\n';
    for (Ingredient ingredient in ingredients) {
      result += '  $ingredient\n';
    }
    result += 'Total calories: ${totalCalories()}';
    return result;
  }

  void addIngredient(Ingredient ingredient) {
    ingredients.add(ingredient);
  }

  int totalCalories() {
    int total = 0;
    for (Ingredient ingredient in ingredients) {
      total += ingredient.calories;
    }
    return total;
  }
}

class Meal {
  String burger;

  Meal(this.burger);

  String toString() {
    return '$burger, chips and drink';
  }
}

class KidsMeal extends Meal {
  String toy = 'unknown';

  // KidsMeal(String burger, this.toy) : super(burger);

  KidsMeal(String burger, String toy) : super(burger) {
    this.toy = toy;
  }

  String toString() {
    return '${super.toString()} plus a $toy';
  }
}
