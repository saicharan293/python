print("grocery list programs")

grocery_list=[]

while True:
    user_input=input("input an item(type 'end' to finish): ")
    if user_input=='end':
        break
    grocery_list.append(user_input)

print("Here is the list of groceries: ")
for item in grocery_list:
    print(f"{item}")
    
for item in grocery_list:
    if item=='bread':
        print('Bread is on the list')
        break
else:
    print("Bread is not in the list")