from uuid import uuid4
import Reward as r


class Standard(r.Reward):

    def __init__(self, name, value, points, expiryDate, category):
        r.Reward.__init__(self, name, value, expiryDate, category)
        uuid = str(uuid4())[:8]
        self.__standard_id = uuid
        self.__points = points

    def set_standard_id(self, uuid):
        self.__standard_id = uuid

    def set_points(self, points):
        self.__points = points

    def set_created(self, created):
        self.__created = created

    def get_points(self):
        return self.__points

    def get_standard_id(self):
        return self.__standard_id

