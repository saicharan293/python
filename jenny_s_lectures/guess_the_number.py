import random


logo='''
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
'''
print(logo)
print('let me think of a number 1 and 50 ')
answer=random.randint(1,50)
print('answer',answer)
level=input("Choose level of difficulty...Type 'e' for 'easy' , 'h' for 'hard' " )
EASY_ATTEMPTS=10
HARD_ATTEMPTS=5
def setDifficultyLevel(lev):
    if lev=='e':
        return EASY_ATTEMPTS
    elif lev=='h':
        return HARD_ATTEMPTS
    else:
        return

attempts=setDifficultyLevel(level)


def check_answer(guess,answer,attempts):
    if guess<answer:
        print("Your guess is too low")
        return attempts-1
    elif guess>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is right..., answer is {answer}")
guess=0

while guess!=answer:
    if attempts is None:
        print("you have entered wrong difficulty level!, play again...")
        break
    print(f'you have {attempts} attempts remaining')
    guess=int(input('Guess the number: '))   
    attempts=check_answer(guess,answer,attempts)
    if attempts==0:
        print("You are out of guess...you lose! ")
        break
    elif guess!=answer:
        print('guess again ')





