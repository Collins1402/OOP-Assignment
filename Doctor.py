class Hospital:
    def __init__(self, name, location, contact):
        self.name = name
        self.location = location
        self.contact = contact

    def display_hospital(self):
        print(f'Hospital Name: {self.name}')
        print(f'Location: {self.location}')
        print(f'Contact: {self.contact}')
        
class Doctor(Hospital):
        def __init__(self, name, location, contact, doctor_id, specialization):
            super().__init__(name, location, contact)
            self.doctor_id = doctor_id
            self.specialization = specialization

        def display_doctor(self):
            print(f'Doctor ID: {self.doctor_id}')
            print(f'Name: {self.name}')
            print(f'Specialization: {self.specialization}')
            print(f'Location: {self.location}')
            print(f'Contact: {self.contact}')

# 5. Additional Requirements:  
# a. Make the program user-friendly with input/output prompts.
# b. Document your code with comments to explain each class and method.

# Create Doctor Object
doctor = Doctor('Dr. Bob', 'Nairobi City', '0720704028', 'D001', 'Cardiologist')
print('Doctor Details:')

doctor.display_doctor()
print()
# HospitalManagementSystem()
# Output
# Hospital Details:
# Hospital Name: Getrude Hospital
# Location: Nairobi City
# Contact: 0701004028

# Patient Details:
# Patient ID: P001
# Name: Alice
# Age: 25
# Location: Nairobi City
# Contact: 0721711933

