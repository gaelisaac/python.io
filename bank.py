# bank program
import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = datetime.date.today()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            raise ValueError("Deposit amount must be greater than zero")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return amount
            else:
                return "Insufficient balance"
        else:
            raise ValueError("Withdrawal amount must be greater than zero")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Current Balance: {self.balance}")

# Example usage
account = BankAccount(123456789, "John Doe", 500)
account.deposit(100)
print(account.withdraw(50))
account.check_balance()
account.customer_details()