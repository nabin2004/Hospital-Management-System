from admin import doctors, patients, discharged_patients

def append_file():
    with open("database/patients.txt", "a") as file:  # Open the file in append mode
        for patient in patients:
            file.write(str(patient) + "\n")

def pat_read_files():
    with open("database/patients.txt", "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        print(line)

def pat_write_file():
    with open("database/patients.txt", "a") as file:  # Open the file in append mode
        for patient in patients:
            file.write(str(patient) + "\n")



