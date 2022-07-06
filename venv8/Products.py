from Parent import *
from uuid import uuid4

class Products(Parent):

    def __init__(self,name,brand,category,price,quantity,status,date_created,date_updated,picture):
        super().__init__(name,date_created,date_updated)
        self.__uuid = str(uuid4())[:4]
        self.__brand = brand
        self.__picture = picture
        self.__category = category
        self.__price = price
        self.__quantity = quantity
        self.__status = status

    def set_brand(self,brand):
        self.__brand = brand

    def set_category(self,category):
        self.__category = category

    def set_price(self,price):
        self.__price = price

    def set_quantity(self,quantity):
        self.__quantity = quantity

    def set_status(self,status):
        self.__status = status

    def get_brand(self):
        return self.__brand

    def set_picture(self,picture):
        self.__picture = picture

    def get_picture(self):
        return self.__picture

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_status(self):
        return self.__status

    def get_uuid(self):
        return self.__uuid


