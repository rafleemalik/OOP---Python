from datetime import date

# ====== Parent Class: Employee ======
class Employee:
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date):
        """Constructor untuk Employee"""
        self.name = name  
        self.position = position  
        self.year_hired = year_hired  
        self.salary = salary  
        self.hire_date = hire_date  
    
    def display_info(self):
        """Menampilkan informasi pegawai"""
        print(f"Employee: {self.name}, Position: {self.position} (Hired: {self.year_hired})")
        print(f"Salary: ${self.salary}")
        print(f"Hire Date: {self.hire_date}")
    
    def get_annual_salary(self):
        """Mengembalikan gaji tahunan"""
        return self.salary * 12

# ====== Subclass: Manager ======
class Manager(Employee):
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date, department: str, team: dict):
        """Constructor untuk Manager"""
        super().__init__(name, position, year_hired, salary, hire_date)  
        self.department = department  
        self.team = team  
    
    def display_info(self):
        """Menampilkan informasi manager"""
        super().display_info()  
        print(f"Department: {self.department}")
        print(f"Team Members: {self.team}")

# ====== Subclass: Engineer ======
class Engineer(Employee):
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date, expertise: str, certifications: list):
        """Constructor untuk Engineer"""
        super().__init__(name, position, year_hired, salary, hire_date)  
        self.expertise = expertise  
        self.certifications = certifications  
    
    def display_info(self):
        """Menampilkan informasi engineer"""
        super().display_info()  
        print(f"Expertise: {self.expertise}")
        print(f"Certifications: {self.certifications}")

# ====== Subclass: Intern ======
class Intern(Employee):
    def __init__(self, name: str, position: str, year_hired: int, salary: float, hire_date: date, duration: int, mentor: str):
        """Constructor untuk Intern"""
        super().__init__(name, position, year_hired, salary, hire_date)  
        self.duration = duration  
        self.mentor = mentor  
    
    def display_info(self):
        """Menampilkan informasi intern"""
        super().display_info()  
        print(f"Internship Duration: {self.duration} months")
        print(f"Mentor: {self.mentor}")

# ====== Main Program ======
if __name__ == "__main__":
    # Membuat objek Manager
    manager = Manager(
        "Alice Johnson", "Project Manager", 2015, 85000.0, date(2015, 6, 10),
        "IT Department", {"Bob": "Developer", "Charlie": "Designer"}
    )
    
    # Membuat objek Engineer
    engineer = Engineer(
        "David Smith", "Software Engineer", 2018, 75000.0, date(2018, 8, 15),
        "Backend Development", ["AWS Certified", "Scrum Master"]
    )
    
    # Membuat objek Intern
    intern = Intern(
        "Emma Brown", "Intern - Data Science", 2024, 1500.0, date(2024, 1, 10),
        6, "Dr. James Wilson"
    )

    # ====== Menampilkan Informasi Manager ======
    print("====== Manager Information ======")
    manager.display_info()
    print(f"Annual Salary: ${manager.get_annual_salary()}")
    
    # ====== Menampilkan Informasi Engineer ======
    print("\n====== Engineer Information ======")
    engineer.display_info()
    print(f"Annual Salary: ${engineer.get_annual_salary()}")
    
    # ====== Menampilkan Informasi Intern ======
    print("\n====== Intern Information ======")
    intern.display_info()
    print(f"Annual Salary: ${intern.get_annual_salary()}")
