from admin import doctors


def doc_write_file():
    file = open("database/doctors.txt", "w")
    
    for doctor in doctors:
        file.writ(str(doctor) + "\n")
    file.close()

def doc_read_files():
    file = open("database/doctors.txt", "r")
    lines = file.read().splitlines()
    file.close()
    
    for line in lines:
        print(line)

def append_file():
    with open("database/doctors.txt", "a") as file:  # Open the file in append mode
        for doctor in doctors:
            file.write(str(doctor) + "\n")

