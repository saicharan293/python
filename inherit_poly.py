class Employee:

    __slots__=('name','age','salary')

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def inc_salary(self, percent):
        self.salary+=self.salary*(percent/100)
    
    def has_slots(self):
        return hasattr(self,"__slots__")

class Tester(Employee):
    def run_tests(self):
        print("Testing is started by",self.name+'...')
        print("Tests are done")

class SlotsInspectorMixin:
    def has_slots(self):
        return hasattr(self,"__slots__")

class Developer(SlotsInspectorMixin, Employee):
    #to add new data variable to the class
    __slots__=("framework",)
    def __init__(self,name,age,salary,framework):
        super().__init__(name,age,salary)
        self.framework=framework

    def inc_salary(self,percent,bonus=0):
        super().inc_salary(percent)
        self.salary+=bonus
       
    

t1=Tester('satish',24,20000)
d1=Developer('sai charan',23,23000,"Flask")

print(isinstance(t1,Tester))
print(isinstance(d1,Developer))

print(issubclass(Developer,Employee))
print(issubclass(Developer,object))
print(issubclass(Tester,object))
# print(d1.has_slots())
# print(Developer.__mro__)
# print(d1.__dict__)

# print(d1.name)
# print(d1.framework)

# class Tester(Employee):
#     def run_tests(self):
#         print("Testing is started by",self.name+'...')
#         print("Tests are done")