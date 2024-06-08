
#manual method
#expenses=[1,2,3,4,5,6]
# sum=0
# for i in expenses:
#     sum+=i

#expenses on user input
total=0
expenses=[]
userInput=int(input("Enter the number of receipts "))
for i in range(userInput):
    expenses.append(float(input("Enter the amount in bill: ")))

#in-built sum
total=sum(expenses)



print("Total expenses is equal to",total)
