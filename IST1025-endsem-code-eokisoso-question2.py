class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing {amount}")

    def withdraw(amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawing {amount}")
        else:
            print("Error: Insufficient funds for withdrawal.")

    def get_balance():
        return self.balance



