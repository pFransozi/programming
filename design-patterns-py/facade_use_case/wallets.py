from decimal import Decimal
from reports import Reports

class Wallets():
    "a singleton dictionary of user wallets"
    _wallets: dict[str, Decimal] = {}

    def __new__(cls):
        return cls

    @classmethod
    def create_wallet(cls, user_id:str) -> bool:
        "a method to initialize a users wallet"

        if not user_id in cls._wallets:
            cls._wallets[user_id] = Decimal('0')
            Reports.log_event(
                f"wallet for '{user_id}' created and set up to 0"
            )
            return True
        return False

    @classmethod
    def get_balance(cls, user_id:str) -> Decimal:
        "a method to check a users balance"
        Reports.log_event(
            f"Balance check foor '{user_id}' = {cls._wallets[user_id]}"
        )
        return cls._wallets[user_id]

    @classmethod
    def adjust_balance(cls, user_id:str, amount:Decimal) -> Decimal:
        "a method to adjust a user balance up or down"

        cls._wallets[user_id] = cls._wallets[user_id] + Decimal(amount)
        Reports.log_event(
            f"Balance adjustment for {user_id} . "
            f"New balance = {cls._wallets[user_id]}"
        )
        return cls._wallets[user_id]