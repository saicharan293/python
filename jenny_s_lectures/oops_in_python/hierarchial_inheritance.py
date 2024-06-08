class Human:
    def __init__(self,name,age):
        # print("from human init")
        self.name=name
        self.age=age
    def show_details(self):
        print(f"name: {self.name} and age: {self.age}")
    def eat(self):
        print("i can eat")
class Male(Human):
    def __init__(self,name,age,location):
        print("Male init")
        super().__init__(name,age)
        self.location=location
    def sleep(self):
        print("I can sleep, whole day")
class Female(Human):
    def __init__(self,name,age,dance):
        print("Female init")
        super().__init__(name,age)
        self.dance=dance
    def show_details(self):
        super().show_details()
        print(f"{female_1.name} Know dancing: {self.dance}")
    def work(self):
        print("I can do lot of work")

female_1=Female("Sati",28,"yes")
# female_1.work()
# female_1.eat()
female_1.show_details()
# print(f"Can she dance: {female_1.dance}")
# male_1=Male("shiva",29,"kurnool")
# print(Male.mro())