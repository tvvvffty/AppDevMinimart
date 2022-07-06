class Login():
    count_id = 0  # class attribute

    def __init__(self, email, password):
        Login.count_id += 1  # self.__class__.count_id += 1
        self.__user_id = Login.count_id  # self.__class__.count_id += 1
        self.__email = email
        self.__password = password

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password



