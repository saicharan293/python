def display(name):
     return name

def do():
    print("this function is called")

# this is used to make this file standalone script(independent),
# instead affecting the file where this is imported
if __name__=='__main__':
    print('1st name main')
    na=input('enter your name: ')
    print(display(na))
    do()