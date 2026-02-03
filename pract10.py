from graphix import Point

class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"

def test_point():

    my_point = MyPoint(100, 50)
    print("my_point's x coordinate is", my_point.x)  # 100
    print("my_point's y coordinate is", my_point.y)  # 50
    my_point.move(10, -20)
    print("my_point's x coordinate is", my_point.x)  # 110
    print("my_point's y coordinate is", my_point.y)  # 30

#test_point()

class Square:
    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.x + side, p1.y + side)
        self.outline_color = "black"
        self.fill_color = "white"


    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)
    
    def get_permitter(self):
        return 4 * self.side
    
    def get_area(self):
        return self.side ** 2
    
    def get_center(self):
        center_x = self.p1.x + self.side / 2
        center_y = self.p1.y + self.side / 2
        return MyPoint(center_x, center_y)

    def __str__(self):
        return f"Square({self.p1}, {self.p2})"
    
def test_square():
    my_square = Square(MyPoint(10, 100), 10)
    print(my_square)
    print(f"square's fill color is {my_square.fill_color}")
    print(f"square's outline color is {my_square.outline_color}")
    my_square.fill_color = "red"
    print("Changing fill color...")
    print("Squares fill color is", my_square.fill_color)
    my_square.outline_color = "blue"
    print("Changing outline color...")
    print("Squares outline color is", my_square.outline_color)

#test_square()

class MyCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = int(radius)
        self.outline_color = str("black")
        self.fill_color = str("white")

    def move(self, dx, dy):
        self.center.x += dx
        self.center.y += dy

    def __str__(self):
        return f"The centre of the circle is {self.center}, the radius is {self.radius}, the fill colour is {self.fill_color}, and outline colour is {self.outline_color}"

def test_circle():
    my_circle = MyCircle(MyPoint(10, 100), 20)
    print(my_circle)
    my_circle.fill_colour = 'red'
    my_circle.outline_colour = 'blue'
    print(my_circle)

    my_circle.move(-10, 20)
    print(my_circle)

#test_circle()

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance =+ amount
        return(f"Depositing £{amount:.2f} ...")
        return(f"Bank account for {self.name} has £{self.balance}")
    
    def withdrawal(self, amount):
        if self.balance >= amount:
          self.balance -= amount
        return(f"Withdrawaing £{amount:.2f} ...")
        return(f"Bank account for {self.name} has £{self.balance}")

    def __str__(self):
        return f"Account holder's name is {self.name} \nAccount balance is £{self.balance}"
    
def test_account():
    my_account = BankAccount("dylan")
    print(my_account)
    my_account.deposit(100)
    my_account.withdrawal(50)
    my_account.withdrawal(100)

#test_account()

class HotelRoom:
    def __init__(self,room_num):
        self.room_num = int(room_num)
        self.name = ""
    
    def check_in(self, name):
        self.name = name
        return(f"Checking in {name} to room {self.room_num}...")

    def check_out(self):
        return(f"Checking out {self.name} from room {self.room_num}...")
        self.name = ""
    
        
    def is_occupied(self):
        if self.name == "":
            return False
        else:
            return True

    def __str__(self):
        if self.is_occupied() == True:
            return f"Room {self.room_num} is occupied by {self.name}."
        else:
            return f"Room {self.room_num} is vacant."

def test_hotel_room():
    room101 = HotelRoom(101)
    print(room101)
    room101.check_in("Dylan")
    print(room101)
    room101.check_out()
    print(room101)

#test_hotel_room()

class Gradebook:
    def __init__(self):
        self.grades = {}
    
    def add_grade(self, module_name, grade):
        self.grades[str(module_name)] = grade

    def remove_grade(self, module_name):
        del self.grades[module_name]
    
    def get_grade(self, module_name):
        return(f"{module_name} grade is {self.grades[str(module_name)]}")

    def __str__(self):
        if not self.grades:
            return "No grades recorded."
        result = "Gradebook:\n"
        for module, grade in self.grades.items():
            result += f"{module}: {grade}\n"
        return result
    
def test_grade_book():
    my_gradebook = Gradebook()
    print(my_gradebook)
    my_gradebook.add_grade("Maths", 85)
    my_gradebook.add_grade("Science", 90)
    my_gradebook.get_grade("Maths")
    print(my_gradebook)


#test_grade_book()
