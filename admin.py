from Doctor import Doctor


class Admin:
    def __init__ (self, username, password, address=''):
        self.username = username 
        self.password = password 
        self.address = address

    def view(self, a_list):
        for i in a_list:
            print(i)

    def login(self):
        input_username = input("Your username: ")
        input_password = input("Your password: ")
        if self.username == input_username and self.password == input_password:
            print("Logged In")
        else:
            print("Incorrect Credentials! ")
        

    def find_index(self, index, doctors):
        if index in doctors:    #mistake huna pani sakcha hai yo
            return doctors


    def get_doctor_details(self):
        pass 

    def doctor_management(self, doctors):
        pass 

    def view_patients(self,patients):
        pass 

    def assign_doctor_to_patient(self,patients,doctors):
        pass 

    def discharge(self,patients,discharge_patients):
        pass 

    def view_discharge(self,discharged_patients):
        pass 

    def update_details(self):
        pass 
