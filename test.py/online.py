class OnlineCourse:

    max_enrolled = 5

    def __init__(self,title, instructor):
        self.title = title
        self.instructor = instructor
        self._student_enrolled = 0


    @property #getter
    def student_enrolled(self):
        return self._student_enrolled
    

    @student_enrolled.setter
    def student_enrolled(self, new_value):
        if 0 <= new_value <= self.max_enrolled:
            self._student_enrolled = new_value

    def entrol_students(self):
        self.student_enrolled += 1

    def unenrol_students(self):
        if self.student_enrolled > 0:
            self.student_enrolled -= 1

    def __str__(self):
        return f"{self.title} by {self.instructor} - {self.student_enrolled} students enrolled"
    


def test_online_course():
    course1 = OnlineCourse("CS", "Mustfah")
    course2 = OnlineCourse("PE", "Theo")

    course1.entrol_students()
    print(course1)
    course2.entrol_students()
    print(course2)

    course1.unenrol_students()
    print(course1)
    course2.unenrol_students()
    print(course2)

    course1.entrol_students()
    course1.entrol_students()
    course1.entrol_students()
    course1.entrol_students()
    course1.entrol_students()
    course1.entrol_students()
    course1.entrol_students()
    print(course1)
test_online_course()