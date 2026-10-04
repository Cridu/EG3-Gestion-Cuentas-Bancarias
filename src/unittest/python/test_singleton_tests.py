""" Singleton test cases """
from unittest import TestCase
from uc3m_money import (AccountManager,)
from uc3m_money.storage.deposits_json_store import  DepositsJsonStore
from uc3m_money.storage.balances_json_store import  BalancesJsonStore
from uc3m_money.storage.transfer_json_store import  TransfersJsonStore

class TestSingletonTests(TestCase):
    """Test class for deposit method"""
    def test_manager_equal_test(self):
        manager1 = AccountManager()
        manager2 = AccountManager()
        self.assertEqual(manager1, manager2)

    def test_deposit_equal_test(self):
        deposit1 = DepositsJsonStore()
        deposit2 = DepositsJsonStore()
        self.assertEqual(deposit1, deposit2)

    def test_balances_equal_test(self):
        balance1 = BalancesJsonStore()
        balance2 = BalancesJsonStore()
        self.assertEqual(balance1, balance2)

    def test_transfer_equal_test(self):
        transfer1 = TransfersJsonStore()
        transfer2 = TransfersJsonStore()
        self.assertEqual(transfer1, transfer2)
