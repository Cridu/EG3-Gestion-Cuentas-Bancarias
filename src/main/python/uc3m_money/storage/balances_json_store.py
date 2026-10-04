'''Archivo para manejar los jsons'''
from uc3m_money.storage.json_store import JsonStore
from uc3m_money.account_management_config import BALANCES_STORE_FILE

class BalancesJsonStore(JsonStore):
    '''Clase balancesJsonStore'''
    #pylint: disable = invalid-name
    class __BalancesJsonStore(JsonStore):
        _file_name = BALANCES_STORE_FILE

    __instance = None

    def __new__(cls):
        if not BalancesJsonStore.__instance:
            BalancesJsonStore.__instance = BalancesJsonStore.__BalancesJsonStore()
        return BalancesJsonStore.__instance
