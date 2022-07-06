

from Products import *

class Cart(Products):

    def __init__(self,uuid, name,brand,category,price,quantity,status,date_created,date_updated,picture):
        super().__init__(uuid,name,price,quantity,date_created,date_updated,picture)
        self.__uuid = str(uuid4())[:4]
        self.__name = name
        self.__brand = brand
        self.__picture = picture
        self.__category = category
        self.__price = price
        self.__quantity = quantity
        self.__status = status
        self.__date_created = date_created
        self.__date_updated = date_updated


    def set_name(self,name):
        self.__name = name

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

    def set_picture(self, picture):
        self.__picture = picture

    def set_date_created(self,date_created):
        self.__date_created = date_created

    def set_date_updated(self,date_updated):
        self.__date_updated = date_updated

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

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

    def get_date_created(self):
        return self.__date_created

    def get_date_updated(self):
        return self.__date_updated

