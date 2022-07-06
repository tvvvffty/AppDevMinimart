from uuid import uuid4


class UserFeedback:

    def __init__(self,  cust_q1, cust_q2, cust_q3, cust_q4, cust_q5):
        uuid = str(uuid4())[:8]
        self.__user_id = uuid
        self.__cust_q1 = cust_q1
        self.__cust_q2 = cust_q2
        self.__cust_q3 = cust_q3
        self.__cust_q4 = cust_q4
        self.__cust_q5 = cust_q5

    def set_user_id(self, uuid):
        self.__user_id = uuid

    def set_cust_q1(self, cust_q1):
        self.__cust_q1 = cust_q1

    def set_cust_q2(self, cust_q2):
        self.__cust_q2 = cust_q2

    def set_cust_q3(self, cust_q3):
        self.__cust_q3 = cust_q3

    def set_cust_q4(self, cust_q4):
        self.__cust_q4 = cust_q4

    def set_cust_q5(self, cust_q5):
        self.__cust_q5 = cust_q5

    def get_cust_q3(self):
        return self.__cust_q3

    def get_cust_q4(self):
        return self.__cust_q4

    def get_cust_q5(self):
        return self.__cust_q5

    def get_cust_q2(self):
        return self.__cust_q2

    def get_cust_q1(self):
        return self.__cust_q1

    def get_user_id(self):
        return self.__user_id


