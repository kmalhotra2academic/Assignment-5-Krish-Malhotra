"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection, ACCOUNTS

class ChatbotTests(unittest.TestCase):

    def setUp(self):
        # Reset the ACCOUNTS dictionary to a known state
        self.test_accounts = {
            123456: {"balance": 1000.0},
            112233: {"balance": 2000.0},
        }
        global ACCOUNTS
        ACCOUNTS = self.test_accounts

    def test_get_account_valid(self):
        """Test getting a valid account number."""
        with patch('builtins.input', return_value='123456'):
            account = get_account()
            self.assertEqual(account, 123456)

    def test_get_account_invalid_non_numeric(self):
        """Test getting a non-numeric account number."""
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                get_account()

    def test_get_account_invalid_non_existent(self):
        """Test getting a non-existent account number."""
        with patch('builtins.input', return_value='999999'):
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_get_amount_valid(self):
        """Test getting a valid deposit amount."""
        with patch('builtins.input', return_value='1500'):
            amount = get_amount()
            self.assertEqual(amount, 1500.0)

    def test_get_amount_invalid_non_numeric(self):
        """Test getting a non-numeric amount."""
        with patch('builtins.input', return_value='abc'):
            with self.assertRaises(ValueError):
                get_amount()

    def test_get_amount_invalid_negative(self):
        """Test getting a negative amount."""
        with patch('builtins.input', return_value='-50'):
            with self.assertRaises(ValueError):
                get_amount()

    def test_get_balance_valid(self):
        """Test getting balance of a valid account."""
        balance_message = get_balance(123456)
        self.assertEqual(balance_message, "Your current balance for account 123456 is $1,000.00.")

    def test_make_deposit_valid(self):
        """Test making a deposit to a valid account."""
        deposit_message = make_deposit(123456, 500.0)
        self.assertEqual(deposit_message, "You have made a deposit of $500.00 to account 123456.")
        self.assertEqual(ACCOUNTS[123456]["balance"], 1500.0)  # Check updated balance

    def test_make_deposit_account_does_not_exist(self):
        """Test making a deposit to a non-existent account."""
        with self.assertRaises(KeyError):
            make_deposit(999999, 500.0)

    def test_make_deposit_invalid_amount(self):
        """Test making a deposit with an invalid amount."""
        with self.assertRaises(ValueError) as context:
            make_deposit(123456, -50.0)
        self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")

    def test_user_selection_valid_lowercase(self):
        """Test user selection with valid lowercase input."""
        with patch('builtins.input', return_value='balance'):
            selection = user_selection()
            self.assertEqual(selection, 'balance')

    def test_user_selection_valid_uppercase(self):
        """Test user selection with valid uppercase input."""
        with patch('builtins.input', return_value='DEPOSIT'):
            selection = user_selection()
            self.assertEqual(selection, 'deposit')

    def test_user_selection_invalid(self):
        """Test user selection with invalid input."""
        with patch('builtins.input', return_value='withdraw'):
            with self.assertRaises(ValueError) as context:
                user_selection()
            self.assertEqual(str(context.exception), "Invalid task. Please choose balance, deposit, or exit.")

if __name__ == "__main__":
    unittest.main()