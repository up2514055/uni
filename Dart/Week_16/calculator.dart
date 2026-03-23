void main(List<String> arguments) {
  basicCalculator(
    int.parse(arguments[1]),
    int.parse(arguments[2]),
    arguments[0],
  );
}

void basicCalculator(int num1, int num2, String operation) {
  if (operation == "subtract") {
    print(num1 - num2);
  } else if (operation == "times") {
    print(num1 * num2);
  } else if (operation == "divide") {
    print(num1 ~/ num2);
  } else if (operation == "addition") {
    print(num1 + num2);
  } else {
    print("Invalid operation");
  }
}
