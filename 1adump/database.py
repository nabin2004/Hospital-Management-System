#create testing list 
from doctor import Doctor
from admin import Admin
from patient import Patient

# Create a list of Doctor objects
doctors = [
    Doctor("John", "Smith", 40, "1234567890", "12345", "johnsmith", "password", "Cardiology"),
    Doctor("Emma", "Johnson", 35, "0987654321", "54321", "emmajohnson", "password", "Dermatology"),
    Doctor("Michael", "Brown", 45, "9876543210", "67890", "michaelbrown", "password", "Orthopedics")
]

discharged_patients = [
    Patient("Johndsichage1", "Smith", 30, "1234567890", "12345", "johnsmith", "password"),
    Patient("Janedsicha", "Doe", 25, "9876543210", "54321", "janedoe", "password"),
    Patient("Michaeldischarge", "Johnson", 40, "5555555555", "67890", "michaeljohnson", "password")
]

patients = [Patient("John", "Smith", 30, "1234567890", "12345", "johnsmith", "password"),
            Patient("Jane", "Doe", 25, "9876543210", "54321", "janedoe", "password")]
