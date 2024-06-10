
#method overriding => Run time polymorphism => at run time, it decides the respective method is called. 
#                       occurs in inheritance(2 classes), 
#                       same name but different method body(logic) but same parameters
class Father:
    def sleep(self):
        print(f'father sleeps from 9:30 to 5:30')

    def eat(self):
        print('can eat')

class Son(Father):
    def sleep(self):
        print('son sleeps from 11:30 to 8:30')
        super().sleep()
sai=Son()

sai.sleep()
sai.eat()