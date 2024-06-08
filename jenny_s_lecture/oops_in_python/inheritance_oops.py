class Human:
    def __init__(self,ears):
        self.eyes=2
        self.nose=1
        self.ears=ears
    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")

class Male(Human):
    def __init__(self,name,ears):
        #include init function from base class and override
        super().__init__(ears)
        self.name=name

    def swim(self):
        print("I can swim")
    #override eat method
    def eat(self):
        #also include method from base class
        super().eat()
        print("I am vegan")
    def det(self):
        print(f"Hi, I am {self.name} and I have {self.ears} ears")

male_1=Male('sai',2)

# male_1.eat()
# male_1.sleep()
# male_1.swim()
# print(male_1.eyes,male_1.nose)
# print(male_1.name)
male_1.det()