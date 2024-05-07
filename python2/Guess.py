import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    # print('rand is ',random_number)
    while (guess!=random_number):
        guess=int(input(f"Guess number between 1 and {x} "))
        if guess>random_number:
            print("it's too high, try low")
        elif guess<random_number:
            print("it's too low, grow it")
    print("you did it !")
# guess(5)

def computer_guess(x):
    low = 1
    high= x
    feedback=''
    while(feedback!='c'):
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high(H) or too low(L) or correct(c)").lower()
        if feedback=='h':
            high=guess - 1
        if feedback=='l':
            low=guess + 1
    print(f'Computer guessed the number {guess}')
computer_guess(10)

