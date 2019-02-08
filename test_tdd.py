import unittest
from bank_account import BankAccount, SubClass


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.my_account = BankAccount()
    
    def test_balance(self):
        self.assertEqual(self.my_account.balance, 5000, msg='Not able to retrieve account balance') 

    def test_deposit(self):
        self.my_account.deposit(3000)
        self.assertEqual(self.my_account.balance, 8000, msg='Inncorec deposit')

    def test_withdraw(self):
        self.my_account.withdraw(1000)
        self.assertEqual(self.my_account.balance, 4000, msg='Too much withdraw')

    def test_subclass(self):
        self.assertTrue(issubclass(SubClass, BankAccount), msg='Not a subclass')