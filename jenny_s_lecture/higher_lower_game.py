game_logo = '''  
  _    _ _       _               
 | |  | (_)     | |              
 | |__| |_  __ _| |__   ___ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__|
 | |  | | | (_| | | | |  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|   
  | |       __/ |                
  | |     _|___/     _____ _ __  
  | |    / _ \ \ /\ / / _ \ '__| 
  | |___| (_) \ V  V /  __/ |    
  |______\___/ \_/\_/ \___|_|    
                                 
'''
print(game_logo)

vs='''       
__   _____ 
\ \ / / __|
 \ V /\__ \
  \_/ |___/
  
'''

data = [
    {
        "name": "Virat Kohli",
        "follower_count": 130,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Priyanka Chopra",
        "follower_count": 90,
        "description": "Actress and singer",
        "country": "India"
    },
    {
        "name": "Shah Rukh Khan",
        "follower_count": 80,
        "description": "Actor and film producer",
        "country": "India"
    },
    {
        "name": "Deepika Padukone",
        "follower_count": 75,
        "description": "Actress",
        "country": "India"
    },
    {
        "name": "Alia Bhatt",
        "follower_count": 70,
        "description": "Actress",
        "country": "India"
    },
    {
        "name": "Narendra Modi",
        "follower_count": 65,
        "description": "Prime Minister of India",
        "country": "India"
    },
    {
        "name": "Amitabh Bachchan",
        "follower_count": 60,
        "description": "Actor",
        "country": "India"
    },
    {
        "name": "Akshay Kumar",
        "follower_count": 55,
        "description": "Actor",
        "country": "India"
    },
    {
        "name": "Salman Khan",
        "follower_count": 50,
        "description": "Actor and film producer",
        "country": "India"
    },
    {
        "name": "Sachin Tendulkar",
        "follower_count": 45,
        "description": "Former cricketer",
        "country": "India"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 550,
        "description": "Professional footballer",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 440,
        "description": "Professional footballer",
        "country": "Argentina"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 420,
        "description": "Singer and actress",
        "country": "USA"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 350,
        "description": "Actor and former professional wrestler",
        "country": "USA"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 340,
        "description": "Media personality and businesswoman",
        "country": "USA"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 330,
        "description": "Singer and actress",
        "country": "USA"
    },
    {
        "name": "Beyoncé",
        "follower_count": 290,
        "description": "Singer and actress",
        "country": "USA"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 280,
        "description": "Media personality and businesswoman",
        "country": "USA"
    },
    {
        "name": "Neymar Jr.",
        "follower_count": 270,
        "description": "Professional footballer",
        "country": "Brazil"
    }
]

import random
import os
cnt=True
score=0
account_2=random.choice(data)
while cnt:
    account_1 = account_2
    account_2 = random.choice(data)
    while(account_1==account_2):
        account_2=random.choice(data)
    def details(acc):
        name = acc['name']
        description = acc['description']
        country = acc['country']

        return f"{name}, {description}, from {country}"

    print(f"compare 1: {details(account_1)}")
    print(vs)
    print(f"compare 2: {details(account_2)}")
    choice=int(input('who has more followers? type 1 or 2 '))
    def check_answer(guess, count1, count2):
        if count1 < count2:
            if guess == 1:
                return False
            else:
                return True
        else:
            if guess == 1:
                return True
            else:
                return False
    is_correct=check_answer(choice, account_1['follower_count'], account_2['follower_count'])
    if is_correct==True:
        os.system('cls')
        score=score+1
        print(f"You are correct, Score is {score}")
    else:
        print(f"You are wrong, final score is {score}")
        cnt=False



