from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):

        if name != None and job != None:
            # string
            isString = isinstance(name, str)

            if isString == True:
                for user in self.store.bd:
                    if user.name == name:
                        return "User duplicated"
                user = User(name=name, job=job)
                self.store.bd.append(user)
                return "User added"
            else:
                return "User cannot be added"

        else:
            return "Invalid user"

    def delete_user(self, name):

        user_bd = self.check_user(name)

        if user_bd != None:
            self.store.bd.remove(user_bd)
            return "The user was removed successfully"
        else:
            return "The user cannot be found"

    def check_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    # update user
    def update_user(self, name, job):
        user_db = self.check_user(name)
        if user_db != None:
            user_db.job = job
            print(user_db.job)
            return "User updated"
        else:
            return "The user cannot be found."

    # select
    def select_user(self, name):
        user_db = self.check_user(name)
        if user_db != None:
            return user_db.job
        else:
            return "The user cannot be found."


