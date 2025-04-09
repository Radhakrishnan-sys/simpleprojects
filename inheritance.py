class Car :
    def __init__ (self, name, model , year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.engine = True

    def service(self):
        print(f"{self.name} is currently running")

class Maruthi(Car):
    pass

class Benz(Car):
    pass

maruthi = Maruthi ("omni", "k310", "1992", "blue")

print(maruthi.color)

maruthi.service()
