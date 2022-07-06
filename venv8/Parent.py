class Parent:
    def __init__(self,name,date_created,date_updated):
        self.__name = name
        self.__date_created = date_created
        self.__date_updated = date_updated
    def set_name(self,name):
        self.__name  = name

    def get_name(self):
        return self.__name

    def set_date_created(self,date_created):
        self.__date_created = date_created

    def set_date_updated(self,date_updated):
        self.__date_updated = date_updated

    def get_date_created(self):
        return self.__date_created

    def get_date_updated(self):
        return self.__date_updated
