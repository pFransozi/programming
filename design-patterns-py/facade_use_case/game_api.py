from decimal import Decimal
from users import Users
from wallets import Wallets
from game_engine import GameEngine
from reports import Reports

class GameAPPI():

    @staticmethod
    def get_balance(user_id:str) -> Decimal:

        return Wallets.get_balance(user_id)

    @staticmethod
    def game_state() -> dict:
        
        return GameEngine().get_game_state()

    @staticmethod
    def get_history() -> dict:
        "A method to get history."
        return Reports.get_history()
    

    @staticmethod
    def change_pwd(user_id: str, password: str) -> bool:

        return Users.change_pwd(user_id, password)


    @staticmethod
    def submit_entry(user_id:str, entry:Decimal) -> bool:

        return GameEngine().submit_entry(user_id, entry)

    @staticmethod
    def register_user(value: dict[str, str]) ->str:

        return Users.register_user(value)