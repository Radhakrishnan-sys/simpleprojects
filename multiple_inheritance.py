class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Patient(Person):  # Inherits from Person
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

class InPatient(Patient):  # Inherits from Patient
    def __init__(self, name, age, patient_id, room_number):
        super().__init__(name, age, patient_id)
        self.room_number = room_number

    def get_details(self):
        return f"{self.name}, Age: {self.age}, ID: {self.patient_id}, Room: {self.room_number}"




class Doctor:
    def diagnose(self):
        return "Diagnosing patient..."

class RobotAssistant:
    def assist(self):
        return "Providing assistance and replying to patient queries."

class MedicalBot(Doctor, RobotAssistant):  # Multiple Inheritance
    def operate(self):
        return self.diagnose() + " " + self.assist()

# Multilevel
inpatient = InPatient("Amit", 32, "P102", "Room 204")
print(inpatient.get_details())

# Multiple
bot = MedicalBot()
print(bot.operate())



