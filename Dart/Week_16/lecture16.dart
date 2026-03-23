import 'dart:io';

void main() {
  print('Uncomment the code with Ctrl+/ to run the examples.');

  // examReminder("Presilia", 14);
  // examReminder(date: 14, name: "Presilia");
  // examReminder(date: 14);

  // print('Trying the gradeStudent function:');
  // gradeStudent(10);
  // gradeStudent(2);
  // gradeStudent(-100);

  // print('Trying the boolToString function:');
  // print(boolToString(true));
  // print(boolToString(false));
  // print(boolToString(null));

  // print('Example of a try-catch block:');
  // print('Trying to parse the String "19th" to an int...');
  // try {
  //   var date = int.parse('19th');
  //   print('The date is $date');
  // } on FormatException {
  //   print('Caught a FormatException!');
  // } catch (e) {
  //   print('An unknown error occurred: $e');
  // }

  // loopExample1(); // Also try loopExample2(), loopExample3(), and loopExample4()

  // int number = getNumber();
  // print("The number is $number");
  examReminder(name: "dylan", date: 23);
}

void examReminder({String name = "Student", required int date}) {
  print(
    "Dear $name,\n"
    "Don't forget your exam on the ${date}th!",
  );
}

// The same function but name has a default value and date is required
// void examReminder({String name = "student", required int date}) {
//   print("Dear $name,\n"
//       "Don't forget your exam on the ${date}th!");
// }

// The same function but name is nullable and date is required
// void examReminder({
//   String? name,
//   required int date
// }) {
//   print("Dear ${name ?? 'student'},\n"
//       "Don't forget your exam on the ${date}th!");
// }

// Example of the arrow syntax
int multiplyBy2(int x) => x * 2;

void checkNumber(int number) {
  if (number > 0) {
    print("The number is positive.");
  } else if (number < 0) {
    print("The number is negative.");
  } else {
    print("The number is zero.");
  }
}

void gradeStudent(int score) {
  switch (score) {
    case 10:
      print('A');
    case 9:
    case 8:
      print('B');
    case 7 || 6:
      print('C');
    case 5 || 4 || 3:
      print('D');
    default:
      print('F');
  }
}

String boolToString(bool? value) {
  switch (value) {
    case true:
      return 'yes';
    case false:
      return 'no';
    // Without the default case, the compiler would complain
    // that the switch statement doesn't cover all cases
    default:
      return 'unknown';
  }
}

void loopExample1() {
  for (int i = 0; i < 5; i++) {
    print(i);
  }
}

void loopExample2() {
  int i = 0;
  while (i < 5) {
    print(i);
    i++;
  }
}

void loopExample3() {
  int i = 0;
  do {
    print(i);
    i++;
  } while (i < 5);
}

void loopExample4() {
  int i = 0;
  while (true) {
    i++;
    if (i == 2) {
      continue;
    } else if (i == 5) {
      break;
    }
    print(i);
  }
}

int getNumber() {
  while (true) {
    print('Enter a number:');
    String? input = stdin.readLineSync();
    if (input == null) {
      print('Nothing was entered.');
      continue;
    }
    int? number = int.tryParse(input);
    if (number == null) {
      print('Not a number.');
      continue;
    }
    return number;
  }
}
