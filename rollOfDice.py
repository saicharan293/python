import random
roll=random.randint(1,6)

#print("roll is",str(roll))
guess=int(input("Guess the number on dice "))
if(guess==roll):
    print("Correct! They rolled a "+str(roll))
else:
    print("Wrong ! They rolled a "+str(roll))