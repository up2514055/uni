import 'dart:math';
import 'dart:io';

void main() {
  int randomNumber = Random().nextInt(100) + 1;
  int guess = 0;

  while (guess != randomNumber) {
    stdout.write('Guess (1-100): ');
    guess = int.parse(stdin.readLineSync()!);

    if (guess < randomNumber)
      print('Too low');
    else if (guess > randomNumber)
      print('Too high');
    else
      print('Correct');
  }
}
