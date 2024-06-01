a=10 #global
def display():
    a=15 #local
    print('inside display',a)
print('outside display',a)
display()