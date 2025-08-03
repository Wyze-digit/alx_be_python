#
# 
class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initializes the account with an optional initial balance.
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Adds the given amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the given amount from the balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")


