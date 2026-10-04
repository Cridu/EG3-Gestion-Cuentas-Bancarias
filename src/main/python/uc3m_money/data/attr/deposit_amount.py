from uc3m_money.account_management_exception import AccountManagementException
from uc3m_money.data.attr.attribute import Attribute


class DepositAmount(Attribute):

    def __init__(self, attr_value):
        """init"""
        self._validation_pattern = r"^EUR [0-9]{4}\.[0-9]{2}"
        self._error_message = "Error - Invalid deposit amount"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        """VALIDACION"""
        attr_value = super()._validate(attr_value)  # Checks the regex

        d_a_f = float(attr_value[4:])
        if d_a_f == 0:
            raise AccountManagementException("Error - Deposit must be greater than 0")

        return d_a_f