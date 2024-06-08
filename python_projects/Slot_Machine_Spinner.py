import random
MAX_LINES=3

#1. Fill the Gaming Wallet
def deposit():
    while True:
        amount=input("Enter your deposit amount? Rs ")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print('Please enter valid number')
    return amount

#2. number of rows 
def num_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print('Enter valid number of lines.')
        else:
            print('Enter valid number. ')
    return lines

MIN_BET=20
MAX_BET=100

#3 Valid the bet money
def get_bet():
    while True:
        bet_amt=input("Enter the bet amount...")
        if bet_amt.isdigit():
            bet_amt=int(bet_amt)
            if MIN_BET <= bet_amt <= MAX_BET:
                break
            else:
                print(f'Enter the valid bet amount between {MIN_BET} and {MAX_BET}')
        else:
            print('Please enter the valid number')
    return bet_amt

ROWS=3
COLS=3
SYMBOLS={
    'A':2,
    'B':4,
    'C':6,
    'D':8
}
SYMBOL_VALUES={
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

#4 get the columns of the slot machine
def get_slot_machine(rows,cols,symbols):    
    all_symbols=[]

    #SYMBOLS converted into list
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    #Distributions of symbols into each column
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


#to transpose rows and columns
#5. print all the columns in form of rows
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=' | ')
            else:
                print(column[row])
        # print()

# 6. Check number of rows filled with desired symbol 
def check_wins(values,columns,lines,bet):
    wins=0
    winning_lines=[]
    #check the line number
    for line in range(lines):
        #first symbol present in specific line
        symbol=columns[0][line]
        
        #we need to consider each column
        for column in columns:
            #collect symbol at that column
            symbol_to_check=column[line]

            #check if the symbol is same or not
            if symbol != symbol_to_check:
                break
        else:
            wins+=values[symbol] * bet
            winning_lines.append(line + 1)

    return wins,winning_lines


# 7. Start the game of spin 

def spin(balance):
    lines=num_lines()
    while True:
        bet=get_bet()
        total_bet=bet * lines
        if total_bet > balance:
            print(f'You do not have enough balance, since your current balance is {balance}')
        else:
            break
    
    print(f'You are betting {bet} Rs on {lines} lines. Total bet is {total_bet}')
    slots=get_slot_machine(ROWS,COLS,SYMBOLS)
    print_slot_machine(slots)
    winnings,winning_lines=check_wins(SYMBOL_VALUES,slots,lines,bet)
    print(f'you won {winnings} on ', *winning_lines)
    return winnings - total_bet


# 8. Initiate the main 
def main():
    balance=deposit()
    while True:
        print(f"current balance is {balance}")
        enter=input('Press enter to play or q to quit ')
        if enter == 'q':
            break
        balance+=spin(balance)
        print(f'you left with {balance}')

# 9. main function call 
main()