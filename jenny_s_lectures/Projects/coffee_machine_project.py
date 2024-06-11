is_on=True
resources={
    'water':500,
    'milk':200,
    'coffee':100
}
menu={
    'lattee':{
        'ingredients':{
            'water':200,
            'milk':150,
            'coffee':24,
        },
        'cost':150
    },
    'espresso':{
        'ingredients':{
            'water':50,
            'coffee':18,
        },
        'cost':100
    },
    'cappuccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24,
        },
        'cost':200
    },
}
profit=0
def check_resources(order):
    for i in order:
        if order[i]>resources[i]:
            print(f"Sorry, there is no enough {i}")
            return False
    return True

def process_coins():
    print("Please enter coins. ")
    total=0
    five=int(input("How many 5 ruppee coins? "))
    ten=int(input("How many 10 ruppee coins? "))
    twenty=int(input("How many 20 ruppee coins? "))
    total=(five * 5)+(ten*10)+(twenty*20)
    return total

def is_paid(payment,cost):
    if payment>=cost:
        global profit
        profit+=cost
        change=payment-cost
        if change>0:
            print(f"Here is your Rs{change} in change.")
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded..")
        return False

def make_coffee(name, ing_dict):
    for item in ing_dict:
        resources[item]-=ing_dict[item]
    print(f"Here is your {name} ☕... Have a great day!")
while is_on:
    choice =input("What would you like to have?\n"
                  "(lattee/espresso/cappuccino)\n"
                  "enter 'o' to turn off\n"
                  "enter 'r' for report ")
    if choice=='o':
        is_on=False
    elif choice=='r':
        print(f"water is {resources['water']} ml\n"
              f"milk is {resources['milk']} ml\n"
              f"coffee is {resources['coffee']} gm\n"
              f"money is {profit}")
    else:
        coffeeType=menu[choice]
        print(coffeeType)
        if check_resources(coffeeType['ingredients']):
            pay=process_coins()
            if is_paid(pay,coffeeType['cost']):
                make_coffee(choice,coffeeType['ingredients'])
    # print('Please insert coins')
