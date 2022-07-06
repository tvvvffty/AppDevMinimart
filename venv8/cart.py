class Cart:

    def __init__(self, uuid, name, brand, category, price, quantity):
        self.__uuid = uuid
        self.__name = name
        self.__brand = brand
        self.__category = category
        self.__price = price
        self.__quantity = quantity


    def set_uuid(self,uuid):
        self.__uuid = uuid

    def set_name(self, name):
        self.__name = name

    def set_brand(self, brand):
        self.__brand = brand

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_uuid(self):
        return self.__uuid

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        calculated_Price = self.__price * self.__quantity
        return calculated_Price



