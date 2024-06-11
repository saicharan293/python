class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,deposit):
        self.balance+=deposit
        print(f"Deposited {deposit}rs into {self.name}'s account")
    
    def withdraw(self,amt):
        if amt>self.balance:
            print(f"{self.name} cannot withdraw {amt}rs, since balance is {self.balance}rs")
        else:
            self.balance-=amt
            print(f"{self.name} withdrew {amt}rs, remaining balance: {self.balance}rs")
    def __str__(self):
        return f"Account holder: {self.name}\nBalance: {self.balance}rs"
    
ramesh=BankAccount('Ramesh',20000)
# print(ramesh)
ramesh.deposit(5000)
ramesh.withdraw(3000)
# print(ramesh)