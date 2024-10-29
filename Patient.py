# Define Hospital
class Hospital:
    def __init__(self, name, location, contact):
        self.name = name
        self.location = location
        self.contact = contact

    def display_hospital(self):
        print(f'Hospital Name: {self.name}')
        print(f'Location: {self.location}')
        print(f'Contact: {self.contact}')

class Patient(Hospital):
        def __init__(self, name, location, contact, patient_id, age):
            super().__init__(name, location, contact)
            self.patient_id = patient_id
            self.age = age

        def display_patient(self):
            print(f'Patient ID: {self.patient_id}')
            print(f'Name: {self.name}')
            print(f'Age: {self.age}')
            print(f'Location: {self.location}')
            print(f'Contact: {self.contact}')

# Create Patient Object
patient = Patient('Alice', 'Nairobi City', '0721711933', 'P001', 25)

print('Patient Details:')

patient.display_patient()
print()