class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_attributes(self):
        print("Attributes and their values of the Student class:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student = Student("S001", "Alice")
student.student_class = "Grade 10"
student.display_attributes()
