# student.py

class Student:
    allowed_courses = [
        "Computer Science",
        "Software Engineering",
        "Networks and Security",
        "Data Science",
        "Cybersecurity",
        "Computing"
    ]

    def __init__(self, name, up_number, course, placement=False):
        self.name = name
        self._up_number = up_number

        # validate course
        if course in Student.allowed_courses:
            self._course = course
        else:
            self._course = "Computer Science"

        # starting year rule
        self._year = 3 if placement else 1

    @property
    def up_number(self):
        return self._up_number

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, new_course):
        if new_course in Student.allowed_courses:
            self._course = new_course

    @property
    def year(self):
        return self._year

    def progress_year(self):
        if self._year < 4:
            self._year += 1

    def __str__(self):
        return (
            f"Student {self.name} (UP{self.up_number})\n"
            f"Course: {self.course}\n"
            f"Year: {self.year}"
        )


class PlacementStudent(Student):
    def __init__(self, name, up_number, course, company):
        super().__init__(name, up_number, course, placement=True)
        self._company = company


    @property
    def company(self):
        return self._company
    
    
    
    
    def __str__(self):
        return (
            f"Placement Student {self.name} (UP{self.up_number})\n"
            f"company: {self.company}\n"
            f"Year: {self.year}"
        )


def test_students():
    s1 = Student("Dylan Mazur", "2514055", "Cybersecurity")
    s2 = PlacementStudent("Alex", "2519999", "Data Science", "Apple")

    print(s1)
    print()
    print(s2)

    print("\nChanging course for s1...")
    s1.course = "Computing"
    print(s1)

    print("\nProgressing s1 year...")
    s1.progress_year()
    s1.progress_year()
    s1.progress_year()
    s1.progress_year()  # should not go past 4
    print(s1)

    print("\nTrying to change UP number (should fail if uncommented)...")
    # s1.up_number = "1234567"  # This should raise an AttributeError


test_students()
