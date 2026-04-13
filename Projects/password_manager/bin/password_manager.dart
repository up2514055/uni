import 'dart:math';
import 'dart:io';
import 'package:sqlite3/sqlite3.dart';

void main() {
  Database db = sqlite3.open('password.db');
  db.execute('''

    CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    password TEXT)

  ''');

  stdout.write("Please enter how long you would like your password: ");
  int length = int.parse(stdin.readLineSync()!);
  print(generatePassword(length));

  String password = generatePassword(length);
  print("Generated password: $password");

  stdout.write("What is this password for: ");
  String name = stdin.readLineSync()!;

  db.execute('INSERT into passwords (name, password) VALUES (?,?)', [
    name,
    password,
  ]);

  print("Password saved succesfully");
}

String generatePassword(int length) {
  String lowercase = 'abcdefghijklmnopqrstuvwxyz';
  String uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  String numbers = '0123456789';
  String symbols = '!@#\$%^&*()_+-=[]{}';
  String allChars = lowercase + uppercase + numbers + symbols;

  String password = '';
  var random = Random();

  for (int i = 0; i < length; i++) {
    password += allChars[random.nextInt(allChars.length)];
  }

  return password;
}
