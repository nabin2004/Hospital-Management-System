from doctor import Doctor
from patient import Patient
from admin import Admin

def database_to_model(person_database_file, person_type):
    person_database = open(person_database_file, 'r')

    parameter_list = [] # Each element in this list is a list of object's parameters
    for index, line in enumerate(person_database):
        if index != 0: # skipping first line as it is just indicator of the columns
            if line != "\n" or line != "":
                parameters = line.split(",")
                parameters = [parameter.strip() for parameter in parameters]
                parameter_list.append(parameters)
    
    # if the given file is of admin
    if person_type.lower() == "admin" or person_type.lower() == "admin":
        try: # trying to create list of a admin object and returning
            parameter_list = parameter_list[0]
            return Admin(parameter_list[0], parameter_list[1], parameter_list[2])
        except: # incase creation of object fails, throwing error and giving error context
            print(f"'{person_database_file}' has invalid structure!")
            print('Structure should follow "username, password, address"')
            exit()

    # if the given file is of doctor
    elif person_type.lower() == "doctor" or person_type.lower() == "doctor":
        try: # trying to create list of object and returning
            object_list = []
            for each in parameter_list:
                doctor = Doctor(each[0], each[1], each[2])
                object_list.append(doctor)
            return object_list
        except: # incase creation of object fails, throwing error and giving error context
            print(f"'{person_database_file}' has invalid structure!")
            print('Structure should follow "first_name, surname, speciality" seperated by new line for every object')
            exit()

    # if the given file is of patient
    elif person_type.lower() == "patient" or person_type.lower() == "patient":
        try: # trying to create list of object and returning
            object_list = []
            for each in parameter_list:
                symptoms = each[-1].split("+")
                symptoms = [each.strip() for each in symptoms]
                patient = Patient(each[0], each[1], int(each[2]), each[3], each[4], symptoms)
                object_list.append(patient)

            return object_list

        except: # incase creation of object fails, throwing error and giving error context
            print(f"'{person_database_file}' has invalid structure!")
            print('Structure should follow "first_name, surname, age, mobile, postcode, symptoms" seperated by new line for every object')
            exit()
    
    else:
        print("Passed 'person_type' is invalid! ")




# admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
admin = database_to_model("./database/admin.txt", 'admin')
# doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
doctors = database_to_model("./database/doctors.txt", 'doctor')
# patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
patients = database_to_model("./database/patients.txt", 'patient')
# patients = admin.group_patients_by_family(patients) # Patients of the same family are grouped together 

for i in patients:
    print(i)
print(patients)
print(doctors)
print(admin)

discharged_patients = []