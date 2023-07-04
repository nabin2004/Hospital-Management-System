from admin import Admin,patients,doctors,discharged_patients

admins = [Admin("admin", "password"), Admin("Namaste", "World")]

def main():
    print("---------Welcome to Hospital Management System")
    login = False
    while not login:
        user = input('Enter username: ')
        passw = input("Enter password: ")
        for i in range(len(admins)):
            if admins[i].get_username() == user and admins[i].get_password() == passw:
                login = True 
                administration = admins[i]
                break
        if not login:
            print("Incorrect details")

    if login:
        print("Login successful")
        while login:
            try:
                # Print the menu
                print('Choose the operation:')
                print(' 1- Register/view/update/delete doctor')
                print(' 2- View/Discharge patients')
                print(' 3- View discharged patient')
                print(' 4- Assign doctor to a patient')
                print(' 5- Update admin details')
                print(" 6- Add patients")
                print(" 7- Find dates/check appointment status")
                print(" 8- Relocate a patient from one doctor to another")
                print(" 9- Request management report")
                
                print(' 11. Group patients by family')
                print(" 12. Add Symptoms")
                print(" 10- Quit")

                # Get the option
                op = input('Option: ')

                if op == '1':
                    administration.doctor_management()

                elif op == '2':
                    # 2- View and discharge patients
                    # administration.same_family()
                    administration.discharge()

                elif op == '3':
                    # 3 - View discharged patients
                    administration.view_discharge()

                elif op == '4':
                    # 4- Assign doctor to a patient
                    administration.assign_doctor_to_patient()

                elif op == '5':
                    # 5- Update admin details
                    administration.update_details()

                elif op == '6':
                    administration.admit_patient()

                elif op == '7':
                    administration.appointment()

                elif op == '8':
                    # Relocate a patient from one doctor to another
                    administration.view(patients)
                    patient_id = int(input("Enter the ID of the patient to relocate: "))
                    administration.view(doctors)
                    new_doctor_id = int(input("Enter the ID of the new doctor: "))
        
                    patient = patients[patient_id]
                    new_doctor = doctors[new_doctor_id]
        
                    # Find the patient and new doctor objects based on their IDs
                    for p in patients:
                        if p.id == patient_id:
                            patient = p
                            break
                    
                    for d in doctors:
                        if d.id == new_doctor_id:
                            new_doctor = d
                            break
                    
                    if patient and new_doctor:
                        administration.relocate_patient(patient, new_doctor)
                    else:
                        print("Patient or new doctor not found")
                    administration.relo_doctor_to_patient(patient_id,new_doctor_id)
                    administration.view(patients)



                elif op == '9':
                    # Request management report
                    administration.report()
                    with open('management_report.txt', 'w') as file:
                        for item in discharged_patients:
                            file.write(str(item) + '\n')
                    print("Management report generated.")

                elif op == '10':
                    # 10 - Quit
                    running = False
                    print('------------Exiting program...--------')
                    print("|-------------------------------------|")
                    print("|          Have a nice time:)         |")
                    print("|-------------------------------------|")
                    quit()

                elif op == '11':
                    administration.same_family()

                else:
                    # The user did not enter an option that exists in the menu
                    print('Invalid option. Try again')
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue

            if op == "12":                
                administration.view(patients)

                index = int(input("Enter index of patient: "))
                print("What do you want to do? ")
                print(" 1. Add symptoms to patient ")
                print(" 2. View symptoms of patients ")
                op1 = input("Enter your choice: ")
                if op1 == '1':
                    print("Welcome to Symptoms addition window")
                    symptoms = input(f"Enter the symptoms that needs to be added for {patients[index].get_first_name()}: ")
                    patients[index].set_symptoms(symptoms)
                    print("Successfully Added!")
                elif op1 == '2':
                    symp = (patients[index].print_symptoms())
                    for i,j in enumerate(symp):
                        print(j)
                else:
                    print("Invalid input!")


main()
