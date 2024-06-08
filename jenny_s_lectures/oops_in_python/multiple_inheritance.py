class Human:
    def __init__(self,heart):
        print("Human init ")
        self.eyes=2
        self.nose=1
        self.heart=heart
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
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def sleep(self):
        print("I wannt sleep")
    def display(self):
        print(f"Hi, I am,{self.name} and I work on {self.language}")

boy_1=Boy("sai",1,"python")
# boy_1.run()
# print(boy_1.nose)
# print(boy_1.heart)
# print(boy_1.language)
boy_1.display()
#to access run method in Male class
# Male.work(boy_1)
# method resolution order: order in which methods
#                          can be accessed according to the hirarchy
# print(Boy.__mro__) or
# print(Boy.mro())
