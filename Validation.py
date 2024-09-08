class UserValidation:
    def __init__(self, user_data):
        self.__users = user_data.get_users()

    def validate(self, username, password):
        try:
            if username in self.__users and self.__users[username] == password:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred during validation: {e}")
            return False


