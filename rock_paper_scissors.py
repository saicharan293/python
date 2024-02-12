import random

computer_choice=random.choice(['rock','paper','scissors'])

print("computer choice",computer_choice)

my_choice=input("Enter your choice ")

if computer_choice==my_choice:
    print("TIE")
elif computer_choice=='rock' and my_choice=='paper':
    print("WIN !")
elif computer_choice=='paper' and my_choice=='scissors':
    print("WIN !")
elif computer_choice=='scissors' and my_choice=='rock':
    print("WIN !")
else:
    print("LOOSE...")