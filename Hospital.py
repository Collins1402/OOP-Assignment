''''Design and implement a system of your choice using Python. The goal is to apply key
Object-Oriented Programming (OOP) concepts such as classes, objects, inheritance,
polymorphism, encapsulation, and abstraction in a practical project.
Instructions:
1. Select a System to Build:
2. Choose a real-world system that interests you. Some examples include:
a. Banking System (with accounts, transactions, and users)
b. Hospital Management System (with patients, doctors, and appointments)
c. Online Shopping Cart (with products, customers, and orders)
d. Game (with players, levels, and scoring)
e. Employee Management System (with employees, departments, and roles)

Feel free to be creative and build any system that aligns with your interests.
3. System Requirements:
Your system should:

a. Have at least 3 classes with appropriate attributes and methods.
b. Demonstrate inheritance by creating subclasses.
c. Include polymorphism by overriding or overloading methods.
d. Apply encapsulation by keeping some attributes private and providing
access methods.
e. (Optional) Implement abstraction by using an abstract base class.
4. Functionality:
Your system should be interactive and perform meaningful operations. For example:
a. Users should be able to add, update, and delete items or records.

b. Implement basic workflows, such as borrowing and returning items (for a
library system) or adding products to a cart (for an e-commerce system).
c. Handle basic exceptions (e.g., prevent borrowing an unavailable item or
transferring money beyond the account balance).

5. Additional Requirements:
a. Make the program user-friendly with input/output prompts.
b. Document your code with comments to explain each class and method.

Deliverables:
1. Python Code: Submit the complete source code.
2. Documentation: A short description of your system, including the purpose of each
class.'''

# Class 1: Hospital Management System
def HospitalManagementSystem():
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
            
    # Create Hospital Object
    hospital = Hospital('Getrude Hospital', 'Nairobi City', '0701004028')   
    print('Hospital Details:')
    hospital.display_hospital()
    print()

    # Create Patient Object
    patient = Patient('Alice', 'Nairobi City', '0721711933', 'P001', 25)
    print('Patient Details:')
    patient.display_patient()
    print()

    # Create Doctor Object
    doctor = Doctor('Dr. Bob', 'Nairobi City', '0720704028', 'D001', 'Cardiologist')
    print('Doctor Details:')
    doctor.display_doctor()
    print()
    
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


# Call HospitalManagementSystem
HospitalManagementSystem()
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

# Doctor Details:
# Doctor ID: D001
# Name: Dr. Bob
# Specialization: Cardiologist
# Location: Nairobi City
# Contact: 0720704028


