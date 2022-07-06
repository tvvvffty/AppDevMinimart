from uuid import uuid4


class Feedback:

    def __init__(self,  q1, q2, q3, q4, q5):
        uuid = str(uuid4())[:8]
        self.__feedback_id = uuid
        self.__q1 = q1
        self.__q2 = q2
        self.__q3 = q3
        self.__q4 = q4
        self.__q5 = q5

    def set_star_id(self, feedback_id):
        self.__feedback_id = feedback_id

    def set_q1(self, q1):
        self.__q1 = q1

    def set_q2(self, q2):
        self.__q2 = q2

    def set_q3(self, q3):
        self.__q3 = q3

    def get_q3(self):
        return self.__q3

    def set_q4(self, q4):
        self.__q4 = q4

    def get_q4(self):
        return self.__q4

    def set_q5(self, q5):
        self.__q5 = q5

    def get_q5(self):
        return self.__q5

    def get_q2(self):
        return self.__q2

    def get_feedback_id(self):
        return self.__feedback_id

    def get_q1(self):
        return self.__q1



