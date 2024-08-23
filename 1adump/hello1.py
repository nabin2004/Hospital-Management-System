from admin import Admin
from patient import Patient
from doctor import Doctor

def database_list(filename,role):
    file = open(filename, 'r')

    class_maker = []
    for index, line in enumerate(file):
        if index != 0: #skip first line of file
            if line != '\n' or line !="":
                parameters = line.split(",")
                parameters = [parameter.strip() for parameter in parameters]
                class_maker.append(parameters)

    if role.lower() == "admin":
        class_maker = class_maker[0]
        return Admin(class_maker[0], class_maker[1], class_maker[2])
    
    elif role.lower() == "doctor":
        object_list = []
        for i in class_maker:
            doctor = Doctor(i[0], i[1], i[2])
            object_list.append(doctor)
        return object_list
    
    elif role.lower() == "patient":
        object_list = []
        for i in class_maker:
            symptoms = i[-1].split("+")
            symptoms = [i.strip() for i in symptoms]
            patient = Patient(i[0], i[1], )            #do correction here
            object_list.append(patient)
        return object_list
    else:
        print(f"Invalid role:  {role}")


# admin_list = database_list("") 
admin = database_list("./database/admin.txt", 'admin')
