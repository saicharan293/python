from datetime import date


class Employee:

    min_wage=1000

    @classmethod # Also known as "Factory functions"
    def change_minimum_wage(cls,new_wage):
        if new_wage>3000:
            raise ValueError("Company is bankrupt")
        cls.min_wage=new_wage

    @classmethod # Also known as "Factory functions"
    #this can be referred as alternative constructors since it returns prepopulated instance with default values
    def new_emp(cls,name,dob):
        now=date.today()
        age=now.year-dob.year-((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.min_wage)

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

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
    


# e1=Employee('sai',23,1200)
# e2=Employee('charan',24,1000)
    
e=Employee.new_emp('sai',date(2000,3,2))
print(e.name)
print(e.age)
print(e.salary)


# print(Employee.min_wage)
# Employee.change_minimum_wage(200)
# print(Employee.min_wage)
#abstraction and encapsulation
