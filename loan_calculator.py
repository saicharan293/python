loan_amt=float(input("What's the loan/rent amount? "))
ann_per_rate=float(input("What's the annual percentage rate? "))
pay_now=float(input("How much amount are you going to pay now? "))
months=int(input("How many months do you need "))
monthly_rate=ann_per_rate/100/12

for i in range(months):
    int_rate=loan_amt*monthly_rate
    loan_amt=loan_amt+int_rate
    if(loan_amt-pay_now<0):
        print(f"last payment is ₹{loan_amt:,.2f}")
        print("You paid in",i+1,'months')
        break
    loan_amt=loan_amt-pay_now
    print(f'Paid ₹{pay_now:,.2f} of which {int_rate:,.2f} was interest')
    print(f'Now I owe ₹{loan_amt:,.2f}')
