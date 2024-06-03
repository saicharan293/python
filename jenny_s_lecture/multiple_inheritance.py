class Human:
    def eat(self):
        print('I can eat')
    def work(self):
        print("I can work")

class Male:
    def run(self):
        print("I can run")
    def work(self):
        print("I can code")

class Boy(Human,Male):
    pass

boy_1=Boy()
boy_1.run()