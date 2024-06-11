#*args = arbitrary positional arguments
#**kwargs= arbitrary keword arguments

def add(*num):
    c=0
    for _ in num:
        c=c+_
    print(f"sum is {c}")
# add(1,2,4)

#key word args
def add2(*num, name):
    c=0
    print(num)
    print(name)
    for _ in num:
        c=c+_
    print(f"second sum is {c}")
# add2(1,2,name='sai')

#positional args(normal) along with variable length args
def add3(a,*num):
    c=0
    print(a)
    print(num)
    for _ in num:
        c=c+_
    print(f"third sum is {c}")
# add3(1,2,3)

#arbitrary keyword arguments=> accessed using dictionary form
# using index, value in kwargs.items()
def info_person(**kwargs):
    for index,value in kwargs.items():
        print(index,value)
# info_person(name='sai',age=23,dept='CS')
# info_person(name='charan',dept='ECE')

#arbitrary positional arguments and arbitrary keyword arguments
def info_person2(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
    print('-'*10)
# info_person2(1,2,name='sai',dept='CS',age=23)
# info_person2(5,8,name='shiva',dept='IT')

#assignment
def multiply(*args):
    c=1
    for _ in args:
        c=c*_
    print(f"multiplication result is {c}")
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)