# user_choice=input("Type 'encrypt' for encryption , or 'decrypt' for decryption: \n")
# msg=input("Enter your message: \n")
# shift_count=int(input("Enter the number of shifts \n"))

alpha=['a','b','c','d','e','f','g','h','i','j',
       'k','l','m','n','o','p','q','r','s','t',
       'u','v','w','x','y','z']
# def encryption(msg,shift_count):
#     cypher_text=''
#     for char in msg:
#         if char in alpha:
#             position=alpha.index(char)
#             new_position=(position+shift_count)%26
#             cypher_text+=alpha[new_position]
#         else:
#             cypher_text+=char
#     print(f"Here's the text after encryption: {cypher_text}")
#
# def decryption(cypher_text,shift_count):
#     plain_text=''
#     for char in cypher_text:
#         if char in alpha:
#             position=alpha.index(char)
#             new_position=(position-shift_count)%26
#             plain_text+=alpha[new_position]
#         else:
#             plain_text+=char
#     print(f"Here's the text after encryption: {plain_text}")

def crypt(text,shift_count):
    plain_text = ''
    for char in text:
        if char in alpha:
            position = alpha.index(char)
            new_position = (position + shift_count) % 26
            plain_text += alpha[new_position]
        else:
            plain_text += char
    print(f"Here's the text after encryption: {plain_text}")
end=False
while not end:
    user_choice = input("Type 'encrypt' for encryption , or 'decrypt' for decryption: \n")
    msg = input("Enter your message: \n").lower()
    shift_count = int(input("Enter the number of shifts \n"))
    if user_choice=='encrypt':
        # encryption(msg,shift_count)
        crypt(msg,shift_count)
    elif user_choice=='decrypt':
        # decryption(msg,shift_count)
        crypt(msg,-shift_count)
    else:
        print("Enter the correct choice ")
        continue
    again=input("Type 'yes' to continue, 'no' to exit \n")
    if again=='no':
        end=True
        print("Thank you & Have a nice day")