from doctor import Doctor
from patient import Patient
import datetime

doctors = [
    Doctor("John", "Smith", "Cardiology"),
    Doctor("Emma", "Johnson", "Dermatology"),
    Doctor("Michael", "Brown", "Orthopedics"),
    Doctor("Sarah", "Williams", "Pediatrics"),
    Doctor("David", "Jones", "Neurology"),
    Doctor("Olivia", "Davis", "Gastroenterology"),
    Doctor("William", "Miller", "Ophthalmology"),
    Doctor("Sophia", "Wilson", "Endocrinology"),
    Doctor("James", "Anderson", "Rheumatology"),
    Doctor("Charlotte", "Taylor", "Oncology")
]

patients = [
    Patient("John", "Smith", 30, "1234567890", "12345"),
    Patient("Kanna", "Smith", 20, "123450", "123458"),
    Patient("Jane", "Doe", 25, "9876543210", "54321"),
    Patient("Michael", "Johnson", 40, "4567890123", "67890"),
    Patient("Emily", "Taylor", 35, "8901234567", "90123"),
    Patient("Daniel", "Wilson", 50, "2345678901", "23456"),
    Patient("Fanny", "Smith", 50, "12223450", "12342258"),
    Patient("Olivia", "Clark", 28, "7890123456", "78901"),
    Patient("Ethan", "Moore", 45, "0123456789", "01234"),
    Patient("Ava", "Lee", 32, "5678901234", "56789"),
    Patient("Mason", "Walker", 55, "9012345678", "90123"),
    Patient("Will", "Smith", 21, "12345110", "12113458"),
    Patient("Sophia", "Hall", 42, "3456789012", "34567")
]


appointments = []

illnesses = []

discharged_patients = [
    Patient("Johndsichage", "Smith", "30", "1234567890", "12345"),
    Patient("Janedsicha", "Doe", "25", "9876543210", "54321"),
    Patient("Michaeldischarge", "Johnson", "40", "5555555555", "67890")
]



class Admin:
    def __init__(self, username, password, address=""):
        self.__username = username
        self.__password = password
        self.__address = address

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password

    # def login(self):
    #     return self.__username in user and self.__password == passw

    def view(self, items):
        if not items:
            print("No items to display.")
        else:
            for i, j in enumerate(items):
                print(i, j)

    def find_index(self, index, items):
        try:
            index = int(index)
            if index in range(len(items)):
                return True
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid index.")

        return False
    
    # File handling
    def doc_write_file(self):
        try:
            with open("database/doctors.txt", "w") as file:
                for doctor in doctors:
                    file.write(str(doctor) + "\n")
            print("File write successful.")
        except IOError:
            print("An error occurred while writing to the file.")

    def doc_read_file(self):
        try:
            with open("database/doctors.txt", "r") as file:
                for line in file:
                    doctors.append(line.strip())
            print("File read successful.")
        except IOError:
            print("An error occurred while reading the file.")

        return doctors

    def doc_read_files(self):
        try:
            with open("database/doctors.txt", "r") as file:
                lines = file.read().splitlines()
            for line in lines:
                print(line)
            print("File read successful.")
        except IOError:
            print("An error occurred while reading the file.")

    def append_file(self):
        try:
            with open("database/doctors.txt", "a") as file:
                for doctor in doctors:
                    file.write(str(doctor) + "\n")
            print("File append successful.")
        except IOError:
            print("An error occurred while appending to the file.")
    # File handling

    def get_doctor_details(self):
        first_name = input("Enter the doctor's first name: ")
        surname = input("Enter the doctor's surname: ")
        speciality = input("Enter the doctor's speciality: ")
        return (first_name, surname, speciality)
    
    
    def doctor_management(self):
        while True:
            print("\nDoctor Management")
            print("1. Register")
            print("2. View")
            print("3. Update")
            print("4. Delete")
            print("0. Back")
            try:
                choice = (input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue
            if choice == '1':
                print("-------Register-------")
                first_name, last_name, speciality = self.get_doctor_details()
                for i in doctors:
                    if (first_name==i.get_first_name() and last_name==i.get_surname()):
                         print("Name already exists.")
                         break
                else:   
                    doctor = Doctor(first_name, last_name, speciality)
                    doctors.append(doctor)
                    self.doc_write_file()
                    print("Doctor registered")

            elif choice == '2':
                print("\nList of doctors:")
                print("ID     ||   FULL NAME          ||   SPECIALITY")
                self.view(doctors)


            elif choice == '3':
                print("\n-----------Update doctor details--------------------")
                print("List of doctors:")
                self.view(doctors)
                index = int(input("Enter the ID of the doctor to update: "))
                index_doctor = self.find_index(index,doctors)
                if index_doctor == False:
                    print("404 Doctor not found :) ")
                else:
                    if self.find_index(index, doctors) == True:
                        print("-----Choose the field (1/2/3/4):")
                        print("1. First name")
                        print("2. Last name")
                        print("3. Speciality")
                        field = input("Enter the field to update: ")
                        if field == '1':
                            new_first_name = input("Enter the new first name: ")
                            doctors[index].set_first_name(new_first_name)
                            print("first Name successfully changed! ")
                        elif field == '2':
                            new_last_name = input("Enter the new last name: ")
                            doctors[int(index)].set_surname(new_last_name)
                            print("Surame successfully changed! ")
                        elif field == '3':
                            new_speciality = input("Enter the new speciality: ")
                            doctors[int(index)].set_speciality(new_speciality)
                            print("Speciallity successfully changed! ")
                        else:
                            print("Invalid choice")
                    else:
                        print("The ID entered was not found")

            elif choice == '4':
                print("-----------Delete a doctor-----------")
                print("List of doctors:")
                self.view(doctors)

                index = int(input("Enter the ID of the doctor to delete: "))
                if self.find_index(index, doctors):
                    doctors.pop(int(index))
                    print("Doctor deleted")
                else:
                    print("The ID entered was not found")

            elif choice == '0':
                break

            else:
                print("Invalid choice")

    def discharge(self):
        self.view(patients)
        print("-------------Discharge Patient------------") 
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)
        y_no = input("Do you want to discharge a patient (Y/N): ")
        if y_no.lower() == 'y':
            print("----------Discharge Patient-------------")
            try:
                patient_index = int(input("Please Enter the patient ID: "))
            except ValueError:
                print("Invalid input. Please enter a valid patient ID.")
                return

            if self.find_index(patient_index, patients):
                discharge_patient = patients.pop(patient_index) # Removing the patient we want to discharge from patients list and keeping it in a variable
                discharged_patients.append(discharge_patient)
                print(f"Patient {discharge_patient.full_name()} is discharged.")
            else:
                print("Invalid patient ID.")
        else:
            print("Not able to discharge.")


    
    def view_patient(self):
        print("--------------------Current admitted patients--------")
        try:
            self.view(patients)
        except Exception as e:
            print("An error occurred while trying to view the patients:", str(e))


    def view_discharge(self):
        print("-----Discharged Patients-----")
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        try:
            self.view(discharged_patients)
        except Exception as e:
            print("An error occurred while trying to view the discharged patients:", str(e))


    def assign_doctor_to_patient(self):
        print("-----Assign-----")

        print("-----Patients-----")
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index)

            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return

        except ValueError:
            print('The ID entered is incorrect.')
            return

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index)

            if doctor_index not in range(len(doctors)):
                print('The ID entered was not found.')
                return

            patients[patient_index].link(doctors[doctor_index].full_name())
            self.view(patients)
            doctors[doctor_index].add_patient(patients[patient_index].full_name())
            print('The patient is now assigned to the doctor.')

        except ValueError:
            print('The ID entered is incorrect.')

    def relo_doctor_to_patient(self,patient_index,doctor_index):
        # print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        try:
            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return

        except ValueError:
            print('The ID entered is incorrect.')
            return

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)

        try:
            if doctor_index not in range(len(doctors)):
                print('The ID entered was not found.')
                return

            patients[patient_index].link(doctors[doctor_index].full_name())
            self.view(patients)
            doctors[doctor_index].add_patient(patients[patient_index].full_name())
            print('The patient is now assigned to the doctor.')

        except ValueError:
            print('The ID entered is incorrect.')


    def relocate_patient(self, patient, new_doctor):
        if patient in patients:
            patients.remove(patient)
            new_doctor.add_patient(patient)
            print(f"{patient.get_first_name()} has been relocated to {new_doctor.full_name()}")
        else:
            print("Patient not found in the list")
            
    def appointment(self):
        print("|--Choose the operation----|")
        print("|--1. Book your date: -----|")
        print("|--2. Check your status:---|")
        print("|--------------------------|")
        op = input("Enter your choice: ")

        try:
            if op == '1':
                # Appointment time
                month = int(input("Enter the month: "))
                day = int(input("Enter the date: "))
                timehour = int(input("Enter hour for appointment: "))
                minute = int(input("Enter minute: "))
                dt = datetime.datetime(2023,month, day, timehour, minute, 0)
                # Appointment time
                print(f"Confirmation:: your appointment time is: {dt}")
                self.view(patients)
                p_index = int(input('Enter the ID of the patient: '))
                patient_index = self.find_index(p_index, patients)
                if not patient_index:
                    raise ValueError("404! -- Patient not found")
                else:
                    alive_pat = patients[p_index]
                    print("-----List of doctors-----")
                    print('ID |          Full name           |  Speciality')
                    self.view(doctors)
                    d_index = int(input('Enter the ID of the doctor: '))
                    doctor_index = self.find_index(d_index, doctors)
                    if not doctor_index:
                        raise ValueError("Doctor not found")
                    else:
                        alive_pat.add_appointment(dt)
                        alive_pat.set_status("Approved(Date found)!")
                        alive_doc = doctors[d_index]
                        alive_doc.set_appointments(dt)
                        print("Appointment Done!")
                        print(alive_pat.show_appointment())

            elif op == '2':
                self.view(patients)
                p_index = int(input('Enter the ID of the patient: '))
                patient_index = self.find_index(p_index, patients)
                if patient_index:
                    pat = patients[patient_index]
                    print(pat.get_status())
                else:
                    raise ValueError("404! -- Patient not found")

            else:
                raise ValueError("Invalid choice. Please try again.")

        except ValueError as e:
            print(str(e))




    # def group_patients_by_family(self):
    #     same_family_patients = []
    #     for i in range(len(patients)):
    #         for j in range(i+1, len(patients)):
    #             if patients[i].get_surname() == patients[j].get_surname():
    #                 same_family_patients.append(patients[i])
    #                 same_family_patients.append(patients[j])
    #     print("All grouped!")

    
    def same_family(self):
        same_family = {}
        for patient in patients:
            patient_surname = patient.get_surname()
            if patient_surname not in same_family:
                same_family[patient_surname] = [patient]
            else:
                li = same_family[patient_surname]
                li.append(patient)
                same_family[patient_surname] = li

        # Converting the dict into a list with all the patients objects
        grouped_by_surname = []
        for key, value in same_family.items():
            grouped_by_surname.extend(value)

        for i in grouped_by_surname:
            print(i)


    def admin_details(self):
        print(f"Username : {self.__username}")
        print(f"Password : {self.__password}")
        print(f"Address : {self.__address}")


    def update_details(self):
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = input('Input: ')

        try:
            if op == '1':
                self.admin_details()
                username1 = input('Enter the new username: ')
                # validate the username
                username2 = input('Enter the new username again: ')
                if username1 == username2:
                    print("Username matched.")
                    self.__username = username2
                    print("------------------------------")
                    self.admin_details()
                    print("-----------Username updated--------------")
                else:
                    print("Username not matched")

            elif op == '2':
                self.admin_details()
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    self.__password = password
                    self.admin_details()
                    print("----------------Password updated---------------")

            elif op == '3':
                self.admin_details()
                address = input('Enter the new address: ')
                # validate the address
                if address == input('Enter the new address again: '):
                    self.__address = address
                    self.admin_details()
                    print("address updated.")

            else:
                raise ValueError("Invalid Choice.")

        except ValueError as e:
            print(str(e))


    def admit_patient(self):
        print("-------Select Patient ID-----------------")
        # self.view(not_admitted_patients)
        # index = int(input("Enter index of patient: "))  # Convert input to integer
        # raw = not_admitted_patients[index]
        # not_admitted_patients.pop(index)  # Use the integer index to remove the patient
        f_name = input("Enter patient firstname: ")
        l_name = input("Enter patient surname: ")
        age = input("enter age: ")
        mobile = input("Enter the mobile number: ")
        post = input("Enter the postcode: ")
        patients.append(Patient(f_name, l_name, age, mobile, post))
        self.view(patients)


    def report(self):
        print("-----------------WELCOME TO REPORT CENTER-----------------------------")
        total_doctors = len(doctors)
        print(f"Total number of doctors: {total_doctors}")  #
        total_patients = len(patients)
        print(f"The total number of patients is {total_patients}")  # ii

        for doctor in doctors:
            list1 = doctor.full_name()
            list2 = doctor.get_num_pat()
            print(f"The number patients for {list1} is: {list2}")

        total_number_of_patiens_based_on_illness = {}
        for patient in patients:
            patient_symptoms = patient.print_symptoms()
            for symptom in patient_symptoms:
                if symptom not in total_number_of_patiens_based_on_illness:
                    total_number_of_patiens_based_on_illness[symptom] = 1
                else:
                    total_number_of_patiens_based_on_illness[symptom] += 1

        for n, (k, v) in enumerate(total_number_of_patiens_based_on_illness.items()):
            if n == 0:
                print(f"\n{'Total number of patients based on the illness':<50} : {k:<23} = {v:>3} patients")
            else:
                print(f"{' ':>50}   {k:<23} = {v:>3} patients")
