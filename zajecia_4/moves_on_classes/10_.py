class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student = Student(101, "Alice")

student.student_class = "10th Grade"

print("Attributes and values after adding student_class:")
print(vars(student))

delattr(student, "student_name")

print("\nAttributes and values after removing student_name:")
print(vars(student))
