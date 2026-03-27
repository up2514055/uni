void main() {
  // maxNumber(2, 4);
  // daysInMonth(1);
  // print(multiplyBy2(1));
  // print(birthdayMessage("Dylan", 17));
  // print(speedCalculator(60, 60));
  // heartMonitor(81, 200);
  // basicCalculator(2, 2, "+");
  // print(isPrime(4));
  //customisedGreeting(1000);
  print(gcd(2, 2));
}

void maxNumber(int num1, int num2) {
  if (num1 > num2) {
    print(num1);
  } else {
    print(num2);
  }
}

void daysInMonth(int month) {
  switch (month) {
    case 12 || 10 || 8 || 7 || 5 || 3 || 1:
      print("31");
    case 11 || 9 || 6 || 4:
      print("30");
    case 2:
      print("28");
  }
}

int multiplyBy2(int x) => x * 2;

String birthdayMessage(String name, int ageLastYear) =>
    "happy birthday $name, you are ${ageLastYear + 1} years old !";

double speedCalculator(double distance, double time) => distance / time;

void heartMonitor(double age, double bpm) {
  if (age <= 20) {
    if (bpm > 170) print("High heart rate for 0-20!");
  } else if (age <= 40) {
    if (bpm > 155) print("High heart rate for 21-40!");
  } else if (age <= 60) {
    if (bpm > 140) print("High heart rate for 41-60!");
  } else if (age <= 80) {
    if (bpm > 130) print("High heart rate for 61-80!");
  } else {
    if (bpm > 100) print("High heart rate for 81+!");
  }
}

void basicCalculator(int num1, int num2, String operation) {
  if (operation == "-") {
    print(num1 - num2);
  } else if (operation == "*") {
    print(num1 * num2);
  } else if (operation == "/") {
    print(num1 ~/ num2);
  } else if (operation == "+") {
    print(num1 + num2);
  } else {
    print("Invalid operation");
  }
}

isPrime(int num) {
  if (num < 2) {
    return false;
  }
  for (int i = 2; i < num; i++) {

    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

void customisedGreeting(int time) {
  if (time >= 600 && time < 1200) {
    print("Have a great morning");
  } else if (time >= 1200 && time < 1700) {
    print("Have a great afternoon");
  } else {
    print("Have a good evening");
  }
}

int gcd(int a, int b) {
  if (a == b) {
    return a;
  } else if (a > b) {
    return gcd(b, a - b);
  } else if (b > a) {
    return gcd(a, b - a);
  } else {
    return gcd(a, b - a);
  }
}
