from uc3m_money.account_management_exception import AccountManagementException
from uc3m_money.data.attr.attribute import Attribute


class TransferAmount(Attribute):

    def __init__(self, attr_value):
        """init"""
        self._validation_pattern = r""
        self._error_message = ""
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        """VALIDACION"""

        try:
            f_amount = float(attr_value)
        except ValueError as exc:
            raise AccountManagementException("Invalid transfer amount") from exc

        n_str = str(f_amount)
        if '.' in n_str:
            decimales = len(n_str.split('.')[1])
            if decimales > 2:
                raise AccountManagementException("Invalid transfer amount")

        if f_amount < 10 or f_amount > 10000:
            raise AccountManagementException("Invalid transfer amount")

        return f_amount