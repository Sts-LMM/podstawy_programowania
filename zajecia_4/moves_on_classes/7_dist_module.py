class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student_instance = Student(1, "Alice")

print("Type of the Student class:")
print(type(Student))

print("\n__dict__ attribute keys of the Student class:")
print(Student.__dict__.keys())

print("\nValue of the __module__ attribute of the Student class:")
print(Student.__module__)
