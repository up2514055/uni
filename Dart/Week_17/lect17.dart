void main() {
  // stringDemo1(); // Uncomment to run

  // stringDemo2(); // Uncomment to run

  // listDemo(); // Uncomment to run

  // iteratingLists(); // Uncomment to run

  // multiDimensionalLists(); // Uncomment to run

  setDemo(); // Uncomment to run
}

void setDemo() {
  Set<String> modules = {'Programming', 'Networks', 'Core Computing'};
  modules.add('Database');
  modules.add('Programming'); // No effect, 'Programming' is already in the set
  print(modules); // {Programming, Networks, Core Computing, Database}

  modules.remove('Networks'); // Removes 'Networks'
  modules.remove('Databases'); // No effect, 'Databases' is not in the set
  print(modules); // {Programming, Core Computing, Database}

  print('Is "Programming" in the set? ${modules.contains('Programming')}');

  print('Modules:');
  for (String module in modules) {
    print(module);
  }
}

void stringDemo1() {
  String txt = 'Hello, World!';
  print('The character at index 7 is: ${txt[7]}'); // W
  print('Length of greeting: ${txt.length}'); // 13

  String news = 'Breaking News: Moon landing!';
  print(news);
  print('The index of "Moon" in the news is: ${news.indexOf('Moon')}'); // 15
  print('The news contains "News": ${news.contains('News')}'); // true
  print('The news contains "Moon": ${news.contains('Moon')}'); // true
  print('The news contains "Mars": ${news.contains('Mars')}'); // false
  print(
      'The news starts with "Breaking": ${news.startsWith('Breaking')}'); // true
  print('The news ends with "landing!": ${news.endsWith('landing!')}'); // true
}

void stringDemo2() {
  String fruits = '🍎,🍌:🍇,🍊;🍐';
  print('Fruits are: $fruits');
  int index = fruits.indexOf('🍇');
  String untilGrape = fruits.substring(0, index);
  print('Until grape: $untilGrape'); // 🍎,🍌:

  List<String> split = 'Hi, Hi; Hi'.split(', ');
  print('splitting with string: $split'); // ['Hi', 'Hi; Hi']
  split = 'Hi, Hi; Hi'.split(RegExp(r'[,;]+ '));
  print('splitting with RegExp: $split'); // ['Hi', 'Hi', 'Hi']

  List<String> colours = ['red', 'white', 'blue'];
  String flag = colours.join(' ');
  print('The flag is: $flag'); // The flag is: red white blue
}

void listDemo() {
  List<String> customers = [
    'Ştefan',
    'Amy',
    'Jamila',
    'Amy',
  ];
  print('Customers: $customers'); // Customers: [Ştefan, Amy, Jamila, Amy]
  print('Customer at index 2: ${customers[2]}'); // Customer at index 2: Jamila
  // print('Customer at index 4: ${customers[4]}'); // Error

  List<int> filledList = List.filled(5, 0);
  print('filledList: $filledList'); // filledList: [0, 0, 0, 0, 0]
  filledList[2] = 3;
  print('filledList after update: $filledList'); // filledList: [0, 0, 3, 0, 0]

  customers[2] = 'Zeinab';
  print('3rd customer is now: ${customers[2]}'); // 3rd customer is now: Zeinab
  int numOfCustomers = customers.length;
  String lastOne = customers[numOfCustomers - 1];
  print('Last customer is: $lastOne');
  // Last customer is: Amy

  print('First customer is: ${customers.first}');
  // First customer is: Ştefan
  print('Last customer is: ${customers.last}');
  // Last customer is: Amy

  customers.add('José');
  print('After adding José: $customers'); // [Ştefan, Amy, Zeinab, Amy, José]

  customers.insert(2, 'Mohammed');
  print(
      'After inserting Mohammed: $customers'); // [Ştefan, Amy, Mohammed, Zeinab, Amy, José]

  customers.remove('Amy');
  print(
      'After removing Amy: $customers'); // [Ştefan, Mohammed, Zeinab, Amy, José]
}

void iteratingLists() {
  List<int> marks = [77, 90, 64, 92, 0];
  print('Before: $marks'); // Before: [77, 90, 64, 92, 0]
  for (int i = 0; i < marks.length; i++) {
    // We can't have more than 100%
    if (marks[i] >= 90) {
      marks[i] = 100;
    } else {
      marks[i] += 10;
    }
  }
  print('After +10: $marks'); // After +10: [87, 100, 74, 100, 10]

  int sum = 0;
  for (int mark in marks) {
    sum += mark;
  }
  double average = sum / marks.length;
  print('Average mark is: $average'); // Average mark is: 74.2
}

void multiDimensionalLists() {
  // A 3x3 matrix (2D list of lists)
  List<List<int>> matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  print('The matrix is: $matrix');
  print('The first row is: ${matrix[0]}'); // The first row is: [1, 2, 3]
  print(
      'The matrix at (1, 2) is: ${matrix[1][2]}'); // The matrix at (1, 2) is: 6

  // Another 2D list of lists
  List<List<String>> foodDiary = [
    ['🧇', '🧆', '🥗'], // Monday
    ['🍳', '🍛'], // Tuesday
    ['🥯', '🥘', '🥪'], // Wednesday
    ['🍩', '🌯', '🍲'], // Thursday
    ['🧇', '🌮', '🍣'], // Friday
    ['🥞', '🥧', '🍔', '🍟'], // Saturday
    ['🍪', '🥪', '🍝'] // Sunday
  ];
  print('The food diary is: $foodDiary');
  print("Saturday's lunch: ${foodDiary[6][1]}"); // Sunday's lunch: 🥪
  print("Updating Saturday's index 1 meal to 🍕");
  print('Before: ${foodDiary[5]}'); // Before: [🥞, 🥧, 🍔, 🍟]
  foodDiary[5][1] = '🍕';
  print('After: ${foodDiary[5]}'); // After: [🥞, 🍕, 🍔, 🍟]
}