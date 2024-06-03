class Human:
    def __init__(self):
        print("Human init ")
    def eat(self):
        print('I can eat')
    def work(self):
        print("I can work")

class Male:
    def __init__(self,name):
        print("Male init")
        self.name=name
    def run(self):
        print("I can run")
    def work(self):
        print("I can code")

class Boy(Human,Male):
    def __init__(self,name):
        Male.__init__(self,name)

boy_1=Boy("sai")
boy_1.run()
#to access run method in Male class
Male.work(boy_1)
# method resolution order: order in which methods
#                          can be accessed according to the hirarchy
# print(Boy.__mro__) or
print(Boy.mro())
