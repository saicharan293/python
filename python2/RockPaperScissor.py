import random
def play():
    user=input("'r' for rock, 'p' for paper,'s' for scissors ")
    computer=random.choice(['r','p','s'])
    print('computer choice is ',computer)
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return ('you won!!!')
    return 'you lost!'


def is_win(user,opp):
    if(user=='r' and opp=='s') or (user=='p' and opp == 'r') or (user == 's' and opp == 'p'):
        return True
print(play())