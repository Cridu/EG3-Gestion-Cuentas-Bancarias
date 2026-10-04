"""Account manager module"""
from uc3m_money.iban_balance import IbanBalance
from uc3m_money.transfer_request import TransferRequest
from uc3m_money.account_deposit import AccountDeposit
from uc3m_money.storage.transfer_json_store import TransfersJsonStore
from uc3m_money.storage.deposits_json_store import DepositsJsonStore
from uc3m_money.storage.balances_json_store import BalancesJsonStore

class AccountManager:
    """Utility class for validating inputs"""

    class __AccountManager:
        """Utility class for validating inputs"""

        def __init__(self):
            pass

        def transfer_request(self, from_iban: str,
                             to_iban: str,
                             concept: str,
                             transfer_type: str,
                             date: str,
                             amount: float) -> str:
            """funcion transfer request"""

            my_request = TransferRequest(from_iban=from_iban,
                                         to_iban=to_iban,
                                         transfer_concept=concept,
                                         transfer_type=transfer_type,
                                         transfer_date=date,
                                         transfer_amount=amount)

            transfer_store = TransfersJsonStore()
            transfer_store.add_item(my_request)
            return my_request.transfer_code

        def deposit_into_account(self, input_file: str) -> str:
            """funicion deposit"""

            deposit_obj = AccountDeposit.load_deposit_from_file(input_file)
            deposits_json_store = DepositsJsonStore()
            deposits_json_store.add_item(deposit_obj)
            return deposit_obj.deposit_signature

        def calculate_balance(self, iban: str) -> bool:
            """funcion calculate balance"""

            iban_balance = IbanBalance(iban)
            balances_storage = BalancesJsonStore()
            balances_storage.add_item(iban_balance)
            return True

    __instance = None

    def __new__(cls):
        if not AccountManager.__instance:
            AccountManager.__instance = AccountManager.__AccountManager()
        return AccountManager.__instance