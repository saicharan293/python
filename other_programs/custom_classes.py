class Employee:
    def __init__(self,name,age,position,salary):
        self.name=name
        self.age=age
        self.position=position
        self.salary=salary
        #annual salary
        self._annual_salary=None

    def inc_salary(self,percent):
        self.salary+=self.salary*(percent/100)

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,salary):
        if salary<1000:
            raise ValueError('Minimum wage is $1000')
        self._annual_salary=None
        self._salary=salary

    @property
    #annual salary=computed property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary= self.salary*12
        return self._annual_salary

    def __str__(self):
        return (f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}")

    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {eval(self.position)}, {eval(self.salary)})"
    


e1=Employee('sai',23,'developer',1200)
e2=Employee('charan',24,'backend',1000)

print(e1.annual_salary)
# e1.set_salary(2000)
e1.salary=20000
print(e1.annual_salary)              

#abstraction and encapsulation
