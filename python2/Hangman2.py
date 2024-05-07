import random
words_list=['sai','charan','amudala','list']

choosen_word=random.choice(words_list)

attempts=len(choosen_word)
display=['_' for _ in choosen_word]
print('Welcome to the Hangman game')
while attempts>0 and '_' in display:
    print('\n'+' '.join(display))
    print(f'choosen_word : {choosen_word}')
    guess=input('Guess a letter in above word: ')
    if guess in choosen_word:
        # using enumerate function: provides index and the letter
        # for index,letter in enumerate(choosen_word):
        #     if letter==guess:
        #         display[index]=guess
        for i in range(len(choosen_word)):
            if choosen_word[i]==guess:
                display[i]=guess
    else:
        attempts-=1
        print(f'failed, left over attempts are {attempts}')

if '_' not in display:
    print('You guessed it correctly')
    print(' '.join(display))
    print('you survived')
else:
    print(f'The original word is {choosen_word}')
    print("Failed, but good attempt!")


