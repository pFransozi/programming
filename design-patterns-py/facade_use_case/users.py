"a singleton dictionary of users"
from decimal import Decimal
from wallets import Wallets
from reports import Reports

class Users():
    _users: dict[str, dict[str, str]] = {}

    def __new__(cls):
        return cls

    @classmethod
    def register_user(cls, new_user: dict[str, str]) -> str:
        "register a new user"

        if not new_user["user_name"] in cls._users:
            user_id = new_user['user_name']
            cls._users[user_id] = new_user
            Reports.log_event(
                f"new user {user_id} created."
            )
            Wallets().create_wallet(user_id)
            Reports.log_event(
                f"Give new user {user_id} sign up bonus of 10"
            )
            return user_id
        return ""

    @classmethod
    def edit_user(cls, user_id:str, user:dict):

        print(user_id)
        print(user)
        return False

    @classmethod
    def change_pwd(cls, user_id:str, password:str):

        print(user_id)
        print(password)
        return False