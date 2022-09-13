class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print("int_rate",self.int_rate,"balnce is",self.balance)
        return self

    def yield_interest(self):
        self.balance +=self.int_rate * self.balance
        return self

bank1=BankAccount(10.2,2000)
bank2=BankAccount(2.7,1500)

bank1.deposit(10).deposit(20).deposit(44).withdraw(100).yield_interest().display_account_info()
bank2.deposit(10).deposit(20).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
