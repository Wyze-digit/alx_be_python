#
#
import sys
from bank_account import BankAccount

def main():
    # Create an instance of BankAccount with a starting balance (you can modify this default)
    account = BankAccount(100.0)  # Starting balance set to ₦100

    # Ensure the user provides a command argument
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract command and optional amount from the argument
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle deposit
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ₦{amount:.2f}")
        account.display_balance()

    # Handle withdrawal
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ₦{amount:.2f}")
        else:
            print("Insufficient funds.")
        account.display_balance()

    # Handle display
    elif command == "display":
        account.display_balance()

    # Handle invalid command
    else:
        print("Invalid command. Please use: deposit:<amount>, withdraw:<amount>, or display")

if __name__ == "__main__":
    main()


