class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

employees = [
    Employee("ADAMS", "E7876", 50000, "ACCOUNTING"),
    Employee("JONES", "E7499", 45000, "RESEARCH"),
    Employee("MARTIN", "E7900", 50000, "SALES"),
    Employee("SMITH", "E7698", 55000, "OPERATIONS")
]

for emp in employees:
    print("Before department change:")
    emp.print_employee_details()
    emp.emp_assign_department("HR")
    print("After department change:")
    emp.print_employee_details()
    print("Salary after overtime:", emp.calculate_emp_salary(55))
    print("-" * 30)
