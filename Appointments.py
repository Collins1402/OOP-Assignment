class Hospital:
    def __init__(self, name, location, contact):
        self.name = name
        self.location = location
        self.contact = contact

    def display_hospital(self):
        print(f'Hospital Name: {self.name}')
        print(f'Location: {self.location}')
        print(f'Contact: {self.contact}')
        
class appointments(Hospital):
    def __init__(self, name, location, contact, patient_id, age, doctor_id, specialization, appointment_date, appointment_time):
        super().__init__(name, location, contact)
        self.patient_id = patient_id
        self.age = age
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

    def display_appointment(self):
        print(f'Patient ID: {self.patient_id}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Location: {self.location}')
        print(f'Contact: {self.contact}')
        print(f'Doctor ID: {self.doctor_id}')
        print(f'Specialization: {self.specialization}')
        print(f'Appointment Date: {self.appointment_date}')
        print(f'Appointment Time: {self.appointment_time}')

# Create Appointment Object
appointment = appointments('Alice', 'Nairobi City', '0721711933', 'P001', 25, 'D001', 'Cardiologist', '2021-02-01', '10:00 AM')
print('Appointment Details:')
appointment.display_appointment()
print()
# Output
# Appointment Details:
# Patient ID: P001
# Name: Alice
# Age: 25
# Location: Nairobi City
# Contact: 0721711933
# Doctor ID: D001
# Specialization: Cardiologist
# Appointment Date: 2021-02-01
# Appointment Time: 10:00 AM
