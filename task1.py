class bank_account():
    balance = 0.0
    
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,amount):
        self.balance
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self,amount):
        self.balance
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')

    def check_balance(self):
        print(f'Current balance: {self.balance}')


if __name__ == "__main__":
    bank = bank_account(100.0)
    bank.deposit(50)
    bank.withdraw(30)
    bank.check_balance()
        