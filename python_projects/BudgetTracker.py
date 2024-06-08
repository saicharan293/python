def add_expenses(expenses,description,amt_spent):
    expenses.append({'description':description,'amt_spent':amt_spent})
    print(f'Added expense: {description}, Amount: {amt_spent}')

def show_budget(budget,expenses,amt_spent):
    print('Expenses')
    for e in expenses:
        print(f"- {e['description']}: {e['amt_spent']}")
    print(f'Amount spent: {amt_spent}')
    print(f'Remaining budget: {budget}')
def budget_tracker():
    expenses=[]
    print('welcome to the budget app')
    total_budget=float(input('Please enter your budget: '))
    budget=total_budget
    # amt_spent=0
    while budget>=0:
        print('What would you like to do ?')
        print('1. Add an expense\n2. Show budget detail\n3. Exit')
        choice=input('Enter your choice (1/2/3) : ')
        if(choice=='1'):
            description=input('Enter expense description ')
            amt_spent=float(input('Enter expense amount '))
            # print(f'Added expense: {description}, Amout: {amt_spent}')
            if(amt_spent>budget):
                print('check your budget')
                return
            else:
                budget=budget - amt_spent
                add_expenses(expenses,description,amt_spent)
            # budget_tracker(amt_spent)
        elif(choice=='2'):
            print(f'Total budget: {total_budget}')
            show_budget(budget,expenses,amt_spent)
        else:
            return
    else:
        print('Please check your budget amt ')

budget_tracker()