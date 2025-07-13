class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def display_all_employees(self):
        print(f"\nEmployees in {self.department_name} Department:")
        for emp in self.employees:
            emp.display_details()
        print(f"Total Salary Expenditure: {self.total_salary()}")

if __name__ == "__main__":
    dept = Department("Finance")

    while True:
        print("\n1. Add Employee\n2. Display Employees\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            emp_id = input("Employee ID: ")
            salary = float(input("Salary: "))
            emp = Employee(name, emp_id, salary)
            dept.add_employee(emp)
            print(f"{name} added to {dept.department_name}.")

        elif choice == '2':
            dept.display_all_employees()

        elif choice == '3':
            break
        else:
            print("Invalid option.")
