class Robot:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print("Boww Boww")

robot_dog=Robot('Tommy','Roxy')
print(robot_dog.name)
print(robot_dog.breed)
robot_dog.bark()