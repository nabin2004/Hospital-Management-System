from person import Person

class Patient(Person):
    def __init__(self, first_name, last_name, age, mobile, postcode, status="Pending"):
        super().__init__(first_name, last_name)
        self.__id = self.generate_id()
        self.__doctor = []
        self.__symptoms = []
        self.appointments = []
        self.status = status
        self.age = age
        self.mobile = mobile
        self.postcode = postcode

    def generate_id(self):
        self.__class__.last_id += 1
        return f"PAT{self.__class__.last_id}"

    def get_id(self):
        return self.__id

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        self.__doctor.append(doctor)

    def print_symptoms(self):
        return self.__symptoms
    
    def set_symptoms(self, symptoms):
        self.__symptoms.append(symptoms)

    def add_appointment(self, time):
        self.appointments.append(time)
        self.set_status("Approved")

    def show_appointment(self):
        return self.appointments

    def get_status(self):
        if len(self.appointments) != 0:
            return ("Approved")
        else:
            return ("Pending")
        
    def get_age(self):
        return self.age
    
    def get_mobile(self):
        return self.mobile

    def get_postcode(self):
        return self.postcode
            

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status
    
    # def same_family(self, patients):
    #     pass

    def __str__(self):
        doctors = ', '.join(self.get_doctor())
        return f'Patient ID: {self.get_id():^8} || Full Name: {self.full_name():^20} || Doctors: {doctors:^20} || Age: {self.get_age():^3} || Mobile: {self.get_mobile():^12} || Postcode: {self.get_postcode():^8}'



