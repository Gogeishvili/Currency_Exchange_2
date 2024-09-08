class UserDataController:
    def __init__(self):
        self.__users = self.__load_user_data()

    @property
    def users(self):
        return self.__users

    def __load_user_data(self):
        return {
            "admin": "admin",
            "user1": "password1",
            "user2": "password2",
        }