from person import Person

class Doctor(Person):
    def __init__(self, first_name, surname, speciality):
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__patients = []
        self.appointments = []

    def get_speciality(self):
        return self.__speciality
    
    # def get_password(self):
    #     return self.__password

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)
    
    def get_patients(self):
        return self.__patients

    def set_appointments(self, time):
        self.appointments.append(time)

    def get_appointments(self):
        return self.appointments
    
    def get_num_pat(self):
        return len(self.__patients)


    def __str__(self) :
            return f'{self.full_name():^30}|{self.__speciality:^15}'


