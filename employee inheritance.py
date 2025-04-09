class Employees :
    def __init__ (self, name, emp_id , year, salary):
        self.name = name
        self.emp_id = emp_id
        self.year = year
        self.salary = salary
        self.is_employed = True

    def service(self):
        print(f"{self.name} is currently working")

class Amazon(Employees):
    pass

class flipkart(Employees):
    pass

employee1 = Amazon ("RK", "QW123", "2025", "50,000")
employee2= flipkart("Sasi", "QW153", "2025", "50,000")

employee1.service()
print(employee2.salary)

