class Employee:
    def __init__(self, name, age, position, salary):
        self.name=name
        self.age=age
        self.position=position
        self.salary=salary
    
    def inc_salary(self,percent):
        self.salary+=self.salary*(percent/100)
    
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)},{repr(self.age)},"
            f"{repr(self.position)},{repr(self.salary)})"
        )
e1=Employee('sai',23,'front end',20000)
e2=Employee('charan',24,'back end',24000)
print(eval(repr(e1)))
print(eval(repr(e2)))