
#method overloading is not available in python,
#  so it would take the latest method definition
# possible ways: use of default arguments,variable length argument(*args)

class Demo:

    # using default args
    # def add(self,a,b,c=0):
    #     return f'sum is {a+b+c}'

    #using variable length args (*args) and loop if req
    def add(self,*args):
        total=0
        for _ in args:
            total+= _
        return f'sum = {total}'
    
        
d=Demo()
# print(d.add(2,3))
print(d.add(2,3,4))
print(d.add(1,2,3,4,5,5))