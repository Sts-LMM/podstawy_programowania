class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()

print("Is student_instance an instance of Student?")
print(isinstance(student_instance, Student))  #True

print("\nIs marks_instance an instance of Marks?")
print(isinstance(marks_instance, Marks))  #True

print("\nIs Student a subclass of object?")
print(issubclass(Student, object))  #True

print("\nIs Marks a subclass of object?")
print(issubclass(Marks, object))  #True
