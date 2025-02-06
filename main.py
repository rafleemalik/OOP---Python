from datetime import date

# ====== Parent Class: Employee ======
class Employee:
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date):
        self.__name = name
        self.__position = position
        self.__year_hired = year_hired
        self.__salary = salary
        self.__hire_date = hire_date
    
    def display_info(self):
        print(f"Employee: {self.__name}, Position: {self.__position} (Hired: {self.__year_hired})")
        print(f"Salary: ${self.__salary}")
        print(f"Hire Date: {self.__hire_date}")
    
    def get_annual_salary(self):
        return self.__salary * 12
    
    # Getter dan Setter
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

# ====== Subclass: Manager ======
class Manager(Employee):
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date, department: str, team: dict):
        super().__init__(name, position, year_hired, salary, hire_date)
        self.__department = department
        self.__team = team
    
    def display_info(self):
        super().display_info()
        print(f"Department: {self.__department}")
        print(f"Team Members: {self.__team}")

# ====== CRUD Functions ======
employees = []

def create_employee():
    name = input("Enter Employee Name: ")
    position = input("Enter Position: ")
    year_hired = int(input("Enter Year Hired: "))
    salary = float(input("Enter Salary: "))
    hire_date = date.fromisoformat(input("Enter Hire Date (YYYY-MM-DD): "))
    employee = Employee(name, position, year_hired, salary, hire_date)
    employees.append(employee)
    print("Employee added successfully!")

def read_employees():
    if not employees:
        print("No employees found.")
    for emp in employees:
        emp.display_info()

def update_employee():
    name = input("Enter the name of the employee to update: ")
    for emp in employees:
        if emp.get_name() == name:
            new_salary = float(input("Enter new salary: "))
            emp.set_salary(new_salary)
            print("Salary updated successfully!")
            return
    print("Employee not found.")

def delete_employee():
    name = input("Enter the name of the employee to delete: ")
    global employees
    employees = [emp for emp in employees if emp.get_name() != name]
    print("Employee deleted successfully!")

# ====== Main Program ======
if __name__ == "__main__":
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")
