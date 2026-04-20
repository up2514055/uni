import 'dart:io';
import 'dart:core';

//task 1
void main() {
  // stdout.write("Enter your email:");
  // String? input = stdin.readLineSync();

  // if (input == null) {
  //   stdout.writeln("No input provided.");
  //   return;
  // }

  // if (isValidEmail(input)) {
  //   stdout.writeln("Valid email address!");
  // } else {
  //   stdout.writeln("Invalid email.");
  // }
  // List<double> expenses = [10, 5.5, 8, 2,];
  // double max = 20;
  // print(checkExpenses(expenses, max));
  // List<double> temp1 = [10, 12.5, 14.0, 16.5, 15.0, 12.0];
  // print(weatherDifference(temp1));
  // List<double> temp2 = [1, 2, 3, 4, 5];
  // print(weatherDifference(temp2));
  // Set<String> food = {'milkshake', 'yoghurt', 'burger', 'banana milk'};
  // print(food);
  // print(removeMilk(food));
  // Map<String, List<int>> modules = {
  //   'Networks': [50, 100, 40],
  //   'Programming': [20, 40, 70],
  //   'Cyber Secruity': [20, 50, 80],
  // };

  // stdout.write("Enter a module: ");
  // String? input = stdin.readLineSync();

  // print(capMarks(input, modules));

  // Map<String, double> finestProduct = {
  //   'Milk': 20.10,
  //   'Bread': 15.40,
  //   'Water': 2.10,
  // };
  // priceRise(finestProduct);
  // stdout.write("Enter a word:");
  // String? input = stdin.readLineSync();
  // print(capitalize(input));
  var post = ['I love programming #cool'];
  print(extractHashtags(post));
}

bool isValidEmail(String email) {
  final lower = email.toLowerCase();
  List<String> parts = lower.split('@');

  if (parts.length != 2) return false;

  final local = parts[0];
  print(parts[0]);
  final domain = parts[1];
  print(parts[1]);

  final validPrefix = local.startsWith('up');
  final suffix = local.substring(2);
  final validNumber = suffix.length == 7;
  final validDomain = domain == 'myport.ac.uk';

  return validPrefix && validNumber && validDomain;
}
//final means it can only be assigned once and not changed after being assinged

//task 2

bool checkExpenses(List<double> expenses, double max) {
  for (int i = 0; i < expenses.length; i++) {
    if (expenses[i] > max) {
      return false;
    }
  }
  return true;
}

//task 3
double weatherDifference(List<double> temperatures) {
  return (temperatures.first - temperatures.last).abs();
}

//task 4
Set<String> removeMilk(Set<String> food) {
  Set<String> result = {};

  for (String item in food) {
    if (!item.contains('milk')) {
      result.add(item);
    }
  }
  return result;
}

//task 5
Map<String, List<int>> capMarks(
  String? module,
  Map<String, List<int>> modules,
) {
  if (module == null || module.isEmpty) {
    return modules;
  }

  if (!modules.containsKey(module)) {
    stdout.writeln("Module is not found");
    return modules;
  }
  List<int>? marks = modules[module];

  if (marks == null) {
    return modules;
  }
  for (int i = 0; i < marks.length; i++) {
    if (marks[i] > 40) {
      marks[i] = 40;
    }
  }
  return modules;
}

//task 6
void priceRise(Map<String, double> productPrices) {
  if (productPrices.containsKey('Milk')) {
    print('Price of milk is £${productPrices['Milk']!.toStringAsFixed(2)}');
  }

  productPrices['Milk'] = productPrices['Milk']! * 1.10;
  productPrices['Milk'] = double.parse(
    productPrices['Milk']!.toStringAsFixed(2),
  );
  print('New price of milk is £${productPrices['Milk']!.toStringAsFixed(2)}');
}

//task 7
String? capitalize(String? word) {
  if (word == null || word.isEmpty) {
    return word;
  }
  String first = word[0].toUpperCase();
  String lowercase = word.substring(1).toLowerCase();

  return first + lowercase;
}

//task 8
Set<String> extractHashtags(List<String> posts) {
  Set<String> hashtags = {};

  for (String post in posts) {
    List<String> words = post.split(' ');

    for (String word in words) {
      if (word.startsWith('#')) {
        if (word.endsWith('!') || word.endsWith('.') || word.endsWith(',')) {
          word = word.substring(0, word.length - 1);
        }

        hashtags.add(word);
      }
    }
  }
  return hashtags;
}
