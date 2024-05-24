from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = 0
        self.date_of_opening = datetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")

account = BankAccount("123456789", "John Doe")
account.deposit(1000)
account.withdraw(500)
account.check_balance()
