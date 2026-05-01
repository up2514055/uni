import 'dart:developer';

void main() {
  // Person alice = Person('Alice', 20);
  // alice.age = 21;
  // print('Alice is ${alice.age} years old');

  // print('Next year, Alice will be ${alice.ageNextYear()} years old');
  // print('Alice has a valid name: ${alice.hasValidName()}');

  // print(alice);
  // print(alice.runtimeType);
  Car mycar = Car('Red', 60);
  print(mycar);
  Person per = Person('Dyl', 15);
  print(per);
  Rectangle rec = Rectangle(10, 5, 10, 10);
  print(rec.getPermimeter());
  print(rec.getArea());
  print(Student('Dylan', 18, '0656565666'));
  Product peas = Product('Peas', 1.50, clubCardItem: true);
  Product sausages = Product('Sausages', 3.00, clubCardItem: true);
  Product milk = Product('Milk', 1.20);

  ShoppingCart cart = ShoppingCart(hasClubcard: true);

  cart.addProduct(peas);
  cart.addProduct(sausages);
  cart.addProduct(milk);

  print(cart);
}

//task 2
class Person {
  String name = 'unknown';
  int age = 0;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  bool isAdult() {
    if (age >= 18) {
      return true;
    } else {
      return false;
    }
  }

  int ageNextYear() {
    return age + 1;
  }

  bool hasValidName() {
    if (name.length > 2 && name.length < 100) {
      return true;
    } else {
      return false;
    }
  }

  String toString() {
    return 'Person(name: $name, age: $age, isAdult: ${isAdult()}';
  }
}

//task 4
class Student extends Person {
  int level = 4;
  String _phoneNumber;

  Student(String name, int age, this._phoneNumber) : super(name, age);

  void graduate() {
    level++;
  }

  String greet() => 'Hello, $name!';

  String get phoneNumber {
    String lastFourDigits = _phoneNumber.substring(6);
    return '***-***-$lastFourDigits';
  }

  void set phoneNumber(String phoneNumber) {
    if (phoneNumber.length == 10) {
      _phoneNumber = phoneNumber;
    }
  }

  String toString() {
    return 'name: $name, age: $age, level: $level, isAdult: ${isAdult()}';
  }
}

class Module {
  String name;
  int credits;

  Module(this.name, {this.credits = 20});
}

class Course {
  String name;
  List<Module> modules = [];
  int totalCredits = 0;
  int _maxCredits = 120;

  Course(this.name);

  void addModule(Module module) {
    if (totalCredits + module.credits <= maxCredits) {
      modules.add(module);
      totalCredits += module.credits;
    }
  }

  int get maxCredits => _maxCredits;

  String toString() {
    String output = 'Course name: $name, Modules:\n';
    for (Module module in modules) {
      output += '  ${module.name} (${module.credits} credits)\n';
    }
    output += 'Total credits: $totalCredits';
    return output;
  }
}

class Shape {
  double x = 0.0;
  double y = 0.0;

  Shape(this.x, this.y);

  void move(double dx, double dy) {
    x += dx;
    y += dy;
  }

  String toString() => 'x: $x, y: $y';
}

class Circle extends Shape {
  double radius = 0.0;

  // Circle(double x, double y, double radius) : super(x, y) {
  //   this.radius = radius;
  // }

  Circle(double x, double y, this.radius) : super(x, y);

  String toString() => '${super.toString()}, radius: $radius';
}

//task 3
class Rectangle extends Shape {
  double width;
  double height;

  Rectangle(double x, double y, this.width, this.height) : super(x, y);

  double getArea() {
    return width * height;
  }

  double getPermimeter() {
    return 2 * (width + height);
  }

  String toString() {
    return '${super.toString()}, width: $width, height: $height';
  }
}

//task 1
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

  double distance(double time) {
    return time * speed;
  }

  String toString() {
    return 'Car(colour: $colour, speed: $speed, distance: ${distance(1)}';
  }
}

//task 5
class Product {
  String name;
  double price;
  bool clubCardItem;

  Product(this.name, this.price, {this.clubCardItem = false});

  double calculateDiscount() {
    if (this.clubCardItem = true) {
      return price * 0.85;
    }
    return price;
  }

  String toString() {
    return 'Product(name: $name, price: £$price, clubcardItem: $clubCardItem)';
  }
}

class ShoppingCart {
  List<Product> products = [];
  bool hasClubcard;

  ShoppingCart({this.hasClubcard = false});

  void addProduct(Product product) {
    products.add(product);
  }

  double getTotal() {
    double total = 0;

    for (Product p in products) {
      if (hasClubcard && p.clubCardItem) {
        total += p.calculateDiscount();
      } else {
        total += p.price;
      }
    }
    return total;
  }

  String toString() {
    String output = 'Shopping cart:\n';
    for (Product p in products) {
      output += '${p.name} - £${p.price}';
      if (p.clubCardItem) {
        output += ' (Clubcard Item)';
      }
      output += '\n';
    }

    output += 'Total: £${getTotal().toStringAsFixed(2)}';
    return output;
  }
}
