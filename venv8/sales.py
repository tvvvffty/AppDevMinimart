from uuid import uuid4

class Sales:
    def __init__(self, Total_amount,name, date):
        self.__uuid = str(uuid4())[:4]
        self.__date = date
        self.__Total_amount = Total_amount
        self.__name = name


    # def set_uuid(self,uuid):
    #     self.__uuid = uuid

    def set_order_date(self, date):
        self.__date = date

    def set_amount(self, Total_amount):
        self.__Total_amount= Total_amount

    def set_email(self, name):
        self.__name = name


    def get_uuid(self):
        return self.__uuid

    def get_date(self):
        return self.__date

    def get_Total_amount(self):
        return self.__Total_amount

    def get_name(self):
        return self.__name



