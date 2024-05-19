class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_student_class(self, student_class):
        self.student_class = student_class

    def remove_student_name(self):
        del self.student_name

    def display_attributes(self, title="Student Attributes"):
        print(f"{title}:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")
        print()

student = Student(101, "Alice")

student.add_student_class("Grade 10")
student.display_attributes("Initial Attributes")
student.remove_student_name()
student.display_attributes("Attributes after removing student_name")
