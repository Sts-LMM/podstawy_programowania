class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def modify_student_name(self, new_name):
        self.student_name = new_name

    def modify_marks(self, new_marks):
        self.marks = new_marks

    def print_student_details(self, title="Student Details"):
        print(f"{title}:")
        print(f"Name: {self.student_name}")
        print(f"Marks: {self.marks}")
        print()

student = Student("Alice", 85)

student.print_student_details("Original Values")
student.modify_student_name("Bob")
student.modify_marks(90)
student.print_student_details("Modified Values")
