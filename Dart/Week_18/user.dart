void main() {
  User user = User('Dylan');
  print(user);
  print(user.login('Password123') ? 'Login successful' : 'Login unsuccessful');
  print(
    user.changePassword('Password123', 'NewPass')
        ? 'Password changed'
        : 'Password change failed',
  );
  //used ? and : instead of an if statement and an else clause.
  print(user.login('Password123') ? 'Login successful' : 'Login unsuccessful');
  print(user.login('NewPass') ? 'Login succesful' : 'Login unsucessful');
}

class User {
  String username;
  String _password = 'Password123';

  //constructor
  User(this.username);

  bool changePassword(String password, String newPassword) {
    if (password == _password) {
      _password = newPassword;
      return true;
    } else {
      return false;
    }
  }

  bool login(String inputPassword) {
    return inputPassword == _password;
  }

  String toString() {
    return 'username: $username';
  }
}
