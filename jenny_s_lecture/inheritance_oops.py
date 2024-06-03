class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")

class Male(Human):
    def __init__(self,name,heart):
        #include init function from base class and override
        super().__init__(heart)
        self.name=name

    def swim(self):
        print("I can swim")
    #override eat method
    def eat(self):
        #also include method from base class
        super().eat()
        print("I am vegan")
    def det(self):
        print(f"Hi, I am {self.name} and I have {self.heart} heart/s")

male_1=Male('sai',5)

# male_1.eat()
# male_1.sleep()
# male_1.swim()
# print(male_1.eyes,male_1.nose)
# print(male_1.name)
male_1.det()