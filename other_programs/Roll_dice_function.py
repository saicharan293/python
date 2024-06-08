
import random


player1=input("Enter player one name ")
player2=input("Enter player two name ")
def roll_dice():
    total_score=random.randint(1,6)+random.randint(1,6)
    return total_score



def main():
    roll1=roll_dice()
    roll2=roll_dice()

    print("roll 1 is",roll1)
    print("roll 2 is",roll2)
    if roll1>roll2:
        print(player1,'WIN')
    elif roll2>roll1:
        print(player2,'WIN')
    else:
        print("YOU TIE")

main()
