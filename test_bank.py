import bank

class Bank_test:
    def test_balance(self):
        account1 = bank("Name", 30456, 30)
        account2 = bank("Name2", 12345)
        self.assertEqual(account1.balance, 30)
        self.assertEqual(account2.balance, 0)
        self.assertNotEqual(account1.balance, account2.balance)