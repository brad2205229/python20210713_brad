
# DAO = Data Access Object
from Lab.Login.Model import User

class UserDao:

    __users = [
        User('john', '1234'),
        User('mary', '5678')
    ]

    def find_user(self, username):
        for user in self.__users:
            if user.username == username:
                return user
        return None

    def find_all_user(self):
        return self.__users

    def add_user(self, user):
        self.__users.append(user)
