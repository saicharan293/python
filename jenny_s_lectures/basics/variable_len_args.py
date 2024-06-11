#*num = arbitrary positional arguments(variable length arguments)
def add(*num):
    c=0
    for i in num:
        c=c+i
        # print(c)
    print(f"sum of numbers is {c}")
add(1,2,3,4,5,6,7,7)