class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    #__add__()=> add method run in the back ground of '+' operator, 
    # so we can manipulate the method according to our requirement
    def __add__(self,other):
        return f'{self.real+other.real} + {self.imaginary+other.imaginary}i'

    

c=Complex(2,3)
c2=Complex(5,7)
# print(c+c2)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #greater than operator is overloaded through object passing
    
    def __gt__(self,person):
        if self.age>person.age:
            return f'{self.name} will pay the bill'
        else:
            return f'{person.name} will pay the bill'
        
p1=Person('sai',54)
p2=Person('AVS',22)

print(p1>p2)

# operator overloading:
# -----------------------
# __lt__ => less than 
# __le__ => less than or equal to 
# __gt__ => greater than
# __ge__ => greater than or equal to 
# __eq__ => equal
# __ne__ => not equal 
# __add__ => add 
# __sub__ => sub 
# __mul__ => mul
# __truediv__ => quotient
# __mod__ => remainder