import random
import Hang_man_stages
import Hang_man_words
# word_list=['apple','potato','beautiful']
chosen_word=random.choice(Hang_man_words.words)
lives=6
print(chosen_word)
display=[]
for _ in chosen_word:
    display.append('_')
ct=''.join(c for c in display)
print(ct)

game_over=False
while(not game_over):
    user_guess = input('Guess a letter ').lower()
    for position in range(len(chosen_word)):
        if chosen_word[position]==user_guess:
            display[position]=user_guess
    ct=''.join(c for c in display)
    print(ct)
    if user_guess not in chosen_word:
        lives-=1
        # print("no match")
        if lives==0:
            game_over=True
            print('You lose')
    if "_" not in display:
        game_over=True
        print("YOU Win")
    print(Hang_man_stages.stages[lives])