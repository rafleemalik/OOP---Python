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
        print(f"Annual Salary: ${self.get_annual_salary()}")
    
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

# ====== Subclass: Engineer ======
class Engineer(Employee):
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date, expertise: str, certifications: list):
        super().__init__(name, position, year_hired, salary, hire_date)
        self.__expertise = expertise
        self.__certifications = certifications
    
    def display_info(self):
        super().display_info()
        print(f"Expertise: {self.__expertise}")
        print(f"Certifications: {self.__certifications}")

# ====== Subclass: Intern ======
class Intern(Employee):
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date, duration: int, mentor: str):
        super().__init__(name, position, year_hired, salary, hire_date)
        self.__duration = duration
        self.__mentor = mentor
    
    def display_info(self):
        super().display_info()
        print(f"Internship Duration: {self.__duration} months")
        print(f"Mentor: {self.__mentor}")

# ====== CRUD Functions ======
employees = []

def create_employee():
    emp_type = input("Enter Employee Type (Manager/Engineer/Intern): ").strip().lower()
    name = input("Enter Employee Name: ")
    position = input("Enter Position: ")
    year_hired = int(input("Enter Year Hired: "))
    salary = float(input("Enter Salary: "))
    hire_date = date.fromisoformat(input("Enter Hire Date (YYYY-MM-DD): "))
    
    if emp_type == "manager":
        department = input("Enter Department: ")
        team_size = int(input("Enter Number of Team Members: "))
        team = {}
        for _ in range(team_size):
            member_name = input("Enter Team Member Name: ")
            role = input("Enter Team Member Role: ")
            team[member_name] = role
        employee = Manager(name, position, year_hired, salary, hire_date, department, team)
    elif emp_type == "engineer":
        expertise = input("Enter Expertise: ")
        certifications = input("Enter Certifications (comma separated): ").split(', ')
        employee = Engineer(name, position, year_hired, salary, hire_date, expertise, certifications)
    elif emp_type == "intern":
        duration = int(input("Enter Internship Duration (months): "))
        mentor = input("Enter Mentor Name: ")
        employee = Intern(name, position, year_hired, salary, hire_date, duration, mentor)
    else:
        print("Invalid employee type!")
        return
    
    employees.append(employee)
    print("Employee added successfully!")

def read_employees():
    if not employees:
        print("No employees found.")
    for emp in employees:
        emp.display_info()
        print("----------------------")

# ====== Main Program ======
if __name__ == "__main__":
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
