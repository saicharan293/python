
import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
operators={
    "+":add,
    '-':sub,
    '/':div,
    '*':mul
}

def calculator():
    first=float(input("Enter first number "))
    for _ in operators:
        print(_)
    continue_flag=True
    while continue_flag:
        operator=input("Pick up an operator ")
        second=float(input("Enter second number "))
        calculate=operators[operator]
        output=calculate(first,second)
        print(f"{first} {operator} {second} = {output}")
        choice=input(f"Enter 'y' to continue to calculation with {output} or 'n' to start new calculation or 'x' to exit ")
        if choice=='y':
            first=output
        elif choice=='n':
            continue_flag=False
            # os.system('cls')
            calculate()
        else:
            continue_flag=False
            print(f"Thank you")
    
calculator()