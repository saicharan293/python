# method overloading => Compile time polymorphism=> method calling is done at compile time,
#                        occurs in same class
#                       same name but different parameters


# method overloading is not available in python,
#  so it would take the latest method definition
# possible ways: use of default arguments,variable length argument(*args)
from multipledispatch import dispatch
class Demo:

    # using default args
    # def add(self,a,b,c=0):
    #     return f'sum is {a+b+c}'


    #using variable length args (*args) and loop if req
    # def add(self,*args):
    #     total=0
    #     for _ in args:
    #         total+= _
    #     return f'first, sum = {total}'
    
    #using dispatch decorator
    @dispatch(int, int)
    def add(self, a, b):
      return f'second,sum = {a+b}'
    @dispatch(int, int, int)
    def add(self, a, b, c):
        # x = a+b+c
        return f'third,sum = {a+b+c}'
        
        
d=Demo()
# print(d.add(2,3))
print(d.add(2,3,))
print(d.add(1,2,3))