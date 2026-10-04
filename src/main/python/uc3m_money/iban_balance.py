'''Account balance'''
from uc3m_money.data.attr.iban_code import IbanCode
from uc3m_money.account_management_exception import AccountManagementException
from uc3m_money.account_management_config import TRANSACTIONS_STORE_FILE
import json
from datetime import datetime,timezone

class IbanBalance():
    '''Clase para calcula el IbanBalance'''

    def __init__(self, iban):
        self._iban = IbanCode(iban).value
        self.__last_balance_time=datetime.timestamp(datetime.now(timezone.utc))
        self.__balance = self.calculate_iban_balance()

    def calculate_iban_balance(self):
        transactions_list = self.read_transactions_file()
        iban_found = False
        current_balance = 0
        for transaction in transactions_list:
            if transaction["IBAN"] == self._iban:
                current_balance += float(transaction["amount"])
                iban_found = True
        if not iban_found:
            raise AccountManagementException("IBAN not found")
        return current_balance

    def read_transactions_file(self):
        try:
            with open(TRANSACTIONS_STORE_FILE, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise AccountManagementException("Wrong file  or file path") from ex
        except json.JSONDecodeError as ex:
            raise AccountManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return input_list

    def to_json(self):
        return {"IBAN": self._iban,
                        "time": self.__last_balance_time,
                        "BALANCE": self.__balance}