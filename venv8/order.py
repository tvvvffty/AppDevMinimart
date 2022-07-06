from uuid import uuid4

class Order:
    def __init__(self, order_date, order_time, amount, email):
        self.__uuid = str(uuid4())[:4]
        self.__order_date = order_date
        self.__order_time = order_time
        self.__amount = amount
        self.__email = email

    # def set_uuid(self,uuid):
    #     self.__uuid = uuid

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def set_order_time(self, order_time):
        self.__order_time = order_time

    def set_amount(self, amount):
        self.__amount = amount

    def set_email(self, email):
        self.__email = email


    def get_uuid(self):
        return self.__uuid

    def get_order_date(self):
        return self.__order_date

    def get_order_time(self):
        return self.__order_time

    def get_amount(self):
        return self.__amount

    def get_email(self):
        return self.__email

