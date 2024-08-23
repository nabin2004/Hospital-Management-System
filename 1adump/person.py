class Person:
    last_id = 0

    def __init__(self, first_name, surname):
        self.id = Person.last_id + 1
        Person.last_id += 1
        self.__first_name = first_name
        self.__surname = surname

    def get_unique_hospital_id(self):
        return self.id

    def full_name(self):
        return f'{self.__first_name} {self.__surname}'
    
    def get_first_name(self):
        return self.__first_name

    
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name 

    def get_surname(self):
        return self.__surname
    
    def set_surname(self, new_surname):
        self.__surname = new_surname

    # def get_age(self):
    #     return self.age
    
    # def set_age(self,new_age):
    #     self.age = new_age

    # def get_mobile(self):
    #     return self.mobile
    
    # def set_mobile(self, new_mobile):
    #     self.mobile = new_mobile

    # def get_postcode(self):
    #     return self.postcode

    # def set_postcode(self, new_postcode):
    #     self.postcode = new_postcode


    # def get_username(self):
    #     return self.username
    # def set_username(self, new_username):
    #     self.username = new_username

    # def get_password(self):
    #     return self.__password
    
    # def set_password(self,new_password):
    #     self.__password = new_password
    # def login_authenticator(self,username,password):
    #     if username == self.username and password == self.__password:
    #         return True
    #     else:
    #         return False