# Design a BankAccount class with methods for deposit, withdrawal, and balance inquiry.
class BankAccount:
    def __init__(self,amount=0):
        self.amount = amount
        print(f"Balance is: {self.amount}")
    
    def deposit(self,amountNum):
        if(amountNum < 0):
            print(f"deposit Balance cannot be entered in negative values")
        else:
            self.amount += amountNum
            print(f"Balance after deposit: {self.amount}")
    
    def withdraw(self,amountNum):
        if(self.amount < amountNum):
            print(f"Sorry your Balance is less than the amount you input:")
            print(f"Your Balance is: {self.amount}")
        elif(amountNum < 0):
            print(f"withdraw Balance cannot be entered in negative values")
        else:
            self.amount -= amountNum
            print(f"Balance after withdrawal: {self.amount}")
    
    def get_balance(self):
        print(f"Balance is: {self.amount}")

account = BankAccount()
account.deposit(2000)
account.withdraw(-500)
account.withdraw(500)
account.deposit(-300)
account.get_balance()
account.withdraw(1500)