from uuid import uuid4
import datetime

class Reward:

    def __init__(self, name, value, expiryDate, category, ):
        uuid = str(uuid4())[:8]
        self.__special_id = uuid
        self.__name = name
        self.__value = value
        self.__expiryDate = expiryDate
        self.__category = category
        # self.__image = image

    def set_special_id(self, special_id):
        self.__special_id = special_id

    def set_name(self, name):
        self.__name = name

    def set_value(self, value):
        self.__value = value

    def set_expiryDate(self, expiryDate):
        self.__expiryDate = expiryDate

    def set_category(self, category):
        self.__category = category

    # def set_image(self, image):
    #     self.__image = image

    def get_special_id(self):
        return self.__special_id

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_expiryDate(self):
        return self.__expiryDate

    def get_category(self):
        return self.__category

    # def get_image(self):
    #     return self.__image
