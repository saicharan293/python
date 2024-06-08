class Human:
    can_breath=True
    def __init__(self,heart):
        self.eyes = 2
        self.heart = heart
    def eat(self):
        print(f"I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print("I can sleep")
class Boy(Male):
    #heart from Human class and name from Male class
    def __init__(self,dance,name,heart):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.dance=dance

    def work(self):
        # Human.work(self) (or)
        super().work()
        print("I can code")

boy_1=Boy('yes','sai',1)
# boy_1.work()
# print(boy_1.eyes)
print(f'{boy_1.name} has {boy_1.eyes} eyes, '
      f'{boy_1.heart} heart, can dance:{boy_1.dance} ')
# print(Boy.mro())
print(f"{boy_1.can_breath}")