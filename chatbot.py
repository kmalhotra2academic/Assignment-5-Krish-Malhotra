"""
Description: Chatbot application.  Allows user to perform balance 
inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

# ACCOUNTS dictionary simulating account records
ACCOUNTS = {
    123456: {"balance": 1000.0},
    112233: {"balance": 2000.0},
    # More accounts can be added here
}

def get_account():
    """Asks the user for an account number and checks

    Returns:
        int: The validated account number.

    Raises:
        ValueError: If the account number is not valid or does not exist.
    """
    account = input("Please enter your account number: ")
    account = int(account)  # This will raise ValueError if not a valid integer
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    return account

def get_amount():
    """Ask the user for a deposit

    Raises:
        ValueError: If the amount is not positive or not numeric.
    """
    amount = input("Enter the transaction amount: ")
    amount = float(amount)  # This will raise ValueError if not a valid float
    if amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    return amount

def get_balance(account):
    """Gets the balance of the account    """
    balance = ACCOUNTS[account]["balance"]
    return f"Your current balance for account {account} is ${balance:,.2f}."

def make_deposit(account, amount):
    """Deposits the specified amount into the account.    """
    ACCOUNTS[account]["balance"] += amount
    return f"You have made a deposit of ${amount:,.2f} to account {account}."

def user_selection():
    """Prompts the user for their selection of a desired task.    """
    VALID_TASKS = {"balance", "deposit", "exit"}
    selection = input("What would you like to do (balance/deposit/exit)? ").strip().lower()
    if selection not in VALID_TASKS:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    return selection

def chatbot():
    
    print("Welcome! I'm the PiXELL River Financial Chatbot! Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            # Call the user_selection function here
            selection = user_selection()

            if selection != "exit":
                # Account number validation.
                valid_account = False
                while not valid_account:
                    try:
                        # Call the get_account function here
                        account = get_account()
                        valid_account = True  # Account retrieved successfully
                    except ValueError as e:
                        # Invalid account.
                        print(e)

                if selection == "balance":
                    # Call the get_balance function here
                    balance_message = get_balance(account)
                    print(balance_message)

                else:  # User selected 'deposit'
                    # Amount validation.
                    valid_amount = False
                    while not valid_amount:
                        try:
                            # Call the get_amount function here
                            amount = get_amount()
                            valid_amount = True  # Amount retrieved successfully
                        except ValueError as e:
                            # Invalid amount.
                            print(e)

                    # Call the make_deposit function here
                    deposit_message = make_deposit(account, amount)
                    print(deposit_message)
            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")

if __name__ == "__main__":
    chatbot()
