
# purely meant for object creation with no inheritence
class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def calculation_pay(self):
        return self.salary/52
    
