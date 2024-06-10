class Father:
    def sleep(self):
        print(f'sleeps from 11:30 to 9:30')

    def eat(self):
        print('can eat')

class Son(Father):
    pass
sai=Son()

sai.sleep()
sai.eat()