class UserData:
    def __init__(self):
        self.__users = self.__load_users_data()

    def get_users(self):
        return self.__users

    def __load_users_data(self):
        return {
            "admin": "admin",
            "user1": "password1",
            "user2": "password2",
        }