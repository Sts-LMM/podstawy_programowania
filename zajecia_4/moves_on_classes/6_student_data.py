def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    
    if student_name:
        print(f"Student Name: {student_name}")
        
    if student_class:
        print(f"Student Class: {student_class}")

print("Example 1:")
student_data(101)
print("\nExample 2:")
student_data(102, student_name="Alice")
