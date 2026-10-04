'''Archivo para manejar los jsons'''
from uc3m_money.storage.json_store import JsonStore
from uc3m_money.account_management_config import DEPOSITS_STORE_FILE
from uc3m_money.account_management_exception import AccountManagementException

class DepositsJsonStore(JsonStore):
    '''Clase para manejar los jsons'''
    class __DepositsJsonStore(JsonStore):
        '''Clase para manejar los jsons'''
        _file_name = DEPOSITS_STORE_FILE

        def add_item(self, item):
            for transfer in self._data_list:
                if (transfer == item.to_json()):
                    raise AccountManagementException("Duplicated transfer in transfer list")
            super().add_item(item)

    __instance = None

    def __new__(cls):
        if not DepositsJsonStore.__instance:
            DepositsJsonStore.__instance = DepositsJsonStore.__DepositsJsonStore()
        return DepositsJsonStore.__instance