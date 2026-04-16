class Staff:
    hospital_name = "LifeCare Hospital"
    def __init__(self, name, role, id_number):
        self.name = name
        self.role = role
        self.id_number = id_number

    def show_details(self):
        print(f"Staff: {self.name} | ID: {self.id_number} | Role: {self.role}")

    def perform_task(self):
        if self.role == "Doctor":
            print(f"{self.name} is checking patients.")
        elif self.role == "Nurse":
            print(f"{self.name} is measuring vital signs.")
        elif self.role == "Receptionist":
            print(f"{self.name} is booking an appointment.")
        else:
            print(f"{self.name} is performing administrative duties.")

staff1 = Staff("Lara Chbib", "Doctor", 101)
staff2 = Staff("Malak", "Nurse", 202)
staff3 = Staff("Sarah", "Receptionist", 303)

print(f"Welcome to {Staff.hospital_name}")

staff1.show_details()
staff2.show_details()
staff3.show_details()

staff1.perform_task()
staff2.perform_task()
staff3.perform_task()
class User:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def login(self):
        print(f"{self.name} has logged into the system.")

class Doctor(User):
    def perform_duty(self):
        print(f"Dr. {self.name} is diagnosing patients and prescribing medication.")

class Nurse(User):
    def perform_duty(self):
        print(f"Nurse {self.name} is monitoring patients and recording vitals.")

class Patient(User):
    def perform_duty(self):
        print(f"Patient {self.name} is viewing their medical records.")

doc = Doctor("Lara Chbib", 101)
nur = Nurse("Malak", 202)
pat = Patient("Hasan", 505)

doc.login()
doc.perform_duty()

nur.login()
nur.perform_duty()

pat.login()
pat.perform_duty()
class AdminManager(User):
    def perform_duty(self):
        print(f"Admin {self.name} is managing the system and monitoring operations.")

adm = AdminManager("Adam", 1)

adm.login()
adm.perform_duty()