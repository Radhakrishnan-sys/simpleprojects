class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):  # Inherits from Person
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

class Manager(Employee):  # Inherits from Employee
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size

    def get_details(self):
        return (f"Manager: {self.name}, Age: {self.age}, "
                f"ID: {self.employee_id}, Dept: {self.department}, "
                f"Team Size: {self.team_size}")





class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Fruit(Item):
    def get_category(self):
        return "This is a fruit."

class Vegetable(Item):
    def get_category(self):
        return "This is a vegetable."

class Organic:
    def is_organic(self):
        return "Certified Organic - No chemicals used."

# Multiple Inheritance
class OrganicFruit(Fruit, Organic):
    def get_details(self):
        return (f"{self.name}: ${self.price} - " +
                self.get_category() + " " +
                self.is_organic())

class OrganicVegetable(Vegetable, Organic):
    def get_details(self):
        return (f"{self.name}: ${self.price} - " +
                self.get_category() + " " +
                self.is_organic())



#Multiple inheritance
apple = OrganicFruit("Apple", 1.5)
print(apple.get_details())

carrot = OrganicVegetable("Carrot", 0.8)
print(carrot.get_details())

#Multi-level inheritance
# Multilevel
manager = Manager("Amit", 32, "E102", "IT")
print(manager.get_details())





