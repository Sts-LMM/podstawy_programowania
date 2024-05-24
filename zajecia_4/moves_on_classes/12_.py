class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def display_attributes(self):
        attributes = vars(self)
        for attribute, value in attributes.items():
            print(attribute + ": " + str(value))

student = Student(101, "Alice")
student.student_class = "10th Grade"
student.display_attributes()
