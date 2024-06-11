class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def __str__(self):
        return f"Account holder: {self.name}\tBalance: {self.balance}"
    
ramesh=BankAccount('Ramesh',20000)
print(ramesh)