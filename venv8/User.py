from Login import *

class User(Login):

    def __init__(self, first_name, last_name, email, address, phone_number, unit_number, postal_code, password, password_confirm):
        super().__init__(email, password)
        self.__picture = "default.jpg"
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__unit_number = unit_number
        self.__postal_code = postal_code
        # self.__password = password
        self.__password_confirm = password_confirm
        self.__feedback_name = None

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def get_unit_number(self):
        return self.__unit_number

    def get_postal_code(self):
        return self.__postal_code

    # def get_password(self):
    #     return self.__password

    def get_password_confirm(self):
        return self.__password_confirm

    def get_picture(self):
        return self.__picture

    def set_picture(self, picture):
        self.__picture = picture

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_unit_number(self, unit_number):
        self.__unit_number = unit_number

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    # def set_password(self, password):
    #     self.__password = password

    def set_password_confirm(self, password_confirm):
        self.__password_confirm = password_confirm

