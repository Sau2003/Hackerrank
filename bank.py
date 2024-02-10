
class Bank_Account:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful, Current balance is {self.balance}")
        else:
            print("Invalid amount, Deposit failed.")

    def withdraw(self, amount):
        if amount>0 and amount<self.balance:
            self.balance=self.balance-amount
            print(f"Withdrawal of {amount} is successful,Current balance is {self.balance}")
        else:
            print("Insufficient balance, failed ! ")

    def get_balance(self):
        print(f"Account balance: {self.balance}")

account = Bank_Account("Sau", 100)
account.get_balance()  
account.deposit(1000)
account.withdraw(2000)
account.get_balance()